#!/usr/bin/env python3
"""Derive multilingual reading links from verified outputs, never planned editions."""
import argparse
import html
import json
from pathlib import Path
import re
from urllib.parse import urlencode

import polished_translation as pipeline
from publish_generated_course_pdf import CANONICAL_FILENAMES

ROOT = Path(__file__).resolve().parents[1]
READER = 'https://learn.lazying.art/leonardsusskind-reader.html'
RAW = 'https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/'

CITATION_LABELS = {
    'en': ('Citation and Support', 'Cite these independent companion notes, not the original lectures:'),
    'ja': ('引用と支援', '以下は独立した補助講義ノートの引用情報です。元の講義は別途引用してください。'),
    'zh-Hans': ('引用与支持', '以下引用信息适用于独立编写的配套讲义，原始讲座请另行引用。'),
    'zh-Hant': ('引用與支持', '以下引用資訊適用於獨立編寫的配套講義，原始講座請另行引用。'),
    'ar': ('الاستشهاد والدعم', 'هذه بيانات الاستشهاد بالملاحظات المستقلة؛ يُرجى الاستشهاد بالمحاضرات الأصلية بصورة منفصلة.'),
    'de': ('Zitation und Unterstützung', 'Diese Angabe zitiert die unabhängigen Begleitnotizen; die Originalvorlesungen bitte gesondert zitieren.'),
    'es': ('Cita y apoyo', 'Esta referencia corresponde a los apuntes independientes; cita las conferencias originales por separado.'),
    'fr': ('Citation et soutien', 'Cette référence concerne les notes indépendantes ; citez les conférences originales séparément.'),
    'ko': ('인용 및 후원', '독립적으로 편집한 보조 강의 노트의 인용 정보입니다. 원래 강의는 별도로 인용해 주세요.'),
    'ru': ('Цитирование и поддержка', 'Эта ссылка относится к независимым сопроводительным заметкам; исходные лекции цитируйте отдельно.'),
    'vi': ('Trích dẫn và hỗ trợ', 'Thông tin này dành cho ghi chú đồng hành độc lập; vui lòng trích dẫn riêng các bài giảng gốc.'),
}


def citation_block(locale):
    heading, explanation = CITATION_LABELS[locale]
    prefix = '' if locale == 'en' else '../'
    return ('<!-- reading-citation:start -->\n## ' + heading + '\n\n' + explanation
            + '\n\n[CITATION.cff](' + prefix + 'CITATION.cff) · '
            '[GitHub Sponsors](https://github.com/sponsors/lachlanchen)\n\n'
            '```bibtex\n@software{lazyingart_susskind_companion_notes,\n'
            '  author = {{LazyingArt contributors}},\n'
            '  title = {Leonard Susskind Lecture Notes: Independent Multilingual Companion Editions},\n'
            '  url = {https://github.com/lachlanchen/leonardsusskind}\n}\n```\n'
            '<!-- reading-citation:end -->\n')

