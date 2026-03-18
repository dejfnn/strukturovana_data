"""
Konvertor Markdown do HTML pro Word
Převádí MD soubory na HTML, které lze otevřít ve Wordu

Použití:
    python md_to_html.py                    # Konvertuje všechny *.md v aktuální složce
    python md_to_html.py soubor.md          # Konvertuje konkrétní soubor
    python md_to_html.py soubor1.md soubor2.md  # Konvertuje více souborů
"""

import markdown
import sys
import os
import io
import glob
import re

# Nastavení UTF-8 pro Windows konzoli
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')


def extract_title_from_md(md_content):
    """Extrahuje title z prvního H1 nadpisu v MD souboru"""
    # Hledá první # nadpis
    match = re.search(r'^#\s+(.+)$', md_content, re.MULTILINE)
    if match:
        # Odstraní případné speciální znaky z titlu
        title = match.group(1).strip()
        # Odstraní markdown formátování (bold, italic, odkazy)
        title = re.sub(r'\*\*(.+?)\*\*', r'\1', title)
        title = re.sub(r'\*(.+?)\*', r'\1', title)
        title = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', title)
        return title
    return None


def convert_md_to_html(md_file):
    """Převede MD soubor na HTML"""

    # Načtení MD souboru
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Extrakce titlu z obsahu
    title = extract_title_from_md(md_content)
    if not title:
        # Fallback na název souboru bez přípony
        title = os.path.splitext(os.path.basename(md_file))[0].replace('-', ' ').replace('_', ' ').title()

    # Konverze na HTML
    html_content = markdown.markdown(
        md_content,
        extensions=['extra', 'codehilite', 'toc', 'tables']
    )

    # HTML šablona s CSS pro Word
    html_template = f"""<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            max-width: 1200px;
            margin: 40px auto;
            padding: 20px;
            background: #fff;
            color: #333;
        }}

        h1 {{
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
            margin-top: 40px;
        }}

        h2 {{
            color: #34495e;
            border-bottom: 2px solid #95a5a6;
            padding-bottom: 8px;
            margin-top: 30px;
        }}

        h3 {{
            color: #7f8c8d;
            margin-top: 20px;
        }}

        pre {{
            background: #f4f4f4;
            border: 1px solid #ddd;
            border-left: 4px solid #3498db;
            padding: 15px;
            overflow-x: auto;
            border-radius: 4px;
            font-size: 14px;
        }}

        code {{
            background: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Consolas', 'Monaco', monospace;
            font-size: 14px;
        }}

        pre code {{
            background: transparent;
            padding: 0;
        }}

        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
        }}

        table th, table td {{
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }}

        table th {{
            background: #3498db;
            color: white;
            font-weight: bold;
        }}

        table tr:nth-child(even) {{
            background: #f9f9f9;
        }}

        blockquote {{
            border-left: 4px solid #3498db;
            padding-left: 20px;
            margin-left: 0;
            color: #555;
            font-style: italic;
        }}

        ul, ol {{
            margin: 15px 0;
            padding-left: 30px;
        }}

        li {{
            margin: 8px 0;
        }}

        a {{
            color: #3498db;
            text-decoration: none;
        }}

        a:hover {{
            text-decoration: underline;
        }}

        hr {{
            border: none;
            border-top: 2px solid #ecf0f1;
            margin: 30px 0;
        }}

        .highlight {{
            background: #fff3cd;
            padding: 2px 4px;
            border-radius: 3px;
        }}
    </style>
</head>
<body>
{html_content}
</body>
</html>
"""

    # Vytvoření HTML souboru
    html_file = md_file.replace('.md', '.html')
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_template)

    print(f"✓ Vytvořen: {html_file}")
    return html_file

def main():
    """Hlavní funkce"""

    print("=" * 70)
    print("KONVERZE MARKDOWN → HTML (pro Word)")
    print("=" * 70)
    print()

    # Určení MD souborů k převodu
    if len(sys.argv) > 1:
        # Soubory zadané jako argumenty
        md_files = sys.argv[1:]
    else:
        # Automaticky najít všechny *.md v aktuální složce
        md_files = glob.glob('*.md')
        if not md_files:
            print("⚠ Žádné MD soubory nenalezeny v aktuální složce.")
            print("  Použití: python md_to_html.py [soubor.md ...]")
            return

    print(f"Nalezeno {len(md_files)} MD soubor(ů) ke konverzi:")
    for f in md_files:
        print(f"  • {f}")
    print()

    converted = []
    for md_file in md_files:
        if os.path.exists(md_file):
            html_file = convert_md_to_html(md_file)
            converted.append(html_file)
        else:
            print(f"⚠ Soubor nenalezen: {md_file}")

    print()
    print("=" * 70)
    print("HOTOVO!")
    print("=" * 70)
    print()
    print("Jak otevřít ve Wordu:")
    print("1. Otevřete Word")
    print("2. Soubor → Otevřít → Vyberte HTML soubor")
    print("3. Soubor → Uložit jako → Vyberte formát .docx")
    print()
    print("Vytvořené HTML soubory:")
    for html_file in converted:
        print(f"  • {html_file}")
    print()

if __name__ == "__main__":
    main()
