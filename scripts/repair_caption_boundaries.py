#!/usr/bin/env python3
"""Audit all cached captions; move only misplaced existing prose, never rewrite it."""
import argparse
import fcntl
import polished_translation as p


def run(apply=False):
    total = 0
    for book in p.read(p.MANIFEST)['books']:
        rows = []
        for rel in book['source_files']:
            if not rel.endswith('content.tex'):
                continue
            prepared = p.read(p.WORK / 'prepared' / book['id'] / (rel + '.json'))
            for lang in p.LANGS:
                cache = p.read(p.result_path(book, lang, rel))
                for key, text in cache['accepted'].items():
                    moves = p.caption_escapes(prepared['parts'][int(key)], text, prepared['protected'])
                    if not moves:
                        continue
                    changed = text
                    for start, end, replacement in sorted(moves, reverse=True):
                        changed = changed[:start] + replacement + changed[end:]
                    assert p.TOKEN.sub('', changed).split() == p.TOKEN.sub('', text).split()
                    error = p.validate(prepared['parts'][int(key)], changed, lang, prepared['protected'])
                    if error:
                        raise ValueError(f'{book["id"]}/{rel}/{key}: {error}')
                    rows.append({'lang': lang, 'file': rel, 'segment_id': key,
                                 'source_sha256': prepared['source_sha256'],
                                 'source': p.restore(prepared['parts'][int(key)], prepared['protected']),
                                 'translation': changed, 'previous_sha256': p.digest(text),
                                 'reason': 'Moved existing trailing caption prose inside its source-defined argument; every translated character and frozen token retained.'})
                    print(book['id'], lang, rel, key, 'caption boundary')
        if rows:
            total += len(rows)
            if apply:
                path = p.WORK / 'reviewed-repairs' / (book['id'] + '-captions.json')
                p.write(path, {'book': book['id'], 'repairs': rows})
                p.apply_reviewed_repairs(path)
    print('Caption repairs:', total, 'applied' if apply else 'proposed')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    with (p.WORK / 'queue.lock').open('a') as lock:
        if args.apply:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        run(args.apply)