NOTICES = {
 'en': ('Read in English, Japanese and Chinese',
        'Japanese and Simplified Chinese editions are available for {count} final polished books, alongside the English originals. Read each language independently in PDF, or select aligned language layers in Bunko.',
        'New translated PDFs use 1.2 × A5 paper (177.6 × 252 mm), with 12 pt text, clear spacing, equations and original figures. The older “pocket 1.2x” files refer to enlarged type, not this paper size.',
        'We are expanding this multilingual library. Help with additional languages, scientific proofreading, accessibility or layout: open an issue or contribute a source-backed correction. More languages are planned, not yet published.'),
 'ja': ('英語・日本語・中国語で読む',
        '最終推敲済みの{count}冊に日本語版と簡体字中国語版があり、英語原版と併せて読めます。PDFは各言語の独立版、Bunkoでは対応する言語を選択して読めます。',
        '新しい翻訳PDFはA5の縦横を1.2倍にした177.6 × 252 mm、本文12 ptです。数式・原図を保持しています。従来の「pocket 1.2x」は文字の拡大率であり、この用紙寸法とは異なります。',
        '多言語ライブラリを拡充しています。新しい言語への翻訳、物理内容の校閲、アクセシビリティ、組版への協力を歓迎します。根拠を添えてIssueや修正案をお寄せください。他言語版は計画中で、まだ公開していません。'),
 'zh-Hans': ('用英语、日语和中文阅读',
        '{count}册最终润色讲义已有日文版与简体中文版，并保留英文原版。PDF是各语言独立成书的版本；Bunko可选择对应的语言层阅读。',
        '新译本默认使用A5长宽各放大1.2倍的纸张（177.6 × 252 mm）、12 pt正文和舒适行距，保留公式与原图。旧版“pocket 1.2x”指字号放大，并非此纸张尺寸。',
        '我们正拓展这座多语言书库，欢迎参与其他语言翻译、科学内容校对、无障碍阅读与排版改进。请通过Issue或附有来源依据的修订协作。其他语言版本仍在规划中，尚未发布。'),
 'zh-Hant': ('用英語、日語和中文閱讀',
        '{count}冊最終潤色講義已有日文版與簡體中文版，並保留英文原版。PDF是各語言獨立成書的版本；Bunko可選擇對應的語言層閱讀。',
        '新譯本預設使用A5長寬各放大1.2倍的紙張（177.6 × 252 mm）、12 pt正文和舒適行距，保留公式與原圖。舊版「pocket 1.2x」指字號放大，並非此紙張尺寸。',
        '我們正拓展多語言書庫，歡迎參與其他語言翻譯、科學內容校對、無障礙閱讀與排版改進。請透過Issue或附有來源依據的修訂協作。其他語言版本仍在規劃中，尚未發布。'),
 'de': ('Auf Englisch, Japanisch und Chinesisch lesen',
        'Für {count} abschließend redigierte Bücher sind japanische und vereinfachte chinesische Ausgaben neben den englischen Originalen verfügbar. PDFs sind eigenständige Sprachausgaben; Bunko bietet ausgerichtete Sprachebenen.',
        'Neue übersetzte PDFs verwenden 177.6 × 252 mm (beide A5-Seiten × 1.2), 12 pt Schrift und erhalten Formeln und Abbildungen. Das ältere „pocket 1.2x“ bezeichnet größere Schrift, nicht dieses Papierformat.',
        'Wir erweitern die mehrsprachige Bibliothek. Beiträge zu weiteren Sprachen, Physik-Korrekturlesen, Barrierefreiheit und Layout sind willkommen. Bitte ein Issue oder eine belegte Korrektur einreichen. Weitere Sprachen sind geplant, noch nicht veröffentlicht.'),
 'es': ('Leer en inglés, japonés y chino',
        'Hay ediciones japonesas y en chino simplificado de {count} libros revisados, junto con los originales ingleses. Los PDF son ediciones independientes; Bunko permite elegir capas de idiomas alineadas.',
        'Los nuevos PDF traducidos usan papel de 177.6 × 252 mm (ambas dimensiones de A5 × 1.2), texto de 12 pt y conservan ecuaciones e ilustraciones. El antiguo «pocket 1.2x» amplía la tipografía, no indica este tamaño de papel.',
        'Estamos ampliando la biblioteca multilingüe. Colabora con otros idiomas, revisión científica, accesibilidad o maquetación mediante una incidencia o corrección documentada. Otros idiomas están previstos, aún no publicados.'),
 'fr': ('Lire en anglais, japonais et chinois',
        'Les éditions japonaises et chinoises simplifiées de {count} livres révisés sont disponibles avec les originaux anglais. Les PDF sont des éditions autonomes ; Bunko permet de choisir des couches linguistiques alignées.',
        'Les nouveaux PDF traduits utilisent du papier de 177.6 × 252 mm (chaque dimension A5 × 1.2), un corps de 12 pt et conservent équations et figures. L’ancien « pocket 1.2x » désigne des caractères agrandis, pas ce format de papier.',
        'Nous élargissons la bibliothèque multilingue. Traductions supplémentaires, relecture scientifique, accessibilité et mise en page : vos contributions sont bienvenues via une issue ou une correction sourcée. Les autres langues sont prévues, pas encore publiées.'),
 'ko': ('영어·일본어·중국어로 읽기',
        '최종 교정된 {count}권의 일본어판과 중국어 간체판을 영어 원본과 함께 제공합니다. PDF는 언어별 독립판이며 Bunko에서는 정렬된 언어 층을 선택할 수 있습니다.',
        '새 번역 PDF는 A5의 가로·세로를 각각 1.2배 한 177.6 × 252 mm 용지와 12 pt 본문을 사용하며 수식과 원본 그림을 유지합니다. 기존 “pocket 1.2x”는 글자 확대율로, 이 용지 크기와 다릅니다.',
        '다국어 서가를 확장하고 있습니다. 추가 언어, 과학 교정, 접근성, 조판에 참여해 주세요. 근거가 있는 수정이나 이슈를 환영합니다. 다른 언어판은 계획 중이며 아직 공개되지 않았습니다.'),
 'ru': ('Читайте на английском, японском и китайском',
        'Для {count} окончательно отредактированных книг доступны японские и упрощённые китайские издания наряду с английскими оригиналами. PDF выпускаются отдельно для каждого языка; в Bunko можно выбирать выровненные языковые слои.',
        'Новые переводные PDF используют бумагу 177.6 × 252 мм (обе стороны A5 × 1.2), шрифт 12 pt и сохраняют формулы и рисунки. Старое обозначение «pocket 1.2x» означает увеличение шрифта, а не этот формат бумаги.',
        'Мы расширяем многоязычную библиотеку. Приглашаем помогать с другими языками, научной вычиткой, доступностью и вёрсткой через issue или обоснованное исправление. Другие языки запланированы, но пока не опубликованы.'),
 'vi': ('Đọc bằng tiếng Anh, tiếng Nhật và tiếng Trung',
        'Có bản tiếng Nhật và tiếng Trung giản thể cho {count} sách đã hiệu đính, bên cạnh bản gốc tiếng Anh. PDF là sách độc lập theo từng ngôn ngữ; Bunko cho phép chọn các lớp ngôn ngữ tương ứng.',
        'PDF dịch mới dùng giấy 177.6 × 252 mm (mỗi chiều A5 × 1.2), chữ 12 pt, giữ nguyên công thức và hình. “pocket 1.2x” cũ chỉ cỡ chữ phóng lớn, không phải khổ giấy này.',
        'Chúng tôi đang mở rộng thư viện đa ngôn ngữ. Mời đóng góp ngôn ngữ mới, hiệu đính khoa học, khả năng tiếp cận và dàn trang qua issue hoặc bản sửa có nguồn. Các ngôn ngữ khác đang được lên kế hoạch, chưa xuất bản.'),
 'ar': ('اقرأ بالإنجليزية واليابانية والصينية',
        'تتوفر طبعات يابانية وصينية مبسطة لعدد {count} من الكتب المنقحة، إلى جانب الأصل الإنجليزي. ملفات PDF طبعات مستقلة لكل لغة، ويتيح Bunko اختيار طبقات لغوية متقابلة.',
        'تستخدم ملفات PDF المترجمة الجديدة ورقاً بقياس 177.6 × 252 مم (كل بُعد من A5 مضروب في 1.2)، وخطاً بحجم 12 نقطة، مع حفظ المعادلات والرسوم. يشير «pocket 1.2x» القديم إلى تكبير الخط لا إلى حجم الورق هذا.',
        'نعمل على توسيع المكتبة متعددة اللغات. نرحب بالمساهمة بلغات إضافية وبالمراجعة العلمية وتحسين الإتاحة والتنسيق، عبر issue أو تصحيح موثق. اللغات الأخرى مخطط لها ولم تُنشر بعد.'),
}


