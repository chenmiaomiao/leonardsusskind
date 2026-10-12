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
        self.assertEqual(p.validate('position', '位�置', 'zh'), 'corrupt Unicode/control character')

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
        self.assertIsNone(p.validate('Spin-One-Half', 'スピン1/2', 'ja'))

    def test_teen_compound_and_unity_are_not_invented_numbers(self):
        self.assertIsNone(p.validate('eight and eighteen elements', '8個と18個の元素', 'ja'))
        self.assertIsNone(p.validate('exactly thirty-seven particles', 'ちょうど37個の粒子', 'ja'))
        self.assertIsNotNone(p.validate('exactly thirty-seven particles', 'ちょうど38個の粒子', 'ja'))
        self.assertIsNotNone(p.validate('exactly thirty-seven particles', '30個と7個の粒子', 'ja'))
        self.assertIsNone(p.validate('eigenvalues of unit magnitude', '固有値の絶対値は1', 'ja'))
        self.assertIsNone(p.validate('their commutator is unity', '它们的对易子为1', 'zh'))
        self.assertIsNotNone(p.validate('a unit of energy', '能量为1', 'zh'))

    def test_reference_glue_and_accented_names_can_move_with_prose(self):
        source, frozen = p.protect(r'Now set \(y=x\) in Eq.~\eqref{test}.')
        tokens = p.TOKEN.findall(source)
        self.assertIsNone(p.validate(source, '式' + tokens[1] + 'において' + tokens[0] + 'と置く。', 'ja', frozen))
        self.assertTrue(p.movable_token(r'Schr\"odinger'))

    def test_inline_math_can_pass_around_but_not_enter_emphasis(self):
        source, frozen = p.protect(r'The integer \(n_i\) is the \emph{occupation number} of oscillator \(i\).')
        a, opening, closing, b = p.TOKEN.findall(source)
        valid = '整数' + a + '是第' + b + '个振子的' + opening + '占据数' + closing + '。'
        invalid = '整数' + a + '是' + opening + '第' + b + '个占据数' + closing + '。'
        self.assertIsNone(p.validate(source, valid, 'zh', frozen))
        self.assertIsNotNone(p.validate(source, invalid, 'zh', frozen))

    def test_repeated_equation_token_is_still_rejected(self):
        source, frozen = p.protect(r'Both \(x\) and \(y\) commute with \(H\).')
        a, b, h = p.TOKEN.findall(source)
        self.assertIsNotNone(p.validate(source, a + '与' + h + '对易，' + b + '也与' + h + '对易。', 'zh', frozen))

    def test_unknown_nested_structure_does_not_open_a_math_escape(self):
        frozen = [r'\emph{', r'\footnote{', '$x$', '}', '}']
        source = '@@T000000@@A@@T000001@@B@@T000002@@@@T000003@@@@T000004@@'
        escaped = '@@T000000@@A@@T000001@@B@@T000003@@@@T000004@@@@T000002@@'
        self.assertFalse(p.token_integrity(source, escaped, frozen))

    def test_source_bound_repair_validates_whole_packet_before_writing(self):
        with TemporaryDirectory() as tmp, patch.object(p, 'WORK', Path(tmp) / 'work'), patch.object(p, 'MANIFEST', Path(tmp) / 'manifest.json'):
            book = {'id': 'fixture', 'source_files': {'chapter.tex': 'sha'}}
            p.write(p.MANIFEST, {'books': [book]})
            p.write(p.WORK / 'prepared/fixture/chapter.tex.json', {
                'source_sha256': 'sha', 'parts': ['eighteen states'], 'protected': []})
            packet = Path(tmp) / 'repairs.json'
            row = {'lang': 'ja', 'file': 'chapter.tex', 'segment_id': '0', 'source_sha256': 'sha',
                   'source': 'eighteen states', 'translation': '18個の状態', 'reason': 'Number-word check'}
            p.write(packet, {'book': 'fixture', 'repairs': [row, {**row, 'source': 'stale'}]})
            with patch.object(p, 'verify_sources'):
                with self.assertRaisesRegex(ValueError, 'Stale repair source'):
                    p.apply_reviewed_repairs(packet)
                self.assertFalse(p.result_path(book, 'ja', 'chapter.tex').exists())
                p.write(packet, {'book': 'fixture', 'repairs': [row]})
                p.apply_reviewed_repairs(packet)
                result = p.read(p.result_path(book, 'ja', 'chapter.tex'))
                self.assertEqual(result['accepted'], {'0': '18個の状態'})
                self.assertEqual(result['review_ids'], ['0'])
                p.write(packet, {'book': 'fixture', 'repairs': [{**row, 'translation': '18の状態'}]})
                with self.assertRaisesRegex(ValueError, 'Existing translation changed'):
                    p.apply_reviewed_repairs(packet)
                result['accepted']['0'] = '18個の状�態'
                p.write(p.result_path(book, 'ja', 'chapter.tex'), result)
                p.write(packet, {'book': 'fixture', 'repairs': [{
                    **row, 'previous_sha256': p.digest(result['accepted']['0'])}]})
                p.apply_reviewed_repairs(packet)

    def test_review_adjudication_is_bound_to_exact_sample_and_issue(self):
        with TemporaryDirectory() as tmp, patch.object(p, 'WORK', Path(tmp)):
            book = {'id': 'fixture'}
            issue = {'source_quote': 'roughly one percent', 'translation_quote': 'およそ1パーセント',
                     'correction': '0.7パーセント'}
            report = {'pass': False, 'issues': [issue], 'sample_sha256': 'current'}
            path = p.WORK / 'review-decisions/fixture/ja.current.json'
            p.write(path, {'sample_sha256': 'current', 'decisions': [{
                'issue_sha256': p.digest(p.json.dumps(issue, ensure_ascii=False, sort_keys=True)),
                'decision': 'dismiss', 'reason': 'The translation preserves the source approximation.'}]})
            effective = p.adjudicated_review(book, 'ja', report)
            self.assertTrue(effective['pass'])
            self.assertEqual(effective['raw_issues'], [issue])
            self.assertFalse(p.adjudicated_review(book, 'ja', {**report, 'sample_sha256': 'changed'})['pass'])
            with self.assertRaisesRegex(ValueError, 'stale review decision'):
                p.adjudicated_review(book, 'ja', {**report, 'issues': [{'other': 'issue'}]})

    def test_inline_math_can_move_but_not_across_structural_boundaries(self):
        source = '@@T000000@@One @@T000001@@ two @@T000002@@@@T000003@@'
        protected = [r'\section{', '$x$', '$y$', '}']
        good = '@@T000000@@日本語@@T000002@@、@@T000001@@@@T000003@@'
        bad = '@@T000000@@日本語@@T000002@@@@T000003@@@@T000001@@'
        self.assertIsNone(p.validate(source, good, 'ja', protected))
        self.assertIsNotNone(p.validate(source, bad, 'ja', protected))

    def test_display_math_must_not_move(self):
        source = '@@T000000@@A@@T000001@@'
        self.assertFalse(p.token_integrity(source, '@@T000001@@A@@T000000@@',
                                          [r'\begin{equation}x\end{equation}', r'\begin{equation}y\end{equation}']))
        self.assertTrue(p.token_integrity(source, '@@T000001@@A@@T000000@@',
                                         [r'\begin{equation}x\end{equation}', '$y$']))

    def test_accented_name_is_atomic(self):
        source = r'Fran\c{c}ois Englert found it.'
        masked, frozen = p.protect(source)
        self.assertNotIn('Fran', masked)
        self.assertEqual(frozen[0], r'Fran\c{c}ois')
        self.assertEqual(p.restore(masked, frozen), source)
        masked, frozen = p.protect(r'Schr\"odinger equation')
        self.assertNotIn('Schr', masked)
        self.assertEqual(frozen[0], r'Schr\"odinger')

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
