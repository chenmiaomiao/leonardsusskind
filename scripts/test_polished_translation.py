import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
from unittest.mock import patch
import polished_translation as p


class TranslationTests(unittest.TestCase):
    def test_lossless_math_and_paths(self):
        source = r'\section{Motion} A field $x^2$ has 2 states.\begin{equation}E=mc^2\end{equation}\includegraphics[width=.8\textwidth]{board_1.png}'
        text, frozen = p.protect(source)
        self.assertEqual(p.restore(text, frozen), source)
        self.assertNotIn('E=mc', text)
        self.assertNotIn('board_1', text)
        self.assertIn('Motion', text)

    def test_heading_intro_and_caption_are_translatable(self):
        text, frozen = p.protect(r'\section{Heading}' + '\n\nIntroduction.\n\n' + r'\begin{figure}[tbp]\includegraphics{x.png}\caption{A board}\lectureframe{00:12:34}\end{figure}')
        for word in ['Heading', 'Introduction', 'A board']:
            self.assertIn(word, text)
        self.assertNotIn('00:12:34', text)
        self.assertNotIn('tbp', text)

    def test_no_unsafe_model_syntax(self):
        self.assertIsNotNone(p.validate('Hello', r'\input{secret}', 'ja'))
        self.assertIsNotNone(p.validate('@@T000000@@ Hello', 'こんにちは', 'ja'))
        self.assertIsNotNone(p.validate('Hello', 'こんにちは 3', 'ja'))

    def test_url_protected_link_title_translated(self):
        text, _ = p.protect(r'\href{https://example.com}{Readable title}')
        self.assertNotIn('example.com', text)
        self.assertIn('Readable title', text)

    def test_math_table_and_question(self):
        source = r'\begin{classroomqa}\audiencequestion{Why $x$?}\lecturerresponse{Because $y$.}\end{classroomqa}'
        masked, tokens = p.protect(source)
        self.assertIn('Why', masked)
        self.assertIn('Because', masked)
        self.assertEqual(p.restore(masked, tokens), source)

    def test_only_words_trigger_translation(self):
        self.assertFalse(p.needs_translation('@@T000001@@\n\n'))
        self.assertTrue(p.needs_translation('@@T000001@@Introduction'))

    def test_valid_number_word_translation(self):
        self.assertIsNone(p.validate('the six quark flavors', '6種類のクォークフレーバー', 'ja'))
        self.assertIsNotNone(p.validate('the six quark flavors', '7種類のクォークフレーバー', 'ja'))
        self.assertIsNone(p.validate('one and a half times, at two standard deviations', '1.5倍で2標準偏差', 'ja'))

    def test_accented_name_is_atomic(self):
        source = r'Fran\c{c}ois Englert found it.'
        masked, frozen = p.protect(source)
        self.assertNotIn('Fran', masked)
        self.assertEqual(frozen[0], r'Fran\c{c}ois')
        self.assertEqual(p.restore(masked, frozen), source)

    def test_retry_only_failed_segment_then_resume_without_calls(self):
        with TemporaryDirectory() as tmp, patch.object(p, 'WORK', Path(tmp)):
            book = {'id': 'fixture', 'titles': {'en': 'Physics', 'ja': '物理'}}
            rel = 'chapters/lecture_01/content.tex'
            prepared = {'source_sha256': 'test', 'parts': ['First paragraph.', '\n\n', 'Second paragraph.'], 'protected': []}
            p.write(p.WORK / 'prepared/fixture' / (rel + '.json'), prepared)
            prompts = []

            def fake_chat(prompt, dest, args):
                prompts.append(prompt)
                if len(prompts) == 1:
                    return {'translations': {'0': '第一の段落。', '2': ''}}
                self.assertNotIn('First paragraph.', prompt)
                return {'translations': {'2': '第二の段落。'}}

            with patch.object(p, 'chat', side_effect=fake_chat):
                p.translate_file(book, 'ja', rel, SimpleNamespace())
                p.translate_file(book, 'ja', rel, SimpleNamespace())
            self.assertEqual(len(prompts), 2)
            result = p.read(p.result_path(book, 'ja', rel))
            self.assertEqual(set(result['accepted']), {'0', '2'})

    def test_source_mutation_blocks_queue(self):
        with TemporaryDirectory() as tmp, patch.object(p, 'ROOT', Path(tmp)):
            source = Path(tmp) / 'generated_course_notes/demo/content.tex'
            source.parent.mkdir(parents=True)
            source.write_text('changed')
            with self.assertRaisesRegex(RuntimeError, 'source changed'):
                p.verify_sources({'course': 'demo', 'source_files': {'content.tex': p.digest('original')}})

    def test_preamble_retains_custom_macros_and_localizes_labels(self):
        source = r'\usepackage[utf8]{inputenc}' + '\n' + r'\newcommand{\custom}[1]{#1}\newcommand{\lectureoverview}[1]{\paragraph{Overview.} #1}'
        result = p.translated_preamble(source, 'ja')
        self.assertNotIn('inputenc', result)
        self.assertIn(r'\newcommand{\custom}', result)
        self.assertIn('Noto Serif CJK JP', result)
        self.assertIn('概観。', result)


if __name__ == '__main__':
    unittest.main()
