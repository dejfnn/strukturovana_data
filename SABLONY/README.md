# Šablony JSON-LD schémat

Tato složka obsahuje **univerzální šablony** pro nejčastější typy strukturovaných dat podle Schema.org.

## Dostupné šablony

| Soubor | Typ schématu | Použití |
|--------|--------------|---------|
| `organization.json` | Organization | Základní informace o firmě (homepage) |
| `website.json` | WebSite | Informace o webu + vyhledávání (homepage) |
| `product.json` | Product | Produktové stránky, e-shop |
| `article.json` | Article | Články, blog posty, novinky |
| `breadcrumb.json` | BreadcrumbList | Navigační drobečková cesta (všechny stránky) |
| `collection-page.json` | CollectionPage | Kategorie produktů/služeb |
| `faq-page.json` | FAQPage | FAQ sekce |
| `local-business.json` | LocalBusiness | Pobočky, prodejny s otevírací dobou |
| `service.json` | Service | Služby s ceníkem |

## Jak používat šablony

### Krok 1: Zkopírujte šablonu

```bash
cp SABLONY/organization.json muj-projekt/
```

### Krok 2: Nahraďte placeholdery

Všechny placeholdery jsou ve formátu `{{NAZEV}}`. Např.:

```json
{
  "name": "{{COMPANY_NAME}}",
  "url": "{{BASE_URL}}"
}
```

Nahraďte reálnými údaji:

```json
{
  "name": "Moje Firma s.r.o.",
  "url": "https://example.com"
}
```

### Krok 3: Validujte

```bash
python validate_schema.py organization.json
```

## Popis placeholderů

### Společné pro všechny šablony

- `{{BASE_URL}}` - Základní URL webu (např. `https://example.com`)
- `{{COMPANY_NAME}}` - Název firmy
- `{{LOGO_URL}}` - URL loga firmy

### Organization

- `{{DESCRIPTION}}` - Popis činnosti firmy
- `{{EMAIL}}` - Email
- `{{PHONE}}` - Telefon (formát: `+420123456789`)
- `{{STREET}}` - Ulice a číslo popisné
- `{{CITY}}` - Město
- `{{REGION}}` - Kraj/region
- `{{ZIP}}` - PSČ
- `{{COUNTRY_CODE}}` - Kód země (např. `CZ`, `SK`)
- `{{CONTACT_TYPE}}` - Typ kontaktu (např. `customer service`, `sales`)
- `{{LANGUAGE}}` - Jazyk (např. `cs`, `en`)
- `{{FACEBOOK_URL}}` - URL Facebook profilu
- `{{INSTAGRAM_URL}}` - URL Instagram profilu
- `{{LINKEDIN_URL}}` - URL LinkedIn profilu
- `{{YOUTUBE_URL}}` - URL YouTube kanálu
- `{{LOGO_WIDTH}}` - Šířka loga v px
- `{{LOGO_HEIGHT}}` - Výška loga v px

### WebSite

- `{{SITE_NAME}}` - Název webu
- `{{LANGUAGE_CODE}}` - Kód jazyka (např. `cs-CZ`, `en-US`)

### Product

- `{{PRODUCT_URL}}` - URL produktu
- `{{PRODUCT_NAME}}` - Název produktu
- `{{BRAND_NAME}}` - Značka produktu
- `{{MANUFACTURER_NAME}}` - Výrobce
- `{{CATEGORY}}` - Kategorie produktu
- `{{CURRENCY}}` - Měna (např. `CZK`, `EUR`)
- `{{PRICE}}` - Cena (pouze číslo, např. `1200`)
- `{{UNIT}}` - Jednotka ceny (např. `den`, `ks`, `měsíc`)
- `{{IMAGE_URL_1}}`, `{{IMAGE_URL_2}}`, ... - URL obrázků
- `{{PROPERTY_NAME_1}}`, `{{PROPERTY_VALUE_1}}` - Technické parametry

### Article

- `{{ARTICLE_URL}}` - URL článku
- `{{HEADLINE}}` - Nadpis článku
- `{{DATE_PUBLISHED}}` - Datum publikace (formát: `YYYY-MM-DD`)
- `{{DATE_MODIFIED}}` - Datum poslední úpravy (formát: `YYYY-MM-DD`)
- `{{SECTION}}` - Sekce/kategorie článku
- `{{KEYWORD_1}}`, `{{KEYWORD_2}}`, ... - Klíčová slova

### BreadcrumbList

