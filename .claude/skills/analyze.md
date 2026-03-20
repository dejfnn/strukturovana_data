---
description: "Analýza webu klienta pro strukturovaná data JSON-LD. Použij když uživatel zadá URL webu, chce začít nový projekt strukturovaných dat, nebo řekne 'analyzuj web'. Vstup: URL webu (povinné), volitelně odkaz na sitemap nebo příklady typových stránek."
---

# /analyze — Analýza webu

## Vstup

- **Povinné:** URL webu klienta
- **Volitelné:**
  - Odkaz na sitemap.xml
  - Seznam typových stránek k analýze (vzorky URL)
  - Typy stránek na webu (např. produkty, kategorie, blog, FAQ...)

## Postup

### 0. Dotaz na typové stránky

Pokud uživatel **neposkytl** typy stránek ani vzorkové URL:
1. **Zeptej se:** "Jaké typy stránek web obsahuje? (např. produkty, kategorie, blog, služby, FAQ, pobočky...) Pokud nevíte, můžu to zjistit automaticky ze sitemap."
2. Pokud uživatel odpoví — použij jeho odpověď jako vodítko pro krok 4 (identifikace typů stránek). Stále proveď crawling/sitemap analýzu, ale zaměř se na potvrzení a doplnění uživatelem zadaných typů.
3. Pokud uživatel řekne, že neví — pokračuj s automatickou detekcí (krok 2+).

Pokud uživatel **poskytl** typy stránek nebo vzorkové URL v zadání — **neptat se znovu**, rovnou pokračuj.

### 1. Příprava projektu

1. Z URL odvoď název klienta (doména bez www a TLD, UPPERCASE)
   - `www.sico.cz` → `SICO`
   - `www.firma-example.cz` → `FIRMA-EXAMPLE`
2. Vytvoř adresář `OUTPUT/{KLIENT}/` (pokud neexistuje)
3. Přidej doménu klienta do `.claude/settings.local.json` → `permissions.allow`:
   ```
   WebFetch(domain:{doména-bez-protokolu})
   ```

### 2. Získání sitemap

Použij agenta `web-analyzer` pro crawlování webu.

**Pokud uživatel poskytl sitemap URL:**
- Stáhni a zparsuj sitemap

**Pokud uživatel neposkytl sitemap:**
1. Zkus `{URL}/robots.txt` — hledej `Sitemap:` direktivu
2. Zkus standardní umístění:
   - `{URL}/sitemap.xml`
   - `{URL}/sitemap_index.xml`
   - `{URL}/sitemap-index.xml`
   - `{URL}/post-sitemap.xml`
3. Pokud sitemap neexistuje nebo je nekvalitní → crawluj hlavní navigaci webu

### 3. Hodnocení kvality sitemap

Zhodnoť a zapiš do analýzy:
- **Kompletnost** — obsahuje všechny důležité stránky? Chybí celé sekce?
- **Struktura** — jsou URL logicky organizované? Existují sub-sitemapy?
- **Aktuálnost** — jsou přítomny `<lastmod>` data? Jsou reálná?
- **Výsledek** — kvalitní / částečně kvalitní / nekvalitní / chybí

Pokud je sitemap nekvalitní nebo chybí, doplň informace crawlingem navigace a hlavních stránek webu.

### 4. Identifikace typů stránek

Z URL patterns v sitemap a/nebo z crawlingu identifikuj všechny typy stránek:

| URL pattern | Pravděpodobný Schema.org typ |
|-------------|------------------------------|
| `/` (homepage) | Organization + WebSite |
| `/produkty/*`, `/product/*` | Product |
| `/kategorie/*`, `/category/*` | CollectionPage |
| `/blog/*`, `/clanky/*` | Article |
| `/sluzby/*`, `/services/*` | Service |
| `/o-nas`, `/about` | AboutPage (WebPage) |
| `/kontakt`, `/contact` | ContactPage (WebPage) |
| `/faq`, `/casto-kladene-dotazy` | FAQPage |
| `/pobocky/*`, `/branches/*` | LocalBusiness |
| `/kariera/*`, `/jobs/*` | JobPosting (WebPage) |

Všechny stránky kromě homepage → BreadcrumbList.

### 5. Sběr dat z vzorkových stránek

Pro každý identifikovaný typ stránky:
1. Vyber 1-3 reprezentativní URL
2. Stáhni stránku přes WebFetch
3. Extrahuj relevantní data (název, popis, ceny, kontakty, obrázky, datumy...)

Použij agenta `web-analyzer` pro paralelní zpracování více stránek.

### 6. Návrh ke schválení

Předlož uživateli přehlednou tabulku:

```markdown
## Identifikované typy stránek

| # | Typ stránky | Počet URL | Schema.org typ | Vzorová URL |
|---|-------------|-----------|----------------|-------------|
| 1 | Homepage | 1 | Organization + WebSite | https://... |
| 2 | Produkty | ~150 | Product + BreadcrumbList | https://... |
| 3 | Kategorie | 12 | CollectionPage + BreadcrumbList | https://... |
| ... | ... | ... | ... | ... |

**Chcete pokračovat s těmito vzorky, nebo upravit výběr?**
```

**ČEKEJ NA SCHVÁLENÍ uživatelem. Nepokračuj dál bez explicitního souhlasu.**

## Výstupní soubor

Zapiš výsledky do `OUTPUT/{KLIENT}/analyza-webu.md`:

```markdown
# Analýza webu: {Název klienta}

**URL:** {url}
**Datum analýzy:** {YYYY-MM-DD}
**Typ webu:** E-commerce / Služby / Blog / Firemní prezentace / ...
**CMS:** WordPress / Shoptet / Custom / ...

## Hodnocení sitemap

- **Zdroj:** {URL sitemap nebo "crawling navigace"}
- **Kvalita:** {kvalitní / částečně kvalitní / nekvalitní / chybí}
- **Počet URL v sitemap:** {číslo}
- **Poznámky:** {co chybí, co je špatně}

## Identifikované typy stránek

### 1. Homepage
- **URL:** https://...
- **Schema.org typy:** Organization, WebSite
- **Priorita:** KRITICKÁ
- **Sebraná data:**
  - Název firmy: ...
  - Logo: ...
  - Kontaktní údaje: ...
  - Sociální sítě: ...

### 2. Produkty
- **Vzorová URL:** https://...
- **Schema.org typy:** Product, Offer, BreadcrumbList
- **Priorita:** VYSOKÁ
- **Počet stránek:** ~{číslo}
- **Sebraná data:**
  - Název: ...
  - Cena: ...
  - Dostupnost: ...
  - Obrázky: ...

### 3. ...
(pokračuje pro každý typ)

## Doporučení

- {co implementovat jako první}
- {specifická doporučení pro tento web}
```