def catalog():
    result = {'schema': 1, 'translatedPdfLayout': pipeline.LAYOUT, 'paperMm': [177.6, 252], 'books': {}}
    for book in pipeline.read(pipeline.MANIFEST)['books']:
        filename = CANONICAL_FILENAMES[book['course']]
        slug = filename[:-4].replace('_', '-')
        bunko = next((p.parent.name for p in (ROOT.parent / 'bunko-books/books').glob('physics-*/rights.json')
                      if any(r.endswith('/generated_course_notes/' + book['course']) for r in pipeline.read(p)['references'])), None)
        row = {'id': book['id'], 'titles': book['titles'], 'bunkoId': bunko, 'editions': {
            'en': {'pdf': RAW + 'all_notes/pocket_books_1_2x/' + filename[:-4] + '_pocket_1_2x.pdf',
                   'layout': 'legacy-pocket-1.2x-type'}}}
        for lang in pipeline.LANGS:
            if pipeline.validated_output(book, lang):
                row['editions'][lang] = {'pdf': RAW + f'translations/{book["id"]}/{lang}/book.pdf',
                                         'layout': pipeline.LAYOUT}
        result['books'][slug] = row
    return result


def decorate_readmes():
    data = catalog()
    pipeline.write(ROOT / 'references/reading_editions.json', data)
    count = sum(all(lang in row['editions'] for lang in ('ja', 'zh')) for row in data['books'].values())
    for path in [ROOT / 'README.md', *sorted((ROOT / 'i18n').glob('README.*.md'))]:
        locale = 'en' if path.parent == ROOT else path.name[7:-3]
        heading, available, layout, invitation = NOTICES[locale]
        block = ('<!-- reading-languages:start -->\n## ' + heading + '\n\n'
                 + available.format(count=count) + '\n\n' + layout + '\n\n' + invitation + '\n\n'
                 '[Bunko](https://lachlan.lazying.art/Bunko/) · [LazyLearn](' + READER + ') · '
                 '[GitHub Issues](https://github.com/lachlanchen/leonardsusskind/issues)\n'
                 '<!-- reading-languages:end -->')
        text = path.read_text()
        text = '\n'.join(
            '[Bunko](https://lachlan.lazying.art/Bunko/) · ' + available.format(count=count)
            if 'https://apps.apple.com/us/app/bunko-classics-with-ruby/' in line
            and 'https://lachlan.lazying.art/Bunko/' in line else line
            for line in text.split('\n'))
        text = re.sub(r'\n*<!-- reading-languages:start -->.*?<!-- reading-languages:end -->\n*', '\n\n', text, flags=re.S)
        text = re.sub(r'(^# [^\n]+\n)', lambda m: m[0] + '\n' + block + '\n', text, count=1, flags=re.M)
        def annotate(match):
            cell = re.sub(r'\s*<!-- edition-links -->.*?<!-- /edition-links -->', '', match[0], flags=re.S)
            link = re.search(r'leonardsusskind-reader\.html\?book=([^"&]+)', cell)
            if not link or link[1] not in data['books']:
                return cell
            row = data['books'][link[1]]
            links = ['<a href="' + READER + '?' + html.escape(urlencode({'book': link[1], 'lang': lang})) + '">' + label + '</a>'
                     for lang, label in [('en', 'English'), ('ja', '日本語'), ('zh', '中文')] if lang in row['editions']]
            annotation = '\n      <!-- edition-links --><br><sub>' + ' · '.join(links) + '</sub><!-- /edition-links -->\n    '
            # A blank line ends the GFM HTML block; indented rows then become code.
            return re.sub(r'\s*</td>$', lambda _: annotation + '</td>', cell)
        text = re.sub(r'<td align="center">.*?</td>', annotate, text, flags=re.S)
        # Older README translations have no cover catalog. Add one shared, compact
        # catalog rather than leaving their language announcement disconnected.
        text = re.sub(r'\n*<!-- language-covers:start -->.*?<!-- language-covers:end -->\n*', '\n\n', text, flags=re.S)
        if 'readme-covers/' not in text:
            rows = ['<!-- language-covers:start -->', '<table>']
            for slug, row in data['books'].items():
                stem = CANONICAL_FILENAMES[row['id'].replace('--', '/')][:-4]
                images = [ROOT / 'figs/readme-covers' / (stem + suffix + '.png') for suffix in ('', '_first_page')]
                cover = next(p for p in images if p.exists())
                title_locale = 'zh' if locale.startswith('zh') else locale
                title = html.escape(row['titles'].get(title_locale, row['titles']['en']))
                links = ['<a href="' + READER + '?' + html.escape(urlencode({'book': slug, 'lang': lang})) + '">' + label + '</a>'
                         for lang, label in [('en', 'English'), ('ja', '日本語'), ('zh', '中文')] if lang in row['editions']]
                rows.append('<tr><td><img width="85" src="../' + str(cover.relative_to(ROOT)) + '" alt="' + title + '"></td><td><strong>' + title + '</strong><br>' + ' · '.join(links) + '</td></tr>')
            rows += ['</table>', '<!-- language-covers:end -->']
            text = text.replace('<!-- reading-languages:end -->', '<!-- reading-languages:end -->\n\n' + '\n'.join(rows), 1)
        text = re.sub(r'\n*<!-- reading-citation:start -->.*?<!-- reading-citation:end -->\n*', '\n\n', text, flags=re.S)
        text = text.rstrip() + '\n\n' + citation_block(locale)
        pipeline.textwrite(path, re.sub(r'^[ \t]+$', '', text, flags=re.M))
    return data


def sync_reader(data, path):
    text = path.read_text()
    block = '<!-- reading-editions:start -->\n<script id="reading-editions" type="application/json">' + json.dumps(data, ensure_ascii=False).replace('<', '\\u003c') + '</script>\n<!-- reading-editions:end -->'
    if '<!-- reading-editions:start -->' in text:
        text = re.sub(r'<!-- reading-editions:start -->.*?<!-- reading-editions:end -->', lambda m: block, text, flags=re.S)
    else:
        text = text.replace('    <script>\n', block + '\n    <script>\n', 1)
    pipeline.textwrite(path, text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--reader', type=Path)
    args = parser.parse_args()
    data = decorate_readmes()
    if args.reader:
        sync_reader(data, args.reader)
