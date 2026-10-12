#!/usr/bin/env python3
"""Lossless cache migration and three source-bound, manually reviewed repairs."""
import fcntl
import re
import time
import polished_translation as p


def migrate():
    for book in p.read(p.MANIFEST)['books']:
        p.verify_sources(book)
        for rel in book['source_files']:
            if rel == 'common_preamble.tex':
                continue
            path = p.WORK / 'prepared' / book['id'] / (rel + '.json')
            old = p.read(path)
            _, protected, expansion = p.split_closing_tokens('', old['protected'])
            if not expansion:
                continue
            def expand(value):
                return p.TOKEN.sub(lambda m: expansion.get(m[0], m[0]), value)
            new = {**old, 'protected': protected, 'parts': [expand(s) for s in old['parts']]}
            for a, b in zip(old['parts'], new['parts']):
                assert p.restore(a, old['protected']) == p.restore(b, protected)
            updates = []
            for lang in p.LANGS:
                cache = p.result_path(book, lang, rel)
                if not cache.exists():
                    continue
                data = p.read(cache)
                if data.get('inflight'):
                    raise RuntimeError('Resolve interrupted requests before migration')
                for field in ('accepted', 'candidates'):
                    for key, value in data.get(field, {}).items():
                        changed = expand(value)
                        assert p.restore(value, old['protected']) == p.restore(changed, protected)
                        data[field][key] = changed
                updates.append((cache, data))
            for target, value in [(path, new), *updates]:
                p.write(target.with_suffix(f'.{time.time_ns()}.bak'), p.read(target))
                p.write(target, value)


def reviewed_repairs():
    for book in p.read(p.MANIFEST)['books']:
        rows = []
        if book['id'] == 'supplementary--advanced_quantum_mechanics--2013_fall':
            rel, key = 'chapters/lecture_01/content.tex', '124'
            prepared = p.read(p.WORK / 'prepared' / book['id'] / (rel + '.json'))
            source = prepared['parts'][int(key)]
            match = re.search(r'(?P<a>@@T\d{6}@@), not (?P<b>@@T\d{6}@@)', source)
            assert match and p.restore(match['a'], prepared['protected']) == r'\(\psi(x-\epsilon)\)'
            assert p.restore(match['b'], prepared['protected']) == r'\(\psi(x+\epsilon)\)'
            old = p.read(p.result_path(book, 'ja', rel))['accepted'][key]
            wrong = match['a'] + 'ではなく' + match['b']
            if wrong in old:
                translation = old.replace(wrong, match['b'] + 'ではなく' + match['a'])
                rows.append(('ja', rel, key, translation,
                             'Corrected reversed negation: a right active shift uses psi(x-epsilon), NOT psi(x+epsilon); confirmed against the neighboring derivation.'))
        elif book['id'] == 'supplementary--string_theory--2010_fall_string_theory_and_m_theory':
            rel, key = 'chapters/lecture_01/content.tex', '272'
            prepared = p.read(p.WORK / 'prepared' / book['id'] / (rel + '.json'))
            source = prepared['parts'][int(key)]
            assert source.startswith('For fixed mass, a smaller radius') and not p.TOKEN.findall(source)
            translation = ('質量が一定なら、半径が小さいほど慣性モーメントははるかに小さくなり、励起エネルギーははるかに大きくなる。'
                'ハドロンはその内部力学の尺度では大きいため、回転励起に必要なエネルギーはおよそ一ギガ電子ボルトで、粒子衝突で到達できる。'
                '電子が何らかの空間的な内部構造をもつとしても、実験による制限から、その尺度ははるかに小さくなり、回転励起は利用可能なエネルギーを大幅に超えることになる。'
                'バスケットボールは逆の極端にある。慣性モーメントが非常に大きいため、角運動量一量子に必要なエネルギーは知覚できないほど小さい。'
                '原子の回転または軌道におけるエネルギーの段階はこの両極端の間にあり、通常は電子ボルトの尺度にある。')
            rows.append(('ja', rel, key, translation, 'Removed a hallucinated placeholder absent from English; checked every physical comparison against the source.'))
        elif book['id'] == 'core--cosmology--2009_winter_legacy_cosmology':
            rel, key = 'chapters/lecture_05/content.tex', '0'
            prepared = p.read(p.WORK / 'prepared' / book['id'] / (rel + '.json'))
            source = prepared['parts'][0]
            assert p.restore(source, prepared['protected']) == r'\chapter{Spheres, Hyperbolic Space, and the Meaning of \(k\)}'
            opening, math, closing = p.TOKEN.findall(source)
            for lang, prefix, suffix in [('ja', '球面、双曲空間、そして', 'の意味'), ('zh', '球面、双曲空间与', '的含义')]:
                rows.append((lang, rel, key, opening + prefix + math + suffix + closing,
                             'Put the complete faithful chapter title inside the separated closing brace; no physical content changed.'))
        if not rows:
            continue
        packet = {'book': book['id'], 'repairs': []}
        for lang, rel, key, translation, reason in rows:
            prepared = p.read(p.WORK / 'prepared' / book['id'] / (rel + '.json'))
            cache = p.read(p.result_path(book, lang, rel))
            if cache['accepted'].get(key) == translation:
                continue
            if key in cache['accepted'] and book['id'] != 'supplementary--advanced_quantum_mechanics--2013_fall':
                raise ValueError('Refusing to replace a later accepted translation')
            packet['repairs'].append({'lang': lang, 'file': rel, 'segment_id': key,
                'source_sha256': prepared['source_sha256'],
                'source': p.restore(prepared['parts'][int(key)], prepared['protected']),
                'translation': translation, 'reason': reason,
                **({'previous_sha256': p.digest(cache['accepted'][key])} if key in cache['accepted'] else {})})
        if packet['repairs']:
            path = p.WORK / 'reviewed-repairs' / (book['id'] + '-boundaries.json')
            p.write(path, packet)
            p.apply_reviewed_repairs(path)


if __name__ == '__main__':
    with (p.WORK / 'queue.lock').open('w') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        migrate()
        reviewed_repairs()
