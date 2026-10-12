#!/usr/bin/env python3
"""Check final paper geometry, text bounds and immutable math/figure inventories."""
from collections import Counter
import json
from pathlib import Path
import re

import fitz
from pylatexenc import latexwalker as lw
import polished_translation as p


def inventory(text):
    math, figures = [], []
    nodes, _, _ = lw.LatexWalker(text).get_latex_nodes()
    def walk(items):
        for node in items:
            if isinstance(node, lw.LatexMathNode):
                math.append(text[node.pos:node.pos + node.len])
            elif isinstance(node, lw.LatexEnvironmentNode):
                if node.environmentname.rstrip('*') in {'equation', 'align', 'alignat', 'gather', 'multline', 'displaymath', 'eqnarray', 'flalign', 'tikzpicture'}:
                    math.append(text[node.pos:node.pos + node.len])
                else:
                    walk(node.nodelist)
            elif isinstance(node, lw.LatexGroupNode):
                walk(node.nodelist)
            elif isinstance(node, lw.LatexMacroNode) and node.nodeargd:
                if node.macroname == 'includegraphics':
                    figures.append(text[node.pos:node.pos+node.len])
                else:
                    walk([arg for arg in node.nodeargd.argnlist if arg])
    walk(nodes)
    return Counter(math), Counter(figures)


def audit():
    books, errors = [], []
    for book in p.read(p.MANIFEST)['books']:
        p.verify_sources(book)
        original = p.ROOT / 'generated_course_notes' / book['course']
        for lang in p.LANGS:
            label = book['id'] + '/' + lang
            if not p.validated_output(book, lang):
                errors.append(label + ': output not validated')
                continue
            dst = p.OUT / book['id'] / lang
            math_count = figure_count = 0
            for rel in book['source_files']:
                if not rel.endswith('content.tex'):
                    continue
                source = inventory((original / rel).read_text())
                target = inventory((dst / rel).read_text())
                if source != target:
                    errors.append(label + '/' + rel + ': equation/figure inventory changed')
                math_count += sum(source[0].values())
                figure_count += sum(source[1].values())
            with fitz.open(dst / 'book.pdf') as pdf:
                for number, page in enumerate(pdf, 1):
                    mm = [page.rect.width * 25.4 / 72, page.rect.height * 25.4 / 72]
                    if any(abs(a-b) > .1 for a, b in zip(mm, [177.6, 252])):
                        errors.append(f'{label}: page {number} wrong dimensions {mm}')
                    for word in page.get_text('words'):
                        if not (page.rect + (-1, -1, 1, 1)).contains(fitz.Rect(word[:4])):
                            errors.append(f'{label}: page {number} text outside page')
                            break
                books.append({'id': book['id'], 'language': lang, 'pages': len(pdf),
                              'outlineEntries': len(pdf.get_toc()), 'mathAndDiagrams': math_count,
                              'figureCommands': figure_count})
    result = {'paperMm': [177.6, 252], 'layoutProfile': p.LAYOUT, 'editions': books,
              'errors': errors, 'semanticReview': 'sampled, not exhaustive'}
    p.write(p.ROOT / 'references/reading_editions_audit.json', result)
    print(json.dumps({'editions': len(books), 'errors': errors}, ensure_ascii=False))
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(audit())
