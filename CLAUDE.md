# Strukturovaná Data JSON-LD — Nástroj

Standardizovaný nástroj pro tvorbu, revizi a dokumentaci Schema.org strukturovaných dat (JSON-LD) pro klientské weby.

## Adresářová struktura

```
SABLONY/              → 9 univerzálních JSON-LD šablon (organization, website, product, article,
                        breadcrumb, collection-page, faq-page, local-business, service)
NASTROJE/             → Python nástroje
  validate_schema.py  → Validátor JSON-LD (podporuje hromadnou validaci)
  md_to_html.py       → Konvertor MD → HTML (pro Word kompatibilitu)
OUTPUT/{KLIENT}/      → Výstupní adresáře klientských projektů (UPPERCASE)
UNIVERZALNI-NAVOD.md  → Detailní referenční příručka (1000+ řádků)
requirements.txt      → Python závislosti (pip install -r requirements.txt)
```

## Workflow — 5 kroků

Každý krok = samostatný skill s jasným vstupem, výstupem a standardem.

| # | Skill | Co dělá | Výstup |
|---|-------|---------|--------|
| 1 | `/analyze` | Analýza webu — sitemap, typy stránek, vzorky | `analyza-webu.md` |
| 2 | `/audit` | Revize stávajících strukturovaných dat | `revize-stavajicich-dat.md` |
| 3 | `/create-schemas` | Tvorba JSON-LD podle šablon | `strukturovana-data-{klient}.md` + `test-*.json` |
| 4 | `/validate` | Validace všech schémat | Validační report (sekce v dokumentaci) |
| 5 | `/document` | README + HTML verze všech souborů | `README.md` + `*.html` |

### Schvalovací bod

Po kroku 1 (`/analyze`) se uživateli předloží:
- Seznam identifikovaných typů stránek
- Navržené vzorky URL pro každý typ
- Doporučené Schema.org typy

**Pokračuje se až po schválení uživatelem.**

### Nový vs. update projekt

Nástroj vždy provádí revizi (krok 2), i u nových projektů. Při updatu existující implementace se revize zaměří na porovnání se stávajícími schématy v OUTPUT/{KLIENT}/.

## Agenti

| Agent | Účel |
|-------|------|
| `web-analyzer` | Crawlování webu — sitemap, robots.txt, identifikace typů stránek, sběr dat |
| `schema-extractor` | Extrakce existujících JSON-LD z webových stránek, hodnocení kvality |

## Konvence

### Pojmenování souborů
- Adresář klienta: `OUTPUT/{KLIENT}/` — název z domény, UPPERCASE, bez TLD a www
  - `www.klenota.cz` → `OUTPUT/KLENOTA/`
  - `www.firma-example.cz` → `OUTPUT/FIRMA-EXAMPLE/`
- Analýza: `analyza-webu.md`
- Revize: `revize-stavajicich-dat.md`
- Hlavní výstup: `strukturovana-data-{klient-lowercase}.md`
- Testovací JSON: `test-{typ-stranky}.json`
- README: `README.md`
- HTML verze: automaticky generované z .md souborů

### JSON-LD standardy
- `@context` vždy `https://schema.org` (HTTPS, nikdy http)
- URL vždy absolutní (`https://example.com/page`, nikdy `/page`)
- Ceny: `"price": "1200", "priceCurrency": "CZK"` (nikdy `"1200 Kč"`)
- Datumy: ISO 8601 `2025-09-15` (nikdy `15.9.2025`)
- Provázání schémat přes `@id` reference (nikdy duplikace celého schématu)
- Více schémat na jedné stránce → `@graph`
- Placeholders v šablonách: `{{PLACEHOLDER}}`

### Priorita implementace Schema.org typů
1. **KRITICKÁ**: Organization + WebSite (homepage)
2. **KRITICKÁ**: BreadcrumbList (všechny stránky)
3. **VYSOKÁ**: Product/Offer (produktové stránky)
4. **VYSOKÁ**: Article (blog/obsah)
5. **STŘEDNÍ**: CollectionPage, LocalBusiness, FAQPage, Service

### @id konvence
```
https://example.com/#organization
https://example.com/#website
https://example.com/page/#breadcrumb
https://example.com/product/name/#product
https://example.com/page/#webpage
```

## Oprávnění

Při zahájení nového projektu se doména klienta automaticky přidá do `.claude/settings.local.json` jako `WebFetch(domain:{doména})`.

## Referenční projekty

- **KOVINTRADE** (`OUTPUT/KOVINTRADE/`) — nejkomplexnější, 16 souborů, 8+ typů stránek
- **SICO** (`OUTPUT/SICO/`) — čistý šablonový projekt, dobrý vzor struktury

## Detailní metodika

Pro edge cases, tipy a best practices viz `UNIVERZALNI-NAVOD.md`.
