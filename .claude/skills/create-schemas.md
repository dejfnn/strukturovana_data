---
description: "Tvorba strukturovaných dat JSON-LD pro klientský web. Použij po /audit, nebo když uživatel chce vytvořit/přepracovat JSON-LD schémata. Vyžaduje hotovou analýzu a revizi v adresáři klienta."
---

# /create-schemas — Tvorba strukturovaných dat

## Vstup

- **Povinné:** Adresář klienta `OUTPUT/{KLIENT}/` s:
  - `analyza-webu.md` (data ze stránek)
  - `revize-stavajicich-dat.md` (stav existující implementace)
- Pokud chybí, upozorni a doporuč nejdřív `/analyze` a `/audit`

## Postup

### 1. Načtení kontextu

1. Přečti `analyza-webu.md` — data sebraná z webu
2. Přečti `revize-stavajicich-dat.md` — co existuje, co chybí, co opravit
3. Přečti relevantní šablony z `SABLONY/`

### 2. Výběr šablon podle typů stránek

| Typ stránky | Šablony k použití |
|-------------|-------------------|
| Homepage | `organization.json` + `website.json` + `breadcrumb.json` |
| Produkty | `product.json` + `breadcrumb.json` |
| Kategorie | `collection-page.json` + `breadcrumb.json` |
| Články | `article.json` + `breadcrumb.json` |
| FAQ | `faq-page.json` + `breadcrumb.json` |
| Pobočky | `local-business.json` + `breadcrumb.json` |
| Služby | `service.json` + `breadcrumb.json` |

### 3. Tvorba schémat

Pro každý typ stránky:

1. **Načti šablonu** z `SABLONY/`
2. **Vyplň reálnými daty** z `analyza-webu.md`
   - Nahraď všechny `{{PLACEHOLDER}}` skutečnými hodnotami
   - Odstraň pole, pro která nemáš data (neponechávej prázdné placeholdery)
3. **Kombinuj schémata** pro stejnou stránku pomocí `@graph`
4. **Provázej přes @id** — nikdy neduplikuj celé schéma
5. **Dodržuj @id konvenci:**
   ```
   {BASE_URL}/#organization
   {BASE_URL}/#website
   {PAGE_URL}/#breadcrumb
   {PAGE_URL}/#product
   {PAGE_URL}/#article
   {PAGE_URL}/#webpage
   ```

### 4. Dodržuj JSON-LD standardy

- `@context`: vždy `https://schema.org`
- URL: vždy absolutní
- Ceny: `"price": "1200", "priceCurrency": "CZK"`
- Datumy: ISO 8601 (`2025-09-15`)
- Telefony: s předvolbou (`+420...`)
- Reference: přes `@id`, nikdy duplikace

### 5. Vytvoření testovacích JSON souborů

Pro každý typ stránky vytvoř samostatný `test-{typ}.json`:

```
test-homepage.json          — Organization + WebSite (@graph)
test-product.json           — Product + BreadcrumbList (@graph)
test-category.json          — CollectionPage + BreadcrumbList (@graph)
test-article.json           — Article + BreadcrumbList (@graph)
test-faqpage.json           — FAQPage + BreadcrumbList (@graph)
test-localbusiness.json     — LocalBusiness
test-contact.json           — ContactPage + BreadcrumbList (@graph)
```

Každý test soubor musí být validní JSON a obsahovat kompletní schéma pro jednu vzorkovou stránku.

### 6. Průběžná validace

Po vytvoření každého test-*.json:
```bash
python NASTROJE/validate_schema.py OUTPUT/{KLIENT}/test-{typ}.json
```

Oprav všechny chyby okamžitě, nepokračuj s chybným schématem.

## Výstupní soubory

### Hlavní dokument: `strukturovana-data-{klient-lowercase}.md`

```markdown
# Strukturovaná data JSON-LD pro {Název klienta}

**URL:** {base_url}
**Datum vytvoření:** {YYYY-MM-DD}
**Verze:** 1.0

---

## HOMEPAGE

### URL stránky
{homepage_url}

### Implementovaná schémata
- Organization
- WebSite
- BreadcrumbList

### JSON-LD kód

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "{base_url}/#organization",
      ...
    },
    {
      "@type": "WebSite",
      "@id": "{base_url}/#website",
      ...
    }
  ]
}
```

### Poznámky k implementaci
- {specifické poznámky pro tento typ stránky}

---

## PRODUKTOVÉ STRÁNKY

### URL vzor
{base_url}/produkt/{slug}/

### Implementovaná schémata
- Product + Offer
- BreadcrumbList

### Dynamická pole
| Pole | Zdroj dat | Poznámka |
|------|-----------|----------|
| name | `<h1>` | Název produktu |
| price | element s cenou | Jen číslo |
| image | hlavní obrázek | Absolutní URL |
| ... | ... | ... |

### JSON-LD kód (vzor)

```json
{kompletní JSON-LD pro vzorkový produkt}
```

---

(pokračuje pro každý typ stránky)

---

## VALIDACE

### Výsledky lokální validace

| Soubor | Status | Chyby | Varování |
|--------|--------|-------|----------|
| test-homepage.json | ✓ | 0 | 0 |
| test-product.json | ✓ | 0 | 0 |
| ... | ... | ... | ... |

---

## IMPLEMENTAČNÍ POZNÁMKY

### Priorita implementace
1. **KRITICKÁ:** Homepage (Organization + WebSite)
2. **KRITICKÁ:** BreadcrumbList (všechny stránky)
3. **VYSOKÁ:** {dle specifik klienta}
4. ...

### Dynamické vs. statické hodnoty
- **Statické** (stejné na všech stránkách): Organization, WebSite
- **Dynamické** (mění se per stránka): Product, Article, BreadcrumbList

### Jak vkládat do HTML
```html
<script type="application/ld+json">
{JSON-LD kód}
</script>
```
Vložit do `<head>` nebo před `</body>`.
```

### Testovací soubory: `test-*.json`

Každý soubor = validní JSON-LD pro jednu vzorkovou stránku, připravený k testování v online validátorech.

## Přechod na další krok

Po dokončení doporuč uživateli pokračovat s `/validate` pro důkladnou validaci a pak `/document` pro finální dokumentaci.
