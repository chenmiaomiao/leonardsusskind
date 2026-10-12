import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
from unittest.mock import patch
import polished_translation as p


class TranslationTests(unittest.TestCase):
    def setUp(self):
        p.PROVIDER_STOP.clear()

    def tearDown(self):
        p.PROVIDER_STOP.clear()

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

    def test_heading_prose_cannot_escape_closing_braces(self):
        source, frozen = p.protect(r'\section{The Common Value of \texorpdfstring{\(L^2\)}{L squared}}')
        a, b, c, d = p.TOKEN.findall(source)
        self.assertIsNone(p.validate(source, a + b + 'Lの二乗' + c + 'の共通値' + d, 'ja', frozen))
        self.assertEqual(p.validate(source, a + b + 'Lの二乗' + c + d + 'の共通値', 'ja', frozen),
                         'heading text escaped its title argument')
        self.assertEqual(p.validate(source, a + '@' + b + 'Lの二乗' + c + d, 'ja', frozen),
                         'stray placeholder character')

    def test_closing_token_migration_preserves_existing_tex_and_ids(self):
        old = [r'\section{', r'\texorpdfstring{\(L^2\)}{', '}}']
        masked = '@@T000000@@Value @@T000001@@L squared@@T000002@@'
        updated, frozen, expansion = p.split_closing_tokens(masked, old)
        self.assertEqual(p.restore(masked, old), p.restore(updated, frozen))
        self.assertEqual(frozen[:2], old[:2])
        self.assertEqual(expansion, {'@@T000002@@': '@@T000002@@@@T000003@@'})
        self.assertEqual(p.split_closing_tokens(updated, frozen), (updated, frozen, {}))

    def test_malformed_json_is_archived_and_retried_once(self):
        with TemporaryDirectory() as tmp:
            dest = Path(tmp) / 'reply.json'
            calls = []

            def completion(prompt, path, log, **kwargs):
                calls.append(prompt)
                path.write_text('{broken' if len(calls) == 1 else '{"translations": {"0": "text"}}')

            with patch.dict(p.sys.modules, {'llm_chat_backend': SimpleNamespace(run_chat_completion=completion)}):
                result = p.chat('Translate', dest, SimpleNamespace(toolkit_root=Path(tmp), model='fixture'))
            self.assertEqual(len(calls), 2)
            self.assertEqual(result, {'translations': {'0': 'text'}})
            self.assertEqual(len(list(Path(tmp).glob('*.invalid-json'))), 1)

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
        self.assertIsNone(p.validate('the first row and the second column', '第1行と第2列', 'ja'))
        self.assertIsNone(p.validate('a single trial and a quarter turn', '1回の試行と4分の1回転', 'ja'))
        self.assertIsNotNone(p.validate('a quarter turn', '3分の1回転', 'ja'))
        self.assertIsNone(p.validate('a penny and a dime', '1セント硬貨と10セント硬貨', 'ja'))
        self.assertIsNotNone(p.validate('a penny and a dime', '5セント硬貨と10セント硬貨', 'ja'))
        self.assertIsNone(p.validate('differentiate once', '1回微分する', 'ja'))
        self.assertIsNone(p.validate('Nineteenth-century physics', '19世紀の物理学', 'ja'))
        self.assertIsNone(p.validate('the two-thirds law', '3分の2の法則', 'ja'))
        self.assertIsNotNone(p.validate('the two-thirds law', '3分の1の法則', 'ja'))
        self.assertIsNotNone(p.validate('a year of time', '時間の2年', 'ja'))

    def test_reference_glue_and_accented_names_can_move_with_prose(self):
        source, frozen = p.protect(r'Now set \(y=x\) in Eq.~\eqref{test}.')
        tokens = p.TOKEN.findall(source)
        self.assertIsNone(p.validate(source, '式' + tokens[1] + 'において' + tokens[0] + 'と置く。', 'ja', frozen))
        self.assertTrue(p.movable_token(r'Schr\"odinger'))

    def test_large_number_units_preserve_values_not_writing_system(self):
        self.assertIsNone(p.validate('ten to twelve billion years; the size doubles', '100億年から120億年で2倍', 'ja'))
        self.assertIsNone(p.validate('a thousand times longer', '1000倍長い', 'ja'))
        self.assertIsNone(p.validate('a million years', '100万年', 'ja'))
        self.assertIsNone(p.validate('two billion years', '20亿年', 'zh'))
        self.assertIsNotNone(p.validate('ten to twelve billion years', '10億年から12億年', 'ja'))
        self.assertIsNotNone(p.validate('a thousand times longer', '100倍長い', 'ja'))
        self.assertIsNone(p.validate('doubles in size, acquiring a doubled wavelength', '大きさが2倍、波長も2倍', 'ja'))
        self.assertIsNone(p.validate('a one-kilogram object', '一个1千克的物体', 'zh'))
        self.assertIsNone(p.validate('two kilowatts', '2千瓦', 'zh'))
        self.assertIsNone(p.validate('three thousand years', '3千年', 'zh'))

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

    def test_failed_segments_use_bounded_reasoning_repair_and_preserve_success(self):
        with TemporaryDirectory() as tmp, patch.object(p, 'WORK', Path(tmp)):
            book = {'id': 'fixture', 'titles': {'en': 'Physics', 'ja': '物理'}}
            rel = 'chapter.tex'
            prepared = {'source_sha256': 'test', 'parts': ['A year of time.', '\n\n', 'A simple statement.'], 'protected': []}
            p.write(p.WORK / 'prepared/fixture' / (rel + '.json'), prepared)
            calls = []

            def reply(prompt, dest, args, **kwargs):
                calls.append(kwargs.get('model', 'writer'))
                if len(calls) == 1:
                    return {'translations': {'0': '時間の2年。', '2': '単純な文。'}}
                self.assertNotIn('A simple statement.', prompt)
                return {'translations': {'0': '時間の2年。' if len(calls) == 2 else '年という時間。'}}

            with patch.object(p, 'chat', side_effect=reply):
                p.translate_file(book, 'ja', rel, SimpleNamespace())
                p.translate_file(book, 'ja', rel, SimpleNamespace())
            self.assertEqual(calls, ['writer', 'writer', 'deepseek-reasoner'])
            result = p.read(p.result_path(book, 'ja', rel))
            self.assertEqual(result['accepted'], {'0': '年という時間。', '2': '単純な文。'})
            self.assertIn('0', result['review_ids'])

    def test_persistent_budget_prevents_resume_retry_amplification(self):
        with TemporaryDirectory() as tmp, patch.object(p, 'WORK', Path(tmp)):
            book = {'id': 'fixture', 'titles': {'en': 'Physics', 'ja': '物理'}}
            rel = 'chapter.tex'
            p.write(p.WORK / 'prepared/fixture' / (rel + '.json'), {
                'source_sha256': 'test', 'parts': ['A field.'], 'protected': []})
            with patch.object(p, 'chat', return_value={'translations': {'0': '場999'}}) as chat:
                for _ in range(3):
                    with self.assertRaisesRegex(RuntimeError, 'Needs segment repair'):
                        p.translate_file(book, 'ja', rel, SimpleNamespace())
                self.assertEqual(chat.call_count, 4)

    def test_interrupted_completed_response_is_recovered_without_new_call(self):
        with TemporaryDirectory() as tmp, patch.object(p, 'WORK', Path(tmp)):
            book = {'id': 'fixture', 'titles': {'en': 'Physics', 'ja': '物理'}}
            rel = 'chapter.tex'
            p.write(p.WORK / 'prepared/fixture' / (rel + '.json'), {
                'source_sha256': 'test', 'parts': ['A field.'], 'protected': []})
            response = Path(tmp) / 'response.json'
            p.write(response, {'translations': {'0': 'ある場。'}})
            p.write(p.result_path(book, 'ja', rel), {'source_sha256': 'test', 'accepted': {},
                'inflight': {'path': str(response), 'ids': ['0'], 'stage': 'writer', 'source_sha256': 'test'}})
            with patch.object(p, 'chat') as chat:
                p.translate_file(book, 'ja', rel, SimpleNamespace())
                chat.assert_not_called()
            self.assertEqual(p.read(p.result_path(book, 'ja', rel))['accepted'], {'0': 'ある場。'})

    def test_provider_failure_stops_calls_and_refunds_content_attempt(self):
        with TemporaryDirectory() as tmp, patch.object(p, 'WORK', Path(tmp)):
            book = {'id': 'fixture', 'titles': {'en': 'Physics', 'ja': '物理'}}
            prepared = {'source_sha256': 'test', 'parts': ['A field.'], 'protected': []}
            result = {'source_sha256': 'test', 'accepted': {}}
            with patch.object(p, 'chat', side_effect=p.ProviderUnavailable('balance')):
                with self.assertRaises(p.ProviderUnavailable):
                    p.request_segments(book, 'ja', 'chapter.tex', prepared, result,
                                       {'0': 'A field.'}, SimpleNamespace(), 'writer', {}, 'prompt')
            self.assertEqual(result['attempts']['0']['writer'], 0)
            self.assertNotIn('inflight', result)
            args = SimpleNamespace(toolkit_root=Path(tmp), model='fixture')
            with patch.dict(p.sys.modules, {'llm_chat_backend': SimpleNamespace(
                    run_chat_completion=lambda *a, **k: (_ for _ in ()).throw(RuntimeError('402')))}):
                with self.assertRaises(p.ProviderUnavailable):
                    p.chat('prompt', Path(tmp) / 'reply.json', args)
                self.assertTrue(p.PROVIDER_STOP.is_set())

    def test_one_blocked_language_does_not_prevent_other_finalization(self):
        with TemporaryDirectory() as tmp, patch.object(p, 'WORK', Path(tmp)):
            book = {'id': 'fixture', 'source_files': {'chapter.tex': 'sha'}}
            args = SimpleNamespace(workers=1, ramp_seconds=0)
            with patch.object(p, 'translate_file', side_effect=[RuntimeError('bad ja'), None]), \
                 patch.object(p, 'update_readmes'), patch.object(p, 'validated_output', return_value=False), \
                 patch.object(p, 'language_complete', side_effect=[False, True]), \
                 patch.object(p, 'compile_book') as compile_book:
                errors = p.run_book(book, args)
            self.assertEqual(len(errors), 1)
            compile_book.assert_called_once_with(book, 'zh', args)

    def test_semantic_repair_retains_original_until_candidate_validates(self):
        with TemporaryDirectory() as tmp, patch.object(p, 'WORK', Path(tmp) / 'work'), \
             patch.object(p, 'OUT', Path(tmp) / 'out'):
            book = {'id': 'fixture', 'titles': {'en': 'Physics'}, 'source_files': {'chapter.tex': 'sha'}}
            source, frozen = p.protect(r'The charge is \(q\).')
            token = p.TOKEN.findall(source)[0]
            old = '電荷は' + token + '。'
            p.write(p.WORK / 'prepared/fixture/chapter.tex.json', {
                'source_sha256': 'sha', 'parts': [source], 'protected': frozen})
            p.write(p.result_path(book, 'ja', 'chapter.tex'), {'source_sha256': 'sha', 'accepted': {'0': old}})
            report = {'issues': [{'chapter': 'chapter.tex', 'segment_id': '0', 'reason': 'Fixture only'}]}
            with patch.object(p, 'chat', return_value={'translations': {'0': '電荷の説明。'}}):
                self.assertTrue(p.repair_review(book, 'ja', report, SimpleNamespace()))
            self.assertEqual(p.read(p.result_path(book, 'ja', 'chapter.tex'))['accepted']['0'], old)
            with patch.object(p, 'chat', return_value={'translations': {'0': '電荷は' + token + 'である。'}}):
                self.assertTrue(p.repair_review(book, 'ja', report, SimpleNamespace()))
            result = p.read(p.result_path(book, 'ja', 'chapter.tex'))
            self.assertEqual(result['superseded']['0'], [old])
            self.assertEqual(result['review_ids'], ['0'])
            self.assertEqual(p.read(p.OUT / 'fixture/ja/quality.json')['status'], 'needs_rebuild')
            with patch.object(p, 'chat') as chat:
                self.assertFalse(p.repair_review(book, 'ja', report, SimpleNamespace()))
                chat.assert_not_called()

    def test_failed_batch_does_not_abandon_remaining_chapter(self):
        with TemporaryDirectory() as tmp, patch.object(p, 'WORK', Path(tmp)):
            book = {'id': 'fixture', 'titles': {'en': 'Physics', 'ja': '物理'}}
            p.write(p.WORK / 'prepared/fixture/chapter.tex.json', {
                'source_sha256': 'sha', 'parts': ['First paragraph. ' * 300, '\n\n', 'Second paragraph.'], 'protected': []})

            def reply(prompt, *args, **kwargs):
                return {'translations': {'2': '第二の段落。'}} if 'Second paragraph.' in prompt else {'translations': {}}

            with patch.object(p, 'chat', side_effect=reply):
                with self.assertRaisesRegex(RuntimeError, 'Needs segment repair'):
                    p.translate_file(book, 'ja', 'chapter.tex', SimpleNamespace())
            self.assertEqual(p.read(p.result_path(book, 'ja', 'chapter.tex'))['accepted'], {'2': '第二の段落。'})

    def test_blocked_book_does_not_stop_later_books(self):
        with TemporaryDirectory() as tmp, patch.object(p, 'WORK', Path(tmp)), \
             patch.object(p, 'MANIFEST', Path(tmp) / 'manifest.json'):
            books = [{'id': 'first'}, {'id': 'second'}]
            p.write(p.MANIFEST, {'books': books})
            p.write(p.WORK / 'pilot-approved.json', {})
            args = SimpleNamespace(pilot_only=False, workers=5, publish=False)
            complete = set()

            def process(book, args):
                if book['id'] == 'second':
                    complete.add('second')
                    return []
                return [{'stage': 'translation', 'error': 'bad paragraph'}]

            with patch.object(p, 'verify_sources'), patch.object(p, 'update_readmes'), \
                 patch.object(p, 'validated_output', side_effect=lambda b, l: b['id'] in complete), \
                 patch.object(p, 'run_book', side_effect=process) as runner:
                p.run(args)
            self.assertEqual(runner.call_count, 2)
            self.assertEqual(p.read(p.WORK / 'status.json')['blocked_books'], ['first'])
            self.assertEqual(p.read(p.WORK / 'book-state/second.json')['state'], 'complete')

    def test_transport_recovery_waits_only_for_transient_failures(self):
        with TemporaryDirectory() as tmp, patch.object(p, 'WORK', Path(tmp)):
            p.write(p.WORK / 'status.json', {'state': 'provider_blocked'})
            args = SimpleNamespace(transport_resumes=2, transport_retry_seconds=0)
            with patch.object(p, 'run', side_effect=[p.ProviderUnavailable('status=429'), None]) as run:
                p.run_with_transport_recovery(args)
                self.assertEqual(run.call_count, 2)
            with patch.object(p, 'run', side_effect=p.ProviderUnavailable('status=402')) as run:
                with self.assertRaises(p.ProviderUnavailable):
                    p.run_with_transport_recovery(args)
                self.assertEqual(run.call_count, 1)
            with patch.object(p, 'run', side_effect=p.ProviderUnavailable('APIConnectionError')) as run:
                with self.assertRaises(p.ProviderUnavailable):
                    p.run_with_transport_recovery(args)
                self.assertEqual(run.call_count, 3)

    def test_transport_wait_honors_stop_marker(self):
        with TemporaryDirectory() as tmp, patch.object(p, 'WORK', Path(tmp)):
            p.write(p.WORK / 'status.json', {'state': 'provider_blocked'})
            (p.WORK / 'STOP').touch()
            with patch.object(p, 'run', side_effect=p.ProviderUnavailable('status=503')), patch.object(p.time, 'sleep') as sleep:
                p.run_with_transport_recovery(SimpleNamespace(transport_resumes=2, transport_retry_seconds=300))
                sleep.assert_not_called()
            self.assertEqual(p.read(p.WORK / 'status.json')['state'], 'paused')

    def test_preamble_retains_custom_macros_and_localizes_labels(self):
        source = r'\usepackage[utf8]{inputenc}' + '\n' + r'\newcommand{\custom}[1]{#1}\newcommand{\lectureoverview}[1]{\paragraph{Overview.} #1}'
        result = p.translated_preamble(source, 'ja')
        self.assertNotIn('inputenc', result)
        self.assertIn(r'\newcommand{\custom}', result)
        self.assertIn('Noto Serif CJK JP', result)
        self.assertIn('概観。', result)


if __name__ == '__main__':
    unittest.main()
