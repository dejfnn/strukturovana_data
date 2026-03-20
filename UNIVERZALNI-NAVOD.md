# Univerzální návod: Analýza a tvorba strukturovaných dat JSON-LD

**Verze**: 1.0
**Datum**: 2025-11-12
**Autor**: Claude Code

---

## 📋 Obsah

1. [Úvod](#úvod)
2. [Příprava na projekt](#příprava-na-projekt)
3. [Krok 1: Analýza webu](#krok-1-analýza-webu)
4. [Krok 2: Revize stávajících dat](#krok-2-revize-stávajících-dat)
5. [Krok 3: Tvorba strukturovaných dat](#krok-3-tvorba-strukturovaných-dat)
6. [Krok 4: Validace](#krok-4-validace)
7. [Krok 5: Dokumentace](#krok-5-dokumentace)
8. [Checklisty](#checklisty)
9. [Časté problémy](#časté-problémy)

---

## Úvod

Tento dokument poskytuje **univerzální postup** pro analýzu webových stránek a tvorbu strukturovaných dat ve formátu JSON-LD podle Schema.org standardu.

### Co budete vytvářet

Pro každého klienta vytvoříte:
- ✅ Analýzu typů stránek na webu
- ✅ Revizi stávajících strukturovaných dat
- ✅ Nová strukturovaná data připravená k implementaci
- ✅ Validační skripty a testovací data
- ✅ Kompletní dokumentaci

### Struktura projektu

```
Strukturovana_data/
├── UNIVERZALNI-NAVOD.md          ← Tento dokument
├── SABLONY/                       ← Šablony pro různé typy schémat
│   ├── organization-template.json
│   ├── product-template.json
│   ├── article-template.json
│   └── ...
├── NASTROJE/                      ← Univerzální validační nástroje
│   ├── validate_schema.py
│   └── md_to_html.py
└── [NAZEV-KLIENTA]/              ← Složka pro konkrétního klienta
    ├── strukturovana-data.md
    ├── revize-stavajicich-dat.md
    ├── README.md
    ├── test-*.json
    └── *.html
```

---

## Příprava na projekt

### 1. Informace od klienta

Před začátkem projektu získejte:

```
✓ URL webu klienta
✓ Přístup k webu (pokud je potřeba)
✓ Priority (které stránky jsou nejdůležitější)
✓ Cílové audience
✓ Konkurenční weby (pro inspiraci)
✓ Existující SEO strategie
```

### 2. Vytvoření projektové složky

Všechny projekty se ukládají do složky `OUTPUT/` pojmenované podle domény klienta (velkými písmeny):

```bash
cd Strukturovana_data/OUTPUT
mkdir NAZEV-DOMENY
cd NAZEV-DOMENY
```

**Příklady názvů složek:**
- `www.sico.cz` → `OUTPUT/SICO/`
- `www.firma-example.cz` → `OUTPUT/FIRMA-EXAMPLE/`

**Struktura projektové složky:**
```
OUTPUT/NAZEV-DOMENY/
├── analyza-webu.md              ← Analýza struktury webu (Krok 1)
├── revize-stavajicich-dat.md    ← Revize stávajících dat (Krok 2)
├── strukturovana-data-*.md      ← Hotová strukturovaná data (Krok 3)
├── README.md                    ← Dokumentace pro klienta (Krok 5)
├── test-*.json                  ← Testovací soubory (Krok 4)
└── *.html                       ← HTML verze pro Word (volitelné)
```

### 3. Inicializace projektu

Vytvořte základní poznámky:
- Název projektu
- Datum zahájení
- URL webu
- Klíčové cíle

---

## Krok 1: Analýza webu

### 1.0 Rychlá analýza struktury webu (NOVÝ VYLEPŠENÝ POSTUP)

Před manuálním procházením webu použijte automatizovanou analýzu struktury:

#### Krok 1: Načtěte robots.txt
```
https://domena.cz/robots.txt
```

Robots.txt často obsahuje:
- Odkaz na sitemapu (`Sitemap:`)
- Strukturu webu (blokované/povolené cesty)
- Informace o sekcích webu

#### Krok 2: Načtěte sitemapu
Obvyklé umístění:
- `https://domena.cz/sitemap.xml`
- `https://domena.cz/sitemap_index.xml`
- URL uvedená v robots.txt

Sitemap poskytuje:
- Kompletní seznam URL na webu
- Kategorizaci stránek (často v separátních sitemapách)
- Datum poslední změny stránek

#### Krok 3: Analyzujte URL patterns
Ze sitemapy identifikujte vzory URL:

| URL pattern | Pravděpodobný typ |
|-------------|-------------------|
| `/produkty/*` nebo `/product/*` | Product |
| `/kategorie/*` nebo `/category/*` | CollectionPage |
| `/blog/*` nebo `/clanky/*` | Article |
| `/sluzby/*` nebo `/services/*` | Service |
| `/o-nas`, `/about` | AboutPage |
| `/kontakt`, `/contact` | ContactPage |
| `/faq`, `/casto-kladene-dotazy` | FAQPage |

#### Krok 4: Vyberte reprezentativní URL
Pro každý identifikovaný typ vyberte 1-3 příklady k detailní analýze.

**Příklad dotazu pro Claude Code:**
```markdown
"Analyzuj strukturu webu https://example.com:
1. Načti robots.txt
2. Najdi a načti sitemapu
3. Identifikuj URL patterns a typy stránek
4. Vytvoř přehled typových stránek s příklady URL"
```

---

### 1.1 Identifikace typových stránek

Po automatické analýze ověřte a doplňte hlavní typy stránek:

**Standardní typy:**
- [ ] **Homepage** - Úvodní stránka
- [ ] **Kategorie** - Seznamy produktů/služeb/článků
- [ ] **Produkty/Služby** - Detailní stránky nabídky
- [ ] **Články/Blog** - Obsahové stránky
- [ ] **Kontakt** - Kontaktní informace
- [ ] **O nás** - Informace o společnosti
- [ ] **FAQ** - Často kladené otázky

**Specializované typy:**
- [ ] **Události** - Kalendář akcí
- [ ] **Recenze** - Hodnocení produktů
- [ ] **Video** - Video obsah
- [ ] **Vzdělávací kurzy**
- [ ] **Lokální pobočky**
- [ ] **Pracovní nabídky**

### 1.2 Sběr informací

Pro každý typ stránky zjistěte:

#### Homepage
```
✓ Název firmy
✓ Logo URL
✓ Popis činnosti
✓ Kontaktní údaje (telefon, email, adresa)
✓ Sociální sítě (Facebook, Instagram, LinkedIn, atd.)
✓ Otevírací doba (pokud relevantní)
✓ IČO, DIČ (pokud dostupné)
```

#### Kategorie
```
✓ Název kategorie
✓ Popis kategorie
✓ Seznam položek v kategorii
✓ Breadcrumb navigace
✓ Počet položek
```

#### Produkty/Služby
```
✓ Název produktu/služby
✓ Popis
✓ Cena (různé varianty: den, týden, měsíc)
✓ Dostupnost
✓ Výrobce/značka
✓ Obrázky (URL)
✓ Technické parametry
✓ SKU/GTIN (pokud dostupné)
```

#### Články
```
✓ Název článku
✓ Datum publikace
✓ Autor
✓ Kategorie/tagy
✓ Hlavní obrázek
✓ Shrnutí obsahu
```

### 1.3 Metoda sběru dat

**Použijte WebFetch nástroj:**

```markdown
Příklad dotazu pro Claude Code:

"Prosím, extrahuj následující informace z homepage https://example.com:
1. Název firmy a popis činnosti
2. Kontaktní údaje
3. Sociální sítě
4. Logo URL
5. Jakékoliv další relevantní informace pro strukturovaná data"
```

**Pro každý typ stránky vytvořte minimálně 1-3 příklady:**
- Homepage: 1 URL
- Kategorie: 2-3 různé kategorie
- Produkty: 3-5 produktů
- Články: 2-3 články

### 1.4 Dokumentace zjištění

Vytvořte dokument `analyza-webu.md`:

```markdown
# Analýza webu: [Název klienta]

## Základní informace
- URL: https://example.com
- Typ webu: E-commerce / Blog / Služby / ...
- CMS: WordPress / Custom / ...

## Identifikované typy stránek

### 1. Homepage
URL: https://example.com/
- Organization data: ...

### 2. Kategorie
Příklad: https://example.com/kategorie/produkty/
- Typ: CollectionPage
- Počet položek: 50

### 3. Produkty
Příklad: https://example.com/produkt/nazev/
- Typ: Product
- Cena: 1200 CZK
- Dostupnost: skladem
```

---

## Krok 2: Revize stávajících dat

### 2.0 Paralelní extrakce JSON-LD (VYLEPŠENÝ POSTUP)

Pro efektivitu extrahujte JSON-LD ze všech typových stránek **najednou** v jednom dotazu:

**Příklad dotazu pro Claude Code:**
```markdown
"Extrahuj strukturovaná data JSON-LD z těchto stránek paralelně:

1. Homepage: https://example.com/
2. Kategorie: https://example.com/kategorie/produkty/
3. Produkt: https://example.com/produkt/nazev/
4. Článek: https://example.com/blog/clanek/

Pro každou stránku:
- Najdi všechny <script type="application/ld+json"> bloky
- Vypiš kompletní JSON-LD kód
- Pokud žádná data nejsou, uveď 'Žádná JSON-LD data nenalezena'"
```

**Výhody paralelní extrakce:**
- Rychlejší než sekvenční kontrola
- Okamžitý přehled o stavu celého webu
- Snadné porovnání konzistence mezi stránkami

---

### 2.1 Extrakce stávajících strukturovaných dat

Pro **každý typ stránky** zkontrolujte stávající implementaci pomocí paralelní extrakce výše.

---

### 2.2 Vytvoření revizního dokumentu

Vytvořte `revize-stavajicich-dat.md` podle struktury ve vzorových projektech (`OUTPUT/SICO/revize-stavajicich-dat.md`).

**Povinné sekce:**

1. **Executive Summary** - rychlý přehled stavu
2. **Detailní rozbor** - pro každý typ stránky:
   - Status (✗ Žádná / ⚠ Částečná / ✓ Kompletní)
   - Nalezená data (JSON-LD kód)
   - Problémy a chyby
   - Doporučení s ukázkou opravy
3. **Validace** - výsledky testů
4. **Akční plán** - prioritizované kroky
5. **Kontrolní seznam** - checkboxy pro implementaci

---

### 2.3 Validace stávajících dat

Pokud existují strukturovaná data, validujte je:

1. **Schema.org Validator**: https://validator.schema.org/
2. **Google Rich Results Test**: https://search.google.com/test/rich-results
3. **Lokální validace**: `python validate_schema.py test.json`

**Dokumentujte výsledky:**

```markdown
## Validace

### Google Rich Results Test
- Status: ✓ Prošlo / ✗ Selhalo
- Chyby: [seznam chyb]
- Varování: [seznam varování]

### Schema.org Validator
- Status: ✓ Prošlo / ✗ Selhalo
- Chyby: [seznam chyb]
```

### 2.4 Analýza konkurence (volitelné)

Zkontrolujte 2-3 konkurenční weby:

```markdown
## Konkurenční analýza

### Konkurent 1 (https://competitor1.com)
- Homepage: ✓ Organization + WebSite
- Produkty: ✓ Product + Offer + AggregateRating
- Články: ✓ Article + BreadcrumbList

**Inspirace:**
- Používají AggregateRating pro hodnocení
- Implementovali FAQPage na produktech
```

---

## Krok 3: Tvorba strukturovaných dat

### 3.0 Workflow tvorby schémat (VYLEPŠENÝ POSTUP)

Pro efektivní tvorbu strukturovaných dat postupujte takto:

#### Krok 1: Použijte data z analýzy webu
Otevřete `analyza-webu.md` vytvořenou v Kroku 1. Obsahuje všechna potřebná data:
- Kontaktní údaje firmy
- URL a popisy kategorií
- Detaily produktů (ceny, parametry)
- Informace o článcích

#### Krok 2: Vyberte relevantní šablony
Na základě identifikovaných typových stránek vyberte šablony z `SABLONY/`:

| Typ stránky | Šablona |
|-------------|---------|
| Homepage | `organization.json` + `website.json` |
| Kategorie | `collection-page.json` + `breadcrumb.json` |
| Produkt | `product.json` + `breadcrumb.json` |
| Článek | `article.json` + `breadcrumb.json` |
| Pobočky | `local-business.json` |
| FAQ | `faq-page.json` |
| Služby | `service.json` |

#### Krok 3: Vyplňte šablony daty z analýzy
Nahraďte `{{PLACEHOLDERY}}` reálnými daty z `analyza-webu.md`.

#### Krok 4: Validujte každé schéma
```bash
python validate_schema.py test-schema.json
```

#### Krok 5: Vytvořte výstupní dokument
Zapište hotová schémata do `strukturovana-data-[klient].md`.

---

### 3.1 Prioritizace

Určete prioritu implementace:

**Kritická priorita:**
1. Organization (homepage)
2. WebSite s SearchAction (homepage)
3. BreadcrumbList (všechny stránky)

**Vysoká priorita:**
4. Product + Offer (produkty)
5. Article (články)
6. CollectionPage (kategorie)

**Střední priorita:**
7. LocalBusiness (pobočky)
8. FAQPage (FAQ sekce)
9. VideoObject (videa)
10. HowTo (návody)

### 3.2 Použití šablon

Pro každý typ schématu použijte připravenou šablonu z `SABLONY/`.

**Příklad: Organization**

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "{{BASE_URL}}/#organization",
  "name": "{{COMPANY_NAME}}",
  "url": "{{BASE_URL}}",
  "logo": {
    "@type": "ImageObject",
    "url": "{{LOGO_URL}}",
    "width": "{{LOGO_WIDTH}}",
    "height": "{{LOGO_HEIGHT}}"
  },
  "description": "{{DESCRIPTION}}",
  "email": "{{EMAIL}}",
  "telephone": "{{PHONE}}",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "{{CITY}}",
    "addressRegion": "{{REGION}}",
    "addressCountry": "{{COUNTRY_CODE}}"
  },
  "sameAs": [
    "{{FACEBOOK_URL}}",
    "{{INSTAGRAM_URL}}",
    "{{LINKEDIN_URL}}"
  ]
}
```

**Nahraďte placeholdery** reálnými daty:
- `{{BASE_URL}}` → `https://example.com`
- `{{COMPANY_NAME}}` → `Firma s.r.o.`
- atd.

### 3.3 Vytvoření hlavního dokumentu

Vytvořte `strukturovana-data.md`:

```markdown
# Strukturovaná data JSON-LD pro [Název klienta]

## HOMEPAGE

### URL STRÁNKY
https://example.com/

### Organization Schema

[JSON-LD kód]

### WebSite Schema

[JSON-LD kód]

---

## KATEGORIE PRODUKTŮ

### URL STRÁNKY
https://example.com/kategorie/nazev/

### CollectionPage Schema

[JSON-LD kód]

...
```

### 3.4 Důležité zásady

#### ✅ DO:
- Používejte `https://schema.org` (ne http)
- Používejte absolutní URL (ne relativní)
- Používejte `@id` pro propojení schémat
- Kombinujte schémata pomocí `@graph`
- Validujte každé schéma před finalizací
- Používejte ISO 8601 formát pro datumy (YYYY-MM-DD)

#### ❌ DON'T:
- Nepoužívejte placeholder hodnoty
- Nevkládejte nevalidní URL
- Nezapomínejte na povinná pole
- Nepoužívejte špatný formát ceny
- Nekombinujte různé verze schémat

### 3.5 Kombinace schémat pomocí @graph

Pro stránky s více schématy:

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://example.com/#organization",
      ...
    },
    {
      "@type": "WebSite",
      "@id": "https://example.com/#website",
      "publisher": {
        "@id": "https://example.com/#organization"
      },
      ...
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://example.com/page/#breadcrumb",
      ...
    }
  ]
}
```

---

## Krok 4: Validace

### 4.0 Hromadná validace (VYLEPŠENÝ POSTUP)

Validační skript podporuje hromadnou validaci více souborů najednou:

```bash
# Validace všech JSON souborů v projektu
python NASTROJE/validate_schema.py OUTPUT/SICO/*.json

# Validace souborů podle vzoru
python NASTROJE/validate_schema.py OUTPUT/SICO/test-*.json

# Validace více souborů najednou
python NASTROJE/validate_schema.py soubor1.json soubor2.json soubor3.json
```

**Příklad výstupu hromadné validace:**
```
======================================================================
SOUBOR: test-organization.json
======================================================================
1. JSON syntaxe: ✓ JSON syntaxe je platná
2. Validace schématu:
   ✓ Typ: Organization
   ✓ Schéma je validní

======================================================================
SOUBOR: test-product.json
======================================================================
1. JSON syntaxe: ✓ JSON syntaxe je platná
2. Validace schématu:
   ✓ Typ: Product
   ✓ Schéma je validní

======================================================================
SOUHRN VALIDACE
======================================================================
Celkem souborů:    2
Soubory s chybami: 0
Celkem chyb:       0
Celkem varování:   0

✅ Všechny soubory jsou validní!
```

**Co validátor kontroluje:**
1. ✓ JSON syntaxi
2. ✓ Povinná pole podle typu schématu (Organization, Product, Article, WebSite, BreadcrumbList, CollectionPage, LocalBusiness, Service, FAQPage)
3. ✓ Validitu URL adres (musí začínat http:// nebo https://)
4. ✓ Přítomnost @context (schema.org)
5. ⚠ Prázdné hodnoty a nevyplněné placeholdery (varování)

---

### 4.1 Příprava testovacích souborů

Pro každý typ schématu vytvořte testovací JSON soubor:

```
test-homepage-organization.json
test-product.json
test-article.json
test-category.json
...
```

### 4.2 Lokální validace

Použijte validační skript:

```bash
# Jeden soubor
python NASTROJE/validate_schema.py test-homepage-organization.json

# Všechny testovací soubory najednou
python NASTROJE/validate_schema.py test-*.json
```

**Očekávaný výstup:**
```
======================================================================
SOUBOR: test-homepage-organization.json
======================================================================

1. JSON syntaxe: ✓ JSON syntaxe je platná
2. Validace schématu:
   ✓ Typ: Organization
   ✓ Schéma je validní
```

**Pokud jsou varování o prázdných hodnotách:**
```
   ⚠ Varování:
     ⚠ Prázdný řetězec: description
     ⚠ Nevyplněný placeholder: telephone = {{PHONE}}
```

→ Opravte prázdné hodnoty nebo odstraňte nevyplněné placeholdery

### 4.3 Online validace

Pro každé schéma:

1. **Schema.org Validator** (https://validator.schema.org/)
   - Vložte JSON-LD kód
   - Klikněte "VALIDATE"
   - Zkontrolujte, že nejsou žádné chyby

2. **Google Rich Results Test** (https://search.google.com/test/rich-results)
   - Vložte JSON-LD kód nebo URL
   - Klikněte "TEST CODE" nebo "TEST URL"
   - Zkontrolujte výsledky

### 4.4 Dokumentace validace

V hlavním dokumentu doplňte sekci:

```markdown
## VALIDACE

### test-homepage-organization.json
- ✓ Lokální validace: Prošlo
- ✓ Schema.org: Prošlo
- ✓ Google Rich Results: Prošlo, detekován Organization

### test-product.json
- ✓ Lokální validace: Prošlo
- ✓ Schema.org: Prošlo
- ✓ Google Rich Results: Prošlo, detekován Product
```

---

## Krok 5: Dokumentace

### 5.1 Vytvoření README

Vytvořte `README.md` pro klienta:

```markdown
# Strukturovaná data JSON-LD pro [Název klienta]

## Vytvořené soubory

### 📄 Hlavní dokumentace
- **strukturovana-data.md** - Kompletní přehled strukturovaných dat

### 🔍 Revize
- **revize-stavajicich-dat.md** - Analýza současného stavu

### 🧪 Testovací soubory
- test-*.json - Validované příklady

## Jak implementovat

1. Otevřete `strukturovana-data.md`
2. Zkopírujte JSON-LD pro konkrétní typ stránky
3. Vložte do HTML jako:

```html
<script type="application/ld+json">
[JSON-LD kód zde]
</script>
```

4. Validujte pomocí:
   - https://validator.schema.org/
   - https://search.google.com/test/rich-results

## Priorita implementace

1. 🔴 KRITICKÁ: Homepage (Organization + WebSite)
2. 🟡 VYSOKÁ: Produkty (Product + Offer)
3. 🟢 STŘEDNÍ: Kategorie, Články

## Kontrolní seznam

- [ ] Homepage: Organization + WebSite
- [ ] Produkty: Product + BreadcrumbList
- [ ] Kategorie: CollectionPage + BreadcrumbList
- [ ] Články: Article + BreadcrumbList
- [ ] Validace všech schémat
- [ ] Monitoring v Google Search Console
```

### 5.2 Konverze do HTML/DOCX (POVINNÉ)

Na závěr každého projektu **vždy** převeďte MD soubory na HTML:

```bash
cd OUTPUT/NAZEV-DOMENY
python ../../NASTROJE/md_to_html.py
```

To automaticky vytvoří HTML verze všech MD souborů:
- `strukturovana-data-*.html`
- `revize-stavajicich-dat.html`
- `analyza-webu.html`
- `README.html`

**Proč HTML:**
- Klient může otevřít ve Wordu a uložit jako .docx
- Lepší formátování pro tisk
- Zachová JSON bloky s barevným zvýrazněním

### 5.3 Finální kontrola

Před předáním klientovi zkontrolujte:

- [ ] Všechny dokumenty jsou kompletní
- [ ] Všechna JSON-LD schémata jsou validní
- [ ] README obsahuje jasné instrukce
- [ ] Testovací soubory fungují
- [ ] Dokumentace je bez chyb a překlepů
- [ ] Prioritizace je jasná
- [ ] Kontaktní údaje jsou správné

---

## Checklisty

### Checklist: Analýza webu

```
□ Identifikovat všechny typové stránky
□ Získat data pro Homepage (Organization)
□ Získat data pro 2-3 kategorie
□ Získat data pro 3-5 produktů/služeb
□ Získat data pro 2-3 články
□ Zkontrolovat FAQ, Kontakt, O nás stránky
□ Vytvořit dokument analyza-webu.md
```

### Checklist: Revize stávajících dat

```
□ Zkontrolovat Homepage
□ Zkontrolovat Kategorie
□ Zkontrolovat Produkty
□ Zkontrolovat Články
□ Validovat stávající schémata
□ Identifikovat kritické chyby
□ Vytvořit dokument revize-stavajicich-dat.md
□ Prioritizovat problémy
```

### Checklist: Tvorba strukturovaných dat

```
□ Homepage: Organization + WebSite
□ Produkty: Product + Offer + BreadcrumbList
□ Kategorie: CollectionPage + BreadcrumbList + ItemList
□ Články: Article + BreadcrumbList
□ Kontakt: ContactPage (pokud relevantní)
□ FAQ: FAQPage (pokud relevantní)
□ Vytvořit testovací JSON soubory
□ Validovat všechna schémata
```

### Checklist: Validace

```
□ Lokální validace všech testovacích souborů
□ Schema.org Validator pro každé schéma
□ Google Rich Results Test pro každé schéma
□ Dokumentovat výsledky validace
□ Opravit všechny chyby
□ Ověřit, že nejsou žádná varování
```

### Checklist: Dokumentace

```
□ strukturovana-data.md je kompletní
□ revize-stavajicich-dat.md je kompletní
□ README.md obsahuje instrukce
□ Všechny testovací soubory jsou připraveny
□ HTML verze jsou vytvořeny (pokud požadováno)
□ Finální kontrola před předáním
```

---

## Časté problémy

### Problém 1: Neplatný @context

**Chyba:**
```json
"@context": "http://schema.org"  // ❌
```

**Oprava:**
```json
"@context": "https://schema.org"  // ✓
```

### Problém 2: Neplatný formát ceny

**Chyba:**
```json
"price": "1200 Kč"  // ❌
"price": "1,200"    // ❌
```

**Oprava:**
```json
"price": "1200",
"priceCurrency": "CZK"  // ✓
```

### Problém 3: Relativní URL

**Chyba:**
```json
"url": "/produkty/nazev"  // ❌
```

**Oprava:**
```json
"url": "https://example.com/produkty/nazev"  // ✓
```

### Problém 4: Chybějící povinná pole

**Product vyžaduje:**
- `@type`
- `name`
- `image`
- `offers` (nebo `review` nebo `aggregateRating`)

**Article vyžaduje:**
- `@type`
- `headline`
- `image`
- `datePublished`
- `author`

### Problém 5: Špatný formát data

**Chyba:**
```json
"datePublished": "15.9.2025"  // ❌
"datePublished": "09/15/2025"  // ❌
```

**Oprava:**
```json
"datePublished": "2025-09-15"  // ✓ ISO 8601
```

### Problém 6: Chybějící @id pro reference

**Špatně:**
```json
{
  "@type": "Product",
  "seller": {
    "@type": "Organization",
    "name": "Firma s.r.o."  // Duplikace dat
  }
}
```

**Správně:**
```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://example.com/#organization",
      "name": "Firma s.r.o."
    },
    {
      "@type": "Product",
      "seller": {
        "@id": "https://example.com/#organization"  // Reference
      }
    }
  ]
}
```

---

## Tipy a best practices

### 1. Začněte s prioritami

Neimplementujte všechno najednou. Začněte s:
1. Organization (identita firmy)
2. BreadcrumbList (navigace)
3. Product/Article (hlavní obsah)

### 2. Používejte @graph

Pro stránky s více schématy používejte `@graph` pro lepší organizaci.

### 3. Testujte průběžně

Nevalidujte až na konci. Validujte každé schéma hned po vytvoření.

### 4. Dokumentujte průběžně

Nepište dokumentaci až na konci. Průběžně zapisujte zjištění.

### 5. Používejte reference pomocí @id

Neopakujte data. Použijte `@id` pro propojení schémat.

### 6. Buďte konzistentní

Používejte stejnou strukturu `@id` na celém webu:
- `https://example.com/#organization`
- `https://example.com/page/#breadcrumb`
- `https://example.com/product/name/#product`

### 7. Sledujte výsledky

Po implementaci:
- Pravidelně kontrolujte Google Search Console
- Sledujte výskyt rich snippets
- Monitorujte CTR z vyhledávání

---

## Vzorový projekt

V této složce najdete **OUTPUT/SICO** jako vzorový vypracovaný projekt.

Podívejte se na:
- `OUTPUT/SICO/strukturovana-data-sico.md` - Jak má vypadat finální výstup
- `OUTPUT/SICO/revize-stavajicich-dat.md` - Jak má vypadat revize
- `OUTPUT/SICO/README.md` - Jak má vypadat dokumentace pro klienta
- `OUTPUT/SICO/test-*.json` - Jak mají vypadat testovací soubory

---

## Časový harmonogram

### Malý projekt (5-10 typových stránek)
- Analýza webu: 2-3 hodiny
- Revize stávajících dat: 1-2 hodiny
- Tvorba strukturovaných dat: 3-4 hodiny
- Validace: 1-2 hodiny
- Dokumentace: 1-2 hodiny
**Celkem: 8-13 hodin**

### Střední projekt (10-20 typových stránek)
- Analýza webu: 3-4 hodiny
- Revize stávajících dat: 2-3 hodiny
- Tvorba strukturovaných dat: 5-8 hodin
- Validace: 2-3 hodiny
- Dokumentace: 2-3 hodiny
**Celkem: 14-21 hodin**

### Velký projekt (20+ typových stránek)
- Analýza webu: 4-6 hodin
- Revize stávajících dat: 3-4 hodiny
- Tvorba strukturovaných dat: 8-12 hodin
- Validace: 3-4 hodiny
- Dokumentace: 3-4 hodiny
**Celkem: 21-30 hodin**

---

## Zdroje a nástroje

### Dokumentace
- [Schema.org Documentation](https://schema.org/docs/documents.html)
- [Google Search Central - Structured Data](https://developers.google.com/search/docs/appearance/structured-data)
- [JSON-LD Specification](https://json-ld.org/spec/latest/json-ld/)

### Validační nástroje
- [Schema.org Validator](https://validator.schema.org/)
- [Google Rich Results Test](https://search.google.com/test/rich-results)
- [Google Search Console](https://search.google.com/search-console)

### Užitečné odkazy
- [Schema.org Types](https://schema.org/docs/full.html)
- [Google's Structured Data Gallery](https://developers.google.com/search/docs/appearance/structured-data/search-gallery)

---

## Podpora

Pro dotazy a problémy:
- Schema.org GitHub: https://github.com/schemaorg/schemaorg/issues
- Google Search Central Community: https://support.google.com/webmasters/community

---

**Verze dokumentu**: 1.0
**Poslední aktualizace**: 2025-11-12
**Vytvořil**: Claude Code

---

## Quick Start

**Pro zahájení nového projektu:**

1. Vytvořte složku klienta:
   ```bash
   cd Strukturovana_data
   mkdir NAZEV-KLIENTA
   cd NAZEV-KLIENTA
   ```

2. Zkopírujte nástroje:
   ```bash
   cp ../NASTROJE/validate_schema.py .
   cp ../NASTROJE/md_to_html.py .
   ```

3. Začněte analýzou webu (Krok 1)

4. Postupujte podle kroků 1-5 v tomto návodu

5. Použijte checklisty pro kontrolu

6. Inspirujte se vzorovou složkou OUTPUT/SICO

**Úspěšný projekt!** 🚀
