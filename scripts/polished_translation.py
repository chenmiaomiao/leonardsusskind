#!/usr/bin/env python3
"""Translate accepted lecture TeX without giving the model control of TeX syntax."""
from __future__ import annotations

import argparse
from contextlib import ExitStack
from fractions import Fraction
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import Counter
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import threading
import time

from pylatexenc import latexwalker as lw
from pylatexenc.macrospec import MacroSpec, EnvironmentSpec

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / '.translation-work'
OUT = ROOT / 'translations'
MANIFEST = ROOT / 'references/polished_translation_queue.json'
VERSION = 1
TOKEN = re.compile(r'@@T\d{6}@@')
LANGS = {'ja': 'modern Japanese', 'zh': 'modern Simplified Chinese'}
NUMBER_WORDS = dict(zip(
    'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split(),
    map(str, range(20))))
for _tens, _value in zip('twenty thirty forty fifty sixty seventy eighty ninety'.split(), range(20, 100, 10)):
    NUMBER_WORDS[_tens] = str(_value)
    for _ones, _number in list(NUMBER_WORDS.items())[:10]:
        if _number != '0':
            NUMBER_WORDS[_tens + '-' + _ones] = str(_value + int(_number))
            NUMBER_WORDS[_tens + ' ' + _ones] = str(_value + int(_number))
NUMBER_WORD_PATTERN = re.compile(r'\b(?:' + '|'.join(
    re.escape(w) for w in sorted(NUMBER_WORDS, key=len, reverse=True)) + r')\b')
TEXT_MACROS = {
    'chapter': '*[{', 'section': '*[{', 'subsection': '*[{',
    'subsubsection': '*[{', 'paragraph': '*[{', 'caption': '[{',
    'textbf': '{', 'textit': '{', 'emph': '{', 'texttt': '{',
    'lectureoverview': '{', 'audiencequestion': '{', 'lecturerresponse': '{',
    'editorialnote': '{', 'classquestion': '{', 'footnote': '[{',
    'texorpdfstring': '{{', 'href': '{{',
}
FROZEN_MACROS = {
    'input': '{', 'includegraphics': '*[{', 'graphicspath': '{',
    'lecturetimestamp': '{', 'lectureframe': '{', 'label': '{',
    'ref': '{', 'eqref': '{', 'pageref': '{', 'cite': '[{',
    'url': '{', 'nolinkurl': '{', 'detokenize': '{',
    'vspace': '*{', 'hspace': '*{', 'enlargethispage': '{',
    'setlength': '{{', 'providecommand': '*{[[{', 'hypersetup': '{',
    'documentclass': '[{', 'thispagestyle': '{', 'c': '{',
}
MATH_ENVS = {'equation', 'align', 'alignat', 'gather', 'multline', 'displaymath',
             'math', 'eqnarray', 'flalign', 'tikzpicture', 'picture', 'verbatim'}
TITLES = {
 'higgs_boson': ('Demystifying the Higgs Boson', 'ヒッグス粒子を解き明かす', '解密希格斯玻色子'),
 'advanced_quantum_mechanics': ('Advanced Quantum Mechanics', '量子力学特論', '高等量子力学'),
 'quantum_entanglement': ('Quantum Entanglement', '量子もつれ', '量子纠缠'),
 'particle_physics_1_basic_concepts': ('Particle Physics 1: Basic Concepts', '素粒子物理学1：基礎概念', '粒子物理学1：基本概念'),
 'particle_physics_2_standard_model': ('Particle Physics 2: Standard Model', '素粒子物理学2：標準模型', '粒子物理学2：标准模型'),
 'particle_physics_3_supersymmetry_and_grand_unification': ('Particle Physics 3: Supersymmetry and Grand Unification', '素粒子物理学3：超対称性と大統一', '粒子物理学3：超对称性与大统一'),
 'cosmology_and_black_holes': ('Topics in String Theory', '弦理論の諸問題', '弦理论专题'),
 'string_theory': ('String Theory and M-Theory', '弦理論とM理論', '弦理论与M理论'),
 'classical_mechanics': ('Classical Mechanics', '古典力学', '经典力学'),
 'quantum_mechanics': ('Quantum Mechanics', '量子力学', '量子力学'),
 'special_relativity': ('Special Relativity', '特殊相対性理論', '狭义相对论'),
 'general_relativity': ('General Relativity', '一般相対性理論', '广义相对论'),
 'statistical_mechanics': ('Statistical Mechanics', '統計力学', '统计力学'),
 'cosmology': ('Cosmology', '宇宙論', '宇宙学'),
}


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + f'.{threading.get_ident()}.tmp')
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
    tmp.replace(path)