- `{{PAGE_URL}}` - URL aktuální stránky
- `{{LEVEL_1_NAME}}`, `{{LEVEL_1_URL}}` - První úroveň (obvykle "Úvod")
- `{{LEVEL_2_NAME}}`, `{{LEVEL_2_URL}}` - Druhá úroveň
- `{{LEVEL_3_NAME}}`, `{{LEVEL_3_URL}}` - Třetí úroveň

### CollectionPage (s ItemList - best practice)

**Best Practice**: Pro kategorie použijte `CollectionPage` s `mainEntity` odkazujícím na `ItemList`. Tato struktura může aktivovat carousel rich results v Google.

- `{{CATEGORY_URL}}` - URL kategorie
- `{{CATEGORY_NAME}}` - Název kategorie
- `{{DESCRIPTION}}` - Popis kategorie
- `{{NUMBER_OF_ITEMS}}` - Počet položek v kategorii
- `{{ITEM_NAME_1}}`, `{{ITEM_URL_1}}` - První položka (název a URL)
- `{{ITEM_NAME_2}}`, `{{ITEM_URL_2}}` - Druhá položka
- `{{ITEM_NAME_3}}`, `{{ITEM_URL_3}}` - Třetí položka (přidejte další dle potřeby)

### FAQPage

- `{{PAGE_URL}}` - URL stránky s FAQ
- `{{QUESTION_1}}`, `{{ANSWER_1}}` - První otázka a odpověď
- `{{QUESTION_2}}`, `{{ANSWER_2}}` - Druhá otázka a odpověď
- atd.

### LocalBusiness

- `{{BRANCH_NAME}}` - Název pobočky
- `{{BRANCH_SLUG}}` - URL slug pobočky
- `{{BRANCH_URL}}` - Kompletní URL pobočky
- `{{BRANCH_DESCRIPTION}}` - Popis pobočky
- `{{LATITUDE}}`, `{{LONGITUDE}}` - GPS souřadnice
- `{{WEEKDAY_OPENS}}`, `{{WEEKDAY_CLOSES}}` - Otevírací doba v týdnu (formát: `09:00`)
- `{{FRIDAY_OPENS}}`, `{{FRIDAY_CLOSES}}` - Otevírací doba v pátek
- `{{SATURDAY_OPENS}}`, `{{SATURDAY_CLOSES}}` - Otevírací doba v sobotu
- `{{PRICE_RANGE}}` - Cenová kategorie (např. `$$`, `$$$`)
- `{{PAYMENT_METHODS}}` - Přijímané platby (např. `Cash, Credit Card`)

### Service

- `{{SERVICE_NAME}}` - Název služby
- `{{SERVICE_URL}}` - URL stránky služby
- `{{SERVICE_DESCRIPTION}}` - Popis služby
- `{{SERVICE_TYPE}}` - Typ služby
- `{{OFFER_NAME_1}}`, `{{OFFER_DESCRIPTION_1}}`, `{{PRICE_1}}` - Položka ceníku
- `{{CATALOG_NAME}}` - Název ceníku
- `{{TERMS_URL}}` - URL obchodních podmínek
- `{{RATING_VALUE}}`, `{{REVIEW_COUNT}}` - Hodnocení služby

## Příklad použití

### Před (šablona):

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "{{COMPANY_NAME}}",
  "url": "{{BASE_URL}}",
  "telephone": "{{PHONE}}"
}
```

### Po (vyplněno):

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "SICO RENT s.r.o.",
  "url": "https://www.sico.cz",
  "telephone": "+420724204100"
}
```

## Kombinace schémat pomocí @graph

Pro kombinaci více schémat na jedné stránce:

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
    }
  ]
}
```

## Tipy

1. **Vždy validujte** po vyplnění šablony
2. **Používejte absolutní URL** (začínající `https://`)
3. **Propojujte schémata** pomocí `@id` reference
4. **Datum ve formátu ISO 8601** (YYYY-MM-DD)
5. **Cena jako číslo** (bez měny v poli price)

## Validace

Po vyplnění šablony validujte:

```bash
# Lokální validace
python ../NASTROJE/validate_schema.py moje-schema.json

# Online validace
# 1. https://validator.schema.org/
# 2. https://search.google.com/test/rich-results
```

## Další zdroje

- [Schema.org Documentation](https://schema.org/docs/documents.html)
- [Google Structured Data Guidelines](https://developers.google.com/search/docs/appearance/structured-data)
- [UNIVERZALNI-NAVOD.md](../UNIVERZALNI-NAVOD.md) - Kompletní návod k použití
