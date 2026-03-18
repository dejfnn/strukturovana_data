# Strukturovaná data JSON-LD — Claude Code nástroj

Standardizovaný nástroj pro tvorbu, revizi a dokumentaci Schema.org strukturovaných dat (JSON-LD) pro klientské weby. Postavený na Claude Code s definovanými skilly, agenty a šablonami.

## Požadavky

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) (CLI)
- Python 3.x (pro validátor a MD→HTML konvertor)

## Instalace

```bash
git clone https://github.com/{org}/strukturovana-data-jsonld.git
cd strukturovana-data-jsonld
```

Otevři v Claude Code — konfigurace se načte automaticky z `CLAUDE.md` a `.claude/`.

## Použití

Celý proces má 5 kroků, každý jako samostatný skill:

### 1. `/analyze` — Analýza webu
```
/analyze https://www.example.cz
```
- Najde sitemap, identifikuje typy stránek, sebere data
- Zhodnotí kvalitu sitemap, případně crawluje web
- **Předloží vzorek stránek ke schválení** před pokračováním

Volitelné vstupy:
- URL sitemap: `/analyze https://www.example.cz --sitemap https://www.example.cz/sitemap.xml`
- Vzorové stránky: uživatel může zadat konkrétní URL k analýze

### 2. `/audit` — Revize stávajících dat
```
/audit
```
- Extrahuje existující JSON-LD ze všech vzorkových stránek
- Zhodnotí správnost, kompletnost a kvalitu
- Identifikuje chyby a chybějící schémata

### 3. `/create-schemas` — Tvorba schémat
```
/create-schemas
```
- Vytvoří JSON-LD pro každý typ stránky z šablon
- Vyplní reálnými daty z analýzy
- Vygeneruje testovací `test-*.json` soubory

### 4. `/validate` — Validace
```
/validate
```
- Spustí lokální validátor (`validate_schema.py`)
- Zkontroluje konzistenci napříč schématy
- Připraví data pro online validátory (Schema.org, Google Rich Results)

### 5. `/document` — Dokumentace
```
/document
```
- Vytvoří README.md pro klienta
- Vygeneruje HTML verze všech .md souborů (kompatibilní s Word)
- Provede finální kontrolu kompletnosti

## Struktura projektu

```
CLAUDE.md                       ← Projektové instrukce pro Claude Code
.claude/
  settings.local.json           ← Oprávnění (WebFetch, Python, soubory)
  skills/
    analyze.md                  ← /analyze skill
    audit.md                    ← /audit skill
    create-schemas.md           ← /create-schemas skill
    validate.md                 ← /validate skill
    document.md                 ← /document skill
  agents/
    web-analyzer.md             ← Crawlování webu, sběr dat
    schema-extractor.md         ← Extrakce existujících JSON-LD
SABLONY/                        ← 9 JSON-LD šablon
  organization.json, website.json, product.json, article.json,
  breadcrumb.json, collection-page.json, faq-page.json,
  local-business.json, service.json
NASTROJE/                       ← Python nástroje
  validate_schema.py            ← Validátor JSON-LD
  md_to_html.py                 ← Konvertor MD → HTML
OUTPUT/                         ← Klientské projekty (lokální, v .gitignore)
  SICO/                         ← Referenční vzorový projekt
UNIVERZALNI-NAVOD.md            ← Detailní referenční příručka
```

## Výstup pro klienta

Každý dokončený projekt (`OUTPUT/{KLIENT}/`) obsahuje:

| Soubor | Obsah |
|--------|-------|
| `analyza-webu.md` | Analýza struktury webu a typů stránek |
| `revize-stavajicich-dat.md` | Revize stávající implementace JSON-LD |
| `strukturovana-data-{klient}.md` | Kompletní JSON-LD schémata s implementačními poznámkami |
| `test-*.json` | Validované testovací soubory pro každý typ stránky |
| `README.md` | Klientská dokumentace s instrukcemi |
| `*.html` | HTML verze všech .md souborů (pro Word) |

## Podporované Schema.org typy

| Typ | Použití | Priorita |
|-----|---------|----------|
| Organization | Firemní identita (homepage) | KRITICKÁ |
| WebSite | Informace o webu + SearchAction | KRITICKÁ |
| BreadcrumbList | Navigace (všechny stránky) | KRITICKÁ |
| Product + Offer | Produktové stránky | VYSOKÁ |
| Article | Blog, články, novinky | VYSOKÁ |
| CollectionPage | Kategorie, výpisy | STŘEDNÍ |
| LocalBusiness | Pobočky, prodejny | STŘEDNÍ |
| FAQPage | FAQ sekce | STŘEDNÍ |
| Service | Služby s ceníkem | STŘEDNÍ |

## Referenční projekt

`OUTPUT/SICO/` obsahuje kompletně vypracovaný vzorový projekt — ideální pro pochopení očekávaného výstupu.

## Detailní metodika

Pro podrobný postup, checklisty a řešení problémů viz [UNIVERZALNI-NAVOD.md](UNIVERZALNI-NAVOD.md).