def textwrite(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8')


def protect(tex):
    """Use AST text spans; everything else is immutable, including math and paths."""
    context = lw.get_default_latex_context_db()
    context.add_context_category('lecture', prepend=True,
        macros=[MacroSpec(k, v) for k, v in {**TEXT_MACROS, **FROZEN_MACROS,
            'resizebox': '*{{{', 'scalebox': '{[{', 'item': '['}.items()],
        environments=[EnvironmentSpec('classroomqa', ''),
                      EnvironmentSpec('figure', '['), EnvironmentSpec('table', '[')])
    nodes, _, length = lw.LatexWalker(tex, latex_context=context,
                                    tolerant_parsing=False).get_latex_nodes()
    if length != len(tex):
        raise ValueError('Incomplete TeX parse')
    spans = []

    def visit(node):
        if isinstance(node, lw.LatexCharsNode):
            spans.append((node.pos, node.pos + node.len))
        elif isinstance(node, lw.LatexGroupNode):
            for child in node.nodelist:
                visit(child)
        elif isinstance(node, lw.LatexEnvironmentNode):
            if node.environmentname.rstrip('*') not in MATH_ENVS:
                for child in node.nodelist:
                    visit(child)
        elif isinstance(node, lw.LatexMacroNode):
            args = node.nodeargd.argnlist if node.nodeargd else []
            if node.macroname in TEXT_MACROS:
                for index, arg in enumerate(args):
                    if arg is not None and not (node.macroname == 'href' and index == 0):
                        visit(arg)
            elif node.macroname in {'resizebox', 'scalebox'} and args[-1]:
                visit(args[-1])
            elif node.macroname == 'item' and args and args[0]:
                visit(args[0])

    for node in nodes:
        visit(node)
    # Preserve the whole accented name, not a command in the middle of a word.
    accents = [(m.start(), m.end()) for m in re.finditer(r"[A-Za-z]+\\(?:c|v|H|u|k|'|`|\^|\"|~)(?:\{[A-Za-z]\}|[A-Za-z])[A-Za-z]*", tex)]
    for left, right in accents:
        spans = [(a, b) for start, end in spans
                 for a, b in [(start, min(end, left)), (max(start, right), end)] if a < b]
    spans.sort()
    protected = []

    def freeze(value):
        if not value:
            return ''
        token = f'@@T{len(protected):06d}@@'
        protected.append(value)
        return token

    cursor = 0
    pieces = []
    for start, end in spans:
        if start < cursor:
            raise ValueError('Overlapping AST spans')
        pieces.append(freeze(tex[cursor:start]))
        # Preserve numbers and TeX-special characters outside math as well.
        pieces.append(re.sub(r'\d+(?:[.,]\d+)*|[{}\\%$&#_^~]',
                             lambda m: freeze(m.group()), tex[start:end]))
        cursor = end
    pieces.append(freeze(tex[cursor:]))
    masked = ''.join(pieces)
    if restore(masked, protected) != tex:
        raise ValueError('TeX masking is not lossless')
    return masked, protected


def restore(masked, protected):
    return TOKEN.sub(lambda m: protected[int(m.group()[3:9])], masked)


def segments(masked):
    return re.split(r'(\n\s*\n)', masked)


def needs_translation(text):
    return bool(re.search(r'[A-Za-z]{2}', TOKEN.sub('', text)))


def movable_token(value):
    value = value.strip()
    return bool(re.fullmatch(
        r'\d+(?:[.,]\d+)*|\$(?:[^$]|\\\$)+\$|\\\(.*\\\)|~?\\(?:eqref|ref|pageref)\{[^{}]*\}'
        r'|[A-Za-z]+\\(?:c|v|H|u|k|\x27|`|\^|"|~)(?:\{[A-Za-z]\}|[A-Za-z])[A-Za-z]*', value, re.S))


def token_integrity(source, translated, protected):
    before, after = TOKEN.findall(source), TOKEN.findall(translated)
    if Counter(before) != Counter(after):
        return False
    if protected is None:
        return before == after
    movable = {token for token in before if movable_token(protected[int(token[3:9])])}
    if [t for t in before if t not in movable] != [t for t in after if t not in movable]:
        return False
    displays = {token for token in before if re.fullmatch(
        r'\\\[.*\\\]|\\begin\{(?:equation\*?|align\*?|gather\*?|multline\*?)\}.*\\end\{[^{}]+\}',
        protected[int(token[3:9])].strip(), re.S)}

    def zones(sequence):
        result, anchor = {}, None
        styles = []
        for token in sequence:
            if token in movable:
                result[token] = anchor
            elif token not in displays:
                value = protected[int(token[3:9])].strip()
                # A complete inline style is an island, not a new prose block.
                # Math can pass around it, but cannot enter or leave its braces.
                if re.fullmatch(r'\\(?:emph|textbf|textit|texttt)\{', value):
                    styles.append(anchor)
                    anchor = token
                elif value == '}' and styles:
                    anchor = styles.pop()
                else:
                    # Unknown nested constructs remain conservative boundaries.
                    styles.clear()
                    anchor = token
        return result
    return zones(before) == zones(after)


def validate(source, translated, lang, protected=None):
    if not isinstance(translated, str) or not translated.strip():
        return 'empty translation'
    if re.search(r'[\ufffd\ud800-\udfff\x00-\x08\x0b\x0c\x0e-\x1f]', translated):
        return 'corrupt Unicode/control character'
    if not token_integrity(source, translated, protected):
        return 'protected token order/coverage changed'
    prose = TOKEN.sub('', translated)
    if re.search(r'[{}\\%$&#_^~]|```|@@T', prose):
        return 'new TeX/transport syntax'
    number_prose = TOKEN.sub('', source).lower()
    source_words = Counter()
    for phrase, number in {'one and a half': '1.5', 'two and a half': '2.5',
                           'one-half': '1/2', 'one half': '1/2', 'three quarters': '3/4',
                           'unit magnitude': '1', 'unit modulus': '1', 'unit norm': '1', 'unity': '1',
                           'half': '0.5', 'quarter': '0.25', 'twice': '2', 'thrice': '3'}.items():
        pattern = r'\b' + re.escape(phrase) + r'\b'
        source_words[number] += len(re.findall(pattern, number_prose))
        number_prose = re.sub(pattern, '', number_prose)
    source_words.update(NUMBER_WORDS[m.group()] for m in NUMBER_WORD_PATTERN.finditer(number_prose))
    normalized_source = Counter()
    for number, count in source_words.items():
        normalized_source[str(Fraction(number))] += count
    try:
        candidate_numbers = Counter(str(Fraction(n)) for n in re.findall(r'\d+(?:\.\d+)?(?:/\d+)?', prose))
    except ZeroDivisionError:
        return 'invalid numerical fraction'
    if candidate_numbers - normalized_source:
        return 'introduced unprotected number'
    if len(TOKEN.sub('', source).strip()) > 60 and not re.search(r'[\u3400-\u9fff\u3040-\u30ff]', prose):
        return 'untranslated prose'
    n = len(re.sub(r'\s', '', TOKEN.sub('', source)))
    size = len(re.sub(r'\s', '', prose))
    if n > 100 and not 0.12 * n <= size <= 2.8 * n:
        return 'suspicious translation length'
    return None


def prepare():
    queue = read(ROOT / 'references/editorial_revision_queue.json')['courses']
    queue = sorted(queue, key=lambda c: 'higgs_boson' not in c['course'])
    queue.append({'course': 'core/cosmology/2009_winter_legacy_cosmology', 'expected_chapters': 8})
    books = []
    prepared_files = []
    for entry in queue:
        course = entry['course']
        src = ROOT / 'generated_course_notes' / course
        main = (src / 'course.tex').read_text()
        paths = re.findall(r'\\input\{(chapters/[^{}]+/content\.tex)\}', main)
        if len(paths) != entry['expected_chapters']:
            raise ValueError(f'Chapter coverage mismatch: {course}')
        for rel in paths:
            fidelity = read(src / Path(rel).parent / 'editorial_fidelity.json')
            if fidelity.get('status') != 'pass':
                raise ValueError(f'Unaccepted source: {course}/{rel}')
        titles = TITLES[course.split('/')[1]]
        if 'part_' in course:
            part = course.rsplit('_', 1)[-1]
            titles = (titles[0] + ' Part ' + part, titles[1] + ' 第' + part + '部', titles[2] + ' 第' + part + '部')
        slug = course.replace('/', '--')
        files = ['course.tex', 'common_preamble.tex'] + paths
        hashes = {rel: digest((src / rel).read_text()) for rel in files}
        assets = sorted({p.resolve() for base in [src / 'figures', src / 'assets']
                         for p in base.rglob('*') if p.is_file()})
        # Content chunks never originate from draft.tex, PDFs, or older English runs.
        count = 0
        for rel in ['course.tex'] + paths:
            t = (src / rel).read_text()
            if rel == 'course.tex':
                t = re.sub(r'\\begin\{titlepage\}.*?\\end\{titlepage\}', r'\\input{cover.tex}', t, flags=re.S)
            masked, frozen = protect(t)
            parts = segments(masked)
            count += sum(needs_translation(x) for x in parts)
            payload = {'source_sha256': hashes[rel], 'parts': parts, 'protected': frozen}
            prepared_files.append((slug, rel, payload))
        books.append({'id': slug, 'course': course, 'titles': dict(zip(['en', 'ja', 'zh'], titles)),
                      'chapters': len(paths), 'source_files': hashes, 'translation_segments': count,
                      'figure_asset_count': len(assets), 'languages': ['ja', 'zh']})
    result = {'schema_version': VERSION, 'provider': 'deepseek', 'model': 'deepseek-chat',
              'workers': 5, 'scope': 'accepted final editorial TeX only', 'books': books}
    if MANIFEST.exists() and read(MANIFEST) != result:
        raise ValueError('Manifest changed: use a new translation edition rather than overwrite accepted work')
    for slug, rel, payload in prepared_files:
        path = WORK / 'prepared' / slug / (rel + '.json')
        if path.exists() and read(path) != payload:
            old = read(path)
            for lang in LANGS:
                cache = WORK / 'results' / slug / lang / (rel + '.json')
                if cache.exists():
                    data = read(cache)
                    write(cache.with_suffix(f'.{time.time_ns()}.bak'), data)
                    # A changed frozen name can keep numbering intact: validate each row's restored source.
                    previous = dict(data['accepted'])
                    data['accepted'] = {}
                    for k, v in previous.items():
                        i = int(k)
                        if i < len(payload['parts']) and old['parts'][i] == payload['parts'][i]:
                            if restore(old['parts'][i], old['protected']) == restore(payload['parts'][i], payload['protected']):
                                data['accepted'][k] = v
                    write(cache, data)
        write(path, payload)
    write(MANIFEST, result)
    print(f'Prepared {len(books)} books, {sum(x["chapters"] for x in books)} chapters, '
          f'{sum(x["translation_segments"] for x in books)} segments per language', flush=True)
    update_readmes()


def result_path(book, lang, rel):
    return WORK / 'results' / book['id'] / lang / (rel + '.json')


def load_results(book, lang, rel, prepared):
    p = result_path(book, lang, rel)
    result = read(p) if p.exists() else {'source_sha256': prepared['source_sha256'], 'accepted': {}}
    if result['source_sha256'] != prepared['source_sha256']:
        raise ValueError('Stale translation cache')
    for key, text in result['accepted'].items():
        issue = validate(prepared['parts'][int(key)], text, lang, prepared['protected'])
        if issue:
            raise ValueError(f'Invalid accepted cache: {key}: {issue}')
    return result


def apply_reviewed_repairs(path):
    """Import explicit, source-bound repairs without re-generating accepted prose."""
    packet = read(path)
    book = next(b for b in read(MANIFEST)['books'] if b['id'] == packet['book'])
    verify_sources(book)
    pending = {}
    for row in packet['repairs']:
        lang, rel, key = row['lang'], row['file'], str(row['segment_id'])
        if lang not in LANGS or rel not in book['source_files'] or not row.get('reason'):
            raise ValueError('Invalid repair scope or missing review reason')
        prepared = read(WORK / 'prepared' / book['id'] / (rel + '.json'))
        source = prepared['parts'][int(key)]
        if (row['source_sha256'] != prepared['source_sha256']
                or row['source'] != restore(source, prepared['protected'])):
            raise ValueError(f'Stale repair source: {rel}:{key}')
        issue = validate(source, row['translation'], lang, prepared['protected'])
        if issue:
            raise ValueError(f'Invalid repair: {rel}:{key}: {issue}')
        identity = (lang, rel)
        if identity not in pending:
            dest = result_path(book, lang, rel)
            pending[identity] = read(dest) if dest.exists() else {
                'source_sha256': prepared['source_sha256'], 'accepted': {}}
            if pending[identity]['source_sha256'] != prepared['source_sha256']:
                raise ValueError('Stale translation cache')
        result = pending[identity]
        previous = result['accepted'].get(key)
        if previous is not None and previous != row['translation']:
            if row.get('previous_sha256') != digest(previous):
                raise ValueError(f'Existing translation changed: {rel}:{key}')
        result['accepted'][key] = row['translation']
        result['review_ids'] = sorted(set(result.get('review_ids', []) + [key]), key=int)
        result.setdefault('repairs', {})[key] = {
            'reason': row['reason'], 'packet_sha256': digest(path.read_text()),
            'translation_sha256': digest(row['translation'])}
    # Validate the whole packet before changing any cache file.
    for (lang, rel), result in pending.items():
        prepared = read(WORK / 'prepared' / book['id'] / (rel + '.json'))
        for key, text in result['accepted'].items():
            issue = validate(prepared['parts'][int(key)], text, lang, prepared['protected'])
            if issue:
                raise ValueError(f'Unresolved cached error: {rel}:{key}: {issue}')
    for (lang, rel), result in pending.items():
        dest = result_path(book, lang, rel)
        if dest.exists():
            shutil.copy2(dest, dest.with_suffix(f'.{time.time_ns()}.bak'))
        write(dest, result)
    print(f'Applied {len(packet["repairs"])} reviewed repairs', flush=True)


def chat(prompt, dest, args):
    sys.path.insert(0, str(args.toolkit_root / 'scripts/interlinear'))
    from llm_chat_backend import run_chat_completion
    run_chat_completion(prompt, dest, dest.with_suffix('.usage.jsonl'), provider='deepseek',
                        model=args.model, timeout_seconds=600, max_attempts=3)
    return read(dest)


def translate_file(book, lang, rel, args):
    p = read(WORK / 'prepared' / book['id'] / (rel + '.json'))
    result = load_results(book, lang, rel, p)
    todo = [(str(i), text) for i, text in enumerate(p['parts'])
            if needs_translation(text) and str(i) not in result['accepted']]
    batches, batch, size = [], [], 0
    for item in todo:
        if batch and size + len(item[1]) > 4800:
            batches.append(batch)
            batch, size = [], 0
        batch.append(item)
        size += len(item[1])
    if batch:
        batches.append(batch)
    for index, rows in enumerate(batches):
        pending = dict(rows)
        errors = {}
        for attempt in range(2):
            prompt = (
                f'Translate these final edited physics lecture paragraphs into fluent, precise {LANGS[lang]}. '
                'Translate faithfully, not summarize: preserve every qualification, negation, physical distinction, '
                'question and answer. Never add facts. Keep standard physics terminology consistent. '
                'Every @@T000000@@-style token is immutable TeX, math, a reference, or a number. '
                'Copy all tokens EXACTLY ONCE; do not translate their contents. Keep structural tokens in '
                'original order. Inline math, numeric and cross-reference tokens may change order ONLY '
                'within the same structural boundaries when required for natural target-language syntax. '
                'Use the read-only token legend to understand the physics and formatting. Even tokens '
                'representing quote marks, dashes or empty-looking braces MUST remain. For example '
                'left@@T000001@@right becomes 左@@T000001@@右, not 左右. '
                'Return JSON {"translations": {"id": "translated paragraph"}} with all supplied IDs only. '
                'No TeX commands, markdown, new numbers, or comments. Translate headings and introductory '
                'paragraphs just as carefully as body text. Proper names may remain Latin, but ordinary '
                'prose such as companion notes or Professor must be translated, not left in English. '
                f'Book: {book["titles"]["en"]}. Target title: {book["titles"][lang]}. '
                'Use Japanese scientific style (である調) or readable modern Chinese as appropriate. '
                'In Japanese use 標準模型 for Standard Model, 弱ゲージボソン for weak boson, '
                'カイラリティ for chirality; render year dates as 年に, not で. '
                'In Chinese retain the 年 year marker after a year token; never write 在YEAR中 for a date. '
                'Distinguish applying an operator from holding it constant; do not change the physical action.\n'
                'Use idiomatic scientific sentences around displayed equations rather than mechanically '
                'copying English word order. Introduce transformations as transformations, not literal sending. '
                'Frozen expressions cannot be repeated, even if repeating them would be natural: use a '
                'pronoun or restructure the sentence instead. English spelled-out numbers up to '
                'ninety-nine and unity may use equivalent Arabic numerals. Never add explanatory quantities. '
                + json.dumps({'paragraphs': pending, 'previous_errors': errors,
                    'read_only_token_legend': {token: p['protected'][int(token[3:9])]
                        for source in pending.values() for token in TOKEN.findall(source)}}, ensure_ascii=False))
            dest = WORK / 'calls' / book['id'] / lang / (rel + f'.{index}.{attempt}.{time.time_ns()}.json')
            reply = chat(prompt, dest, args)
            translations = reply.get('translations', {})
            if not isinstance(translations, dict):
                translations = {}
            errors = {}
            for key, source in list(pending.items()):
                translated = translations.get(key)
                issue = validate(source, translated, lang, p['protected'])
                if issue:
                    errors[key] = issue
                else:
                    result['accepted'][key] = translated
                    if attempt or TOKEN.findall(source) != TOKEN.findall(translated):
                        result['review_ids'] = sorted(set(result.get('review_ids', []) + [key]), key=int)
                    del pending[key]
            write(result_path(book, lang, rel), result)
            print(json.dumps({'book': book['id'], 'lang': lang, 'file': rel,
                              'accepted': len(result['accepted']), 'pending_batch': len(pending)}, ensure_ascii=False), flush=True)
            if not pending:
                break
        if pending:
            raise RuntimeError(f'Needs segment repair: {book["id"]}/{lang}/{rel}: {errors}')


def translated_preamble(source, lang):
    t = re.sub(r'\\usepackage(?:\[[^\]]*\])?\{(?:fontenc|inputenc|lmodern)\}\s*', '', source)
    family = 'JP' if lang == 'ja' else 'SC'
    prefix = (r'\usepackage{fontspec}' '\n' r'\usepackage{xeCJK}' '\n'
              r'\setmainfont{Latin Modern Roman}' '\n'
              f'\\setCJKmainfont[ItalicFont={{Noto Serif CJK {family}}},BoldItalicFont={{Noto Serif CJK {family} Bold}}]{{Noto Serif CJK {family}}}\n'
              f'\\setCJKsansfont{{Noto Sans CJK {family}}}\n'
              f'\\setCJKmonofont{{Noto Sans Mono CJK {family}}}\n')
    prefix += '\\newfontfamily\\proseunicodefont{DejaVu Serif}\n'
    labels = {
        'Theorem': ('定理', '定理'), 'Proposition': ('命題', '命题'),
        'Lemma': ('補題', '引理'), 'Corollary': ('系', '推论'),
        'Definition': ('定義', '定义'), 'Example': ('例', '例'), 'Remark': ('注意', '注'),
        'Overview.': ('概観。', '概述。'),
        'Question from the audience.': ('受講者からの質問。', '听众提问。'),
        'Question for the class.': ('受講者への問い。', '课堂提问。'),
        'Response.': ('回答。', '回答。'), 'Lecture timestamp:': ('講義時刻：', '讲课时间：'),
        'Lecture frame:': ('講義映像：', '讲课画面：'),
        'Editorial clarification:': ('編集上の補足：', '编者说明：'),
    }
    for english, versions in labels.items():
        t = t.replace(english, versions[0 if lang == 'ja' else 1])
    names = {'contentsname': ('目次', '目录'), 'chaptername': ('章', '章'),
             'figurename': ('図', '图'), 'tablename': ('表', '表'),
             'proofname': ('証明', '证明'), 'bibname': ('参考文献', '参考文献')}
    suffix = '\n' + '\n'.join(f'\\renewcommand{{\\{k}}}{{{v[0 if lang == "ja" else 1]}}}' for k, v in names.items())
    # CJK italics are not supplied by Noto. Keep readable upright CJK, Latin italic intact.
    return prefix + t + suffix + '\n\\emergencystretch=2em\n\\pdfstringdefDisableCommands{\\def\\proseunicodefont{}}\n'


def cover(book, lang):
    source = (ROOT / 'generated_course_notes' / book['course'] / 'course.tex').read_text()
    titlepage = re.search(r'\\begin\{titlepage\}.*?\\end\{titlepage\}', source, re.S).group()
    title = book['titles'][lang]
    titlepage = re.sub(r'(\\color\{black!\d+\} )[^}\n]+(?=\})',
        lambda m: m.group(1) + title + r'\\[0.85em]', titlepage, count=1)
    track = ('日本語版' if lang == 'ja' else '中文版') + ' / ' + book['course'].split('/')[-1].replace('_', ' ')
    titlepage = re.sub(r'(\\large\\color\{black!\d+\} )[^}\n]+', lambda m: m.group(1) + track, titlepage, count=1)
    lecturer = '原講義：Leonard Susskind' if lang == 'ja' else '原讲授：Leonard Susskind'
    titlepage = re.sub(r'(?:Original lectures?|Lectures) by Leonard Susskind', lecturer, titlepage)
    titlepage = titlepage.replace('Companion edition by ', '講義補助版：' if lang == 'ja' else '讲义辅助版本：')
    titlepage = titlepage.replace(' with ', ' / ')
    # Allow long CJK titles to wrap within the existing cover text area.
    return titlepage


def assemble(book, lang):
    src = ROOT / 'generated_course_notes' / book['course']
    dst = OUT / book['id'] / lang
    for rel, expected in book['source_files'].items():
        if digest((src / rel).read_text()) != expected:
            raise ValueError(f'English source changed: {rel}')
        if rel == 'common_preamble.tex':
            textwrite(dst / rel, translated_preamble((src / rel).read_text(), lang))
            continue
        p = read(WORK / 'prepared' / book['id'] / (rel + '.json'))
        result = load_results(book, lang, rel, p)
        translated = []
        for i, part in enumerate(p['parts']):
            if needs_translation(part):
                translated.append(result['accepted'][str(i)])
            else:
                translated.append(part)
        # Font substitution affects translated prose only, never frozen math.
        masked = re.sub(r'[\u0370-\u03ff]', lambda m: '{\\proseunicodefont ' + m.group() + '}', ''.join(translated))
        rendered = restore(masked, p['protected'])
        if rel == 'course.tex':
            def graphic_paths(match):
                paths = re.findall(r'\{([^{}]*)\}', match.group(1))
                return '\\graphicspath{' + ''.join('{' + os.path.relpath(src / path, dst) + '/}' for path in paths) + '}'
            rendered = re.sub(r'\\graphicspath\{((?:\{[^{}]*\})+)\}', graphic_paths, rendered)
        textwrite(dst / rel, rendered)
    titlepage = cover(book, lang).replace('{assets/', '{' + os.path.relpath(src / 'assets', dst) + '/')
    textwrite(dst / 'cover.tex', titlepage)
    return dst


def review_sample(book, lang, args):
    pairs = []
    for rel in book['source_files']:
        if not (rel.endswith('content.tex') or rel == 'course.tex'):
            continue
        p = read(WORK / 'prepared' / book['id'] / (rel + '.json'))
        result = load_results(book, lang, rel, p)
        accepted = result['accepted']
        eligible = [(k, t) for k, t in accepted.items() if len(TOKEN.sub('', p['parts'][int(k)])) > 200]
        # Fixed middle technical paragraph from every chapter, plus opening prose.
        selected = dict([eligible[0], eligible[len(eligible)//2]] if eligible else [])
        selected.update({key: accepted[key] for key in result.get('review_ids', []) if key in accepted})
        for key, t in selected.items():
            pairs.append({'chapter': rel, 'source': restore(p['parts'][int(key)], p['protected']),
                          'translation': restore(t, p['protected']), 'segment_id': key})
    report = WORK / 'reviews' / book['id'] / f'{lang}.json'
    sample_hash = digest(json.dumps(pairs, ensure_ascii=False))
    if report.exists() and read(report).get('sample_sha256') == sample_hash:
        return read(report)
    issues = []
    for start in range(0, len(pairs), 10):
        batch = pairs[start:start + 10]
        batch_path = report.with_name(lang + '.' + digest(json.dumps(batch, ensure_ascii=False))[:20] + '.batch.json')
        if batch_path.exists():
            reply = read(batch_path)
        else:
            reply = chat('Audit these source/translation pairs for material physics mistranslation, missing '
                 'qualifications or added claims. Ignore style preferences and preserved English math labels. '
                 'Return JSON {"pass": true/false, "issues": [{"chapter": "...", '
                 '"segment_id": "...", '
                 '"source_quote": "...", "translation_quote": "...", "correction": "...", "reason": "..."}]}. '
                 'For accurate pairs, do NOT create issue entries. A sentence saying there is no error '
                 'must never be listed as an issue. If all pairs are accurate, return pass=true and issues=[]. '
                 'This is sampled semantic review, not full-book review.\n' + json.dumps(batch, ensure_ascii=False),
                 batch_path, args)
        if reply.get('pass') is not True or reply.get('issues') != []:
            issues.extend(reply.get('issues') or [{'reason': 'Invalid reviewer response', 'batch': start}])
    report_data = {'pass': not issues, 'issues': issues, 'sample_sha256': sample_hash, 'pairs_reviewed': len(pairs)}
    write(report, report_data)
    return report_data


def compile_book(book, lang, args):
    import fitz
    write(OUT / book['id'] / lang / 'quality.json', {'status': 'building'})
    dst = assemble(book, lang)
    build = WORK / 'build' / book['id'] / lang
    build.mkdir(parents=True, exist_ok=True)
    for _ in range(3):
        run = subprocess.run(['xelatex', '-interaction=nonstopmode', '-halt-on-error', '-no-shell-escape',
                              f'-output-directory={build}', 'course.tex'], cwd=dst,
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=900)
        (build / 'compile-output.txt').write_bytes(run.stdout)
        if run.returncode:
            raise RuntimeError(f'XeLaTeX failed: {build}/compile-output.txt')
    log = (build / 'course.log').read_text(errors='replace')
    overflows = re.findall(r'Overfull \\[hv]box \(([^\n]+)', log)
    errors = [s for s in ['Missing character:', 'undefined references', 'multiply defined'] if s in log]
    with fitz.open(build / 'course.pdf') as pdf:
        text = ''.join(page.get_text() for page in pdf)
        qa = {'pages': len(pdf), 'outline_entries': len(pdf.get_toc()),
              'cjk_characters': len(re.findall(r'[\u3400-\u9fff\u3040-\u30ff]', text)),
              'image_placements': sum(len(page.get_images()) for page in pdf),
              'overflows': overflows, 'errors': errors}
    write(build / 'quality.json', qa)
    if errors or overflows or not qa['outline_entries'] or qa['cjk_characters'] < 100:
        raise RuntimeError(f'PDF quality gate needs repair: {build}/quality.json')
    review = review_sample(book, lang, args)
    if review.get('pass') is not True or review.get('issues') != []:
        raise RuntimeError(f'Sampled semantic review needs repair: {lang}')
    shutil.copy2(build / 'course.pdf', dst / 'book.pdf')
    qa.update({'status': 'validated', 'pdf_sha256': hashlib.sha256((dst / 'book.pdf').read_bytes()).hexdigest(),
               'semantic_review': 'sampled, not exhaustive', 'sample_pairs': review['pairs_reviewed'],
               'source_files': book['source_files'],
               'translated_tex': {str(p.relative_to(dst)): digest(p.read_text()) for p in dst.rglob('*.tex')}})
    write(dst / 'quality.json', qa)
    return qa


def status():
    rows = []
    for book in read(MANIFEST)['books']:
        row = {'book': book['id'], 'segments_per_language': book['translation_segments']}
        for lang in LANGS:
            files = list((WORK / 'results' / book['id'] / lang).glob('**/*.json'))
            row[lang] = sum(len(read(p).get('accepted', {})) for p in files)
            q = OUT / book['id'] / lang / 'quality.json'
            row[lang + '_pdf'] = 'validated' if validated_output(book, lang) else (read(q)['status'] if q.exists() and read(q)['status'] != 'validated' else 'not_available')
        rows.append(row)
    return rows


def update_readmes():
    if not MANIFEST.exists():
        return
    rows = status()
    table = ['| Final polished book | 日本語 | 中文 |', '| --- | --- | --- |']
    for book, st in zip(read(MANIFEST)['books'], rows):
        cells = []
        for lang in LANGS:
            if st[lang + '_pdf'] == 'validated':
                cells.append(f'[Available PDF](translations/{book["id"]}/{lang}/book.pdf)')
            else:
                cells.append(f'In preparation ({st[lang]}/{st["segments_per_language"]} segments)')
        table.append(f'| {book["titles"]["en"]} ({book["course"].split("/")[-1].replace("_", " ")}) | ' + ' | '.join(cells) + ' |')
    block = ('<!-- polished-translations:start -->\n## Final Polished Translations\n\n'
             'Japanese and Simplified Chinese editions are being prepared from the accepted final '
             'English companion TeX only. These are AI-assisted translations, not lecturer-endorsed '
             'editions. Equations and original board figures are preserved; labels within them remain '
             'as in the English source. A download is marked available only after complete segment '
             'coverage, a clean build, outline/overflow checks, and sampled semantic review.\n\n'
             + '\n'.join(table) + '\n\n[Workflow and limitations](references/POLISHED_TRANSLATIONS.md)\n'
             '<!-- polished-translations:end -->')
    for path in [ROOT / 'README.md', *sorted((ROOT / 'i18n').glob('README.*.md'))]:
        content = path.read_text()
        adjusted = block
        if path.parent.name == 'i18n':
            locale = path.name.removeprefix('README.').removesuffix('.md')
            heading, notice, label = {
                'ja': ('最終推敲版の翻訳', '最終推敲済みの英語講義ノートから、日本語版と簡体字中国語版を順次作成しています。数式・図版を保持し、検証済みのPDFのみ公開します。原講師が公認した翻訳ではありません。', '日本語・中国語版の公開状況'),
                'zh-Hans': ('最终润色版译本', '正在根据最终润色的英文讲义，依次制作日文版与简体中文版。保留公式与图版，仅发布通过检查的PDF。这些译本未经原讲师认可。', '日文与中文版发布进度'),
                'zh-Hant': ('最終潤色版譯本', '正在根據最終潤色的英文講義，依次製作日文版與簡體中文版。保留公式與圖版，僅發布通過檢查的PDF。這些譯本未經原講師認可。', '日文與中文版發布進度'),
                'de': ('Uebersetzungen der finalen Ausgabe', 'Japanische und chinesische Ausgaben entstehen aus den final redigierten englischen Notizen. Formeln und Abbildungen bleiben erhalten; nur gepruefte PDFs werden verlinkt.', 'Verfuegbarkeit und Pruefverfahren'),
                'es': ('Traducciones de la edición final', 'Se preparan versiones en japonés y chino a partir del texto inglés revisado. Se conservan las ecuaciones y figuras; solo se enlazan los PDF verificados.', 'Disponibilidad y controles'),
                'fr': ('Traductions de la version finale', 'Des versions japonaises et chinoises sont en préparation à partir du texte anglais révisé. Les équations et figures sont conservées ; seuls les PDF vérifiés sont proposés.', 'Disponibilité et vérification'),
                'ko': ('최종 교정판 번역', '최종 교정된 영어 강의 노트를 바탕으로 일본어판과 중국어판을 준비합니다. 수식과 그림을 유지하며 검증된 PDF만 공개합니다.', '번역판 공개 현황'),
                'ru': ('Переводы окончательной редакции', 'Готовятся японское и китайское издания окончательно отредактированных английских конспектов. Формулы и рисунки сохраняются; публикуются только проверенные PDF.', 'Доступность и проверка'),
                'vi': ('Bản dịch từ bản hiệu đính cuối', 'Đang chuẩn bị bản tiếng Nhật và tiếng Trung từ bản tiếng Anh đã hiệu đính. Giữ nguyên công thức và hình; chỉ công bố PDF đã kiểm tra.', 'Tiến độ và kiểm tra'),
                'ar': ('ترجمات النسخة النهائية', 'يجري إعداد نسختين يابانية وصينية من النص الإنجليزي المنقح، مع الحفاظ على المعادلات والرسوم ونشر ملفات PDF بعد التحقق.', 'حالة الإتاحة والتحقق'),
            }[locale]
            adjusted = ('<!-- polished-translations:start -->\n## ' + heading + '\n\n' + notice + '\n\n'
                        f'[{label}](../README.md#final-polished-translations)\n'
                        '<!-- polished-translations:end -->')
        if '<!-- polished-translations:start -->' in content:
            content = re.sub(r'<!-- polished-translations:start -->.*?<!-- polished-translations:end -->', lambda m: adjusted, content, flags=re.S)
        else:
            content += '\n\n' + adjusted + '\n'
        textwrite(path, content)


def verify_sources(book):
    src = ROOT / 'generated_course_notes' / book['course']
    for rel, expected in book['source_files'].items():
        if digest((src / rel).read_text()) != expected:
            raise RuntimeError(f'Final English source changed; prepare a separate edition: {rel}')


def validated_output(book, lang):
    folder = OUT / book['id'] / lang
    quality = folder / 'quality.json'
    pdf = folder / 'book.pdf'
    if not quality.exists() or not pdf.exists():
        return False
    q = read(quality)
    return (q.get('status') == 'validated'
            and hashlib.sha256(pdf.read_bytes()).hexdigest() == q.get('pdf_sha256')
            and all((folder / p).is_file() and digest((folder / p).read_text()) == sha
                    for p, sha in q.get('translated_tex', {}).items()))


def publish_book(book):
    """Publish only owned outputs; refuse a dirty index or edits outside README markers."""
    def git(*args):
        return subprocess.check_output(['git', *args], cwd=ROOT, text=True, stderr=subprocess.STDOUT)
    if git('diff', '--cached', '--name-only').strip():
        raise RuntimeError('Index has staged changes; automatic publication deferred')
    paths = ['README.md', *[str(p.relative_to(ROOT)) for p in (ROOT / 'i18n').glob('README.*.md')]]
    marker = r'\s*<!-- polished-translations:start -->.*?<!-- polished-translations:end -->\s*'
    for name in paths:
        previous = git('show', 'HEAD:' + name)
        current = (ROOT / name).read_text()
        if re.sub(marker, '', previous, flags=re.S).strip() != re.sub(marker, '', current, flags=re.S).strip():
            raise RuntimeError(f'Unrelated README changes: {name}; publication deferred')
    for p in sorted((OUT / book['id']).rglob('*')):
        if p.is_file():
            if p.stat().st_size >= 95 * 1024 * 1024:
                raise RuntimeError(f'Artifact too large for regular Git: {p.name}')
            paths.append(str(p.relative_to(ROOT)))
    git('add', '--', *paths)
    if git('diff', '--cached', '--name-only').strip():
        git('commit', '--only', '-m', 'Publish polished Japanese and Chinese ' + book['titles']['en'], '--', *paths)
    git('push', 'origin', 'HEAD')


def run(args):
    WORK.mkdir(parents=True, exist_ok=True)
    with (WORK / 'queue.lock').open('w') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        books = read(MANIFEST)['books']
        if not args.pilot_only and not (WORK / 'pilot-approved.json').exists():
            raise RuntimeError('First run --pilot-only; inspect both PDFs and approve-pilot before full queue')
        if args.pilot_only:
            books = books[:1]
        for book in books:
            if (WORK / 'STOP').exists():
                break
            verify_sources(book)
            if all(validated_output(book, l) for l in LANGS):
                continue
            write(WORK / 'status.json', {'state': 'running', 'book': book['id'], 'workers': args.workers})
            try:
                with ThreadPoolExecutor(max_workers=args.workers) as pool:
                    futures = []
                    for lang in LANGS:
                        for rel in book['source_files']:
                            if rel == 'common_preamble.tex':
                                continue
                            futures.append(pool.submit(translate_file, book, lang, rel, args))
                            time.sleep(args.ramp_seconds)
                    for future in as_completed(futures):
                        future.result()
                        update_readmes()
                for lang in LANGS:
                    compile_book(book, lang, args)
                    update_readmes()
                if args.publish:
                    try:
                        publish_book(book)
                        write(WORK / 'publication.json', {'book': book['id'], 'state': 'pushed'})
                    except Exception as exc:
                        write(WORK / 'publication.json', {'book': book['id'], 'state': 'deferred', 'error': str(exc)})
            except Exception as exc:
                write(WORK / 'status.json', {'state': 'blocked', 'book': book['id'], 'error': str(exc)})
                update_readmes()
                raise
        write(WORK / 'status.json', {'state': 'pilot_ready' if args.pilot_only else 'queue_stopped_or_complete'})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['prepare', 'run', 'status', 'compile', 'approve-pilot', 'readme', 'repair'])
    parser.add_argument('--workers', type=int, default=5)
    parser.add_argument('--ramp-seconds', type=float, default=1)
    parser.add_argument('--model', default='deepseek-chat')
    parser.add_argument('--toolkit-root', type=Path, default=ROOT.parent / 'ZhJpBook')
    parser.add_argument('--pilot-only', action='store_true')
    parser.add_argument('--publish', action='store_true', help='Commit and push validated outputs only')
    parser.add_argument('--book')
    parser.add_argument('--evidence', help='Human review note; required for approving the pilot')
    parser.add_argument('--repairs', type=Path, help='Source-bound reviewed repair JSON')
    args = parser.parse_args()
    if not 1 <= args.workers <= 5:
        parser.error('Use 1 to 5 workers')
    with ExitStack() as stack:
        if args.command in {'prepare', 'compile', 'approve-pilot', 'repair'}:
            WORK.mkdir(parents=True, exist_ok=True)
            lock = stack.enter_context((WORK / 'queue.lock').open('w'))
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        if args.command == 'prepare':
            prepare()
        elif args.command == 'run':
            run(args)
        elif args.command == 'status':
            print(json.dumps(status(), ensure_ascii=False, indent=2))
        elif args.command == 'readme':
            update_readmes()
        elif args.command == 'repair':
            if not args.repairs:
                parser.error('--repairs is required')
            apply_reviewed_repairs(args.repairs)
        elif args.command == 'compile':
            book = next(b for b in read(MANIFEST)['books'] if b['id'] == args.book)
            for lang in LANGS:
                compile_book(book, lang, args)
            update_readmes()
        else:
            if not args.evidence:
                parser.error('--evidence is required')
            book = read(MANIFEST)['books'][0]
            checks = {l: read(OUT / book['id'] / l / 'quality.json') for l in LANGS}
            if not all(validated_output(book, lang) for lang in LANGS):
                parser.error('Pilot is not validated')
            write(WORK / 'pilot-approved.json', {'evidence': args.evidence, 'checks': checks})


if __name__ == '__main__':
    main()
