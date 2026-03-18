# Strukturovaná data JSON-LD pro SICO RENT

## Vytvořené soubory

### 📄 Hlavní dokumentace
- **strukturovana-data-sico.md** - Kompletní přehled všech strukturovaných dat s reálnými údaji ze stránek SICO

### 🐍 Validační nástroj
- **validate_schema.py** - Python skript pro lokální validaci JSON-LD dat
- **test-homepage-organization.json** - Testovací soubor pro Organization schema
- **test-product.json** - Testovací soubor pro Product schema
- **test-article.json** - Testovací soubor pro Article schema

---

## 📋 Obsah strukturovana-data-sico.md

Dokument obsahuje strukturovaná data pro následující typy stránek:

### 1. **HOMEPAGE** (https://www.sico.cz/)
- ✓ Organization Schema
- ✓ WebSite Schema (s SearchAction)

### 2. **KATEGORIE PRODUKTŮ** (https://www.sico.cz/kategorie/nuzkove/)
- ✓ CollectionPage Schema
- ✓ BreadcrumbList Schema
- ✓ ItemList Schema (seznam produktů)

### 3. **PRODUKTOVÁ STRÁNKA** (https://www.sico.cz/plosiny/optimum-6/)
- ✓ Product Schema
- ✓ BreadcrumbList Schema
- ✓ Service Schema (doplňkové služby)

### 4. **ZAJÍMAVOSTI - ČLÁNEK** (https://www.sico.cz/autoplosina-man-tgl-palfinger-p300ks-na-pontonu/)
- ✓ Article Schema
- ✓ BreadcrumbList Schema

### 5. **ZAJÍMAVOSTI - HLAVNÍ STRÁNKA** (https://www.sico.cz/radce-sico-rent/)
- ✓ Blog Schema
- ✓ ItemList Schema (seznam článků)

---

## 🔍 Jak validovat strukturovaná data

### Metoda 1: Online validátory (DOPORUČENO)

#### Google Rich Results Test
1. Otevřete https://search.google.com/test/rich-results
2. Vložte JSON-LD kód nebo URL stránky
3. Klikněte na "Test URL" nebo "Test CODE"
4. Zkontrolujte výsledky a případné chyby/varování

#### Schema.org Validator
1. Otevřete https://validator.schema.org/
2. Vložte JSON-LD kód
3. Klikněte na "VALIDATE"
4. Zkontrolujte výsledky

### Metoda 2: Lokální validace pomocí Python skriptu

#### Instalace
Není potřeba žádná instalace - skript používá pouze standardní Python knihovny.

#### Použití
```bash
python validate_schema.py <cesta_k_json_souboru>
```

#### Příklady
```bash
# Validace Organization schema
python validate_schema.py test-homepage-organization.json

# Validace Product schema
python validate_schema.py test-product.json

# Validace Article schema
python validate_schema.py test-article.json
```

#### Co validuje?
- ✓ Základní JSON syntaxe
- ✓ Přítomnost povinných polí (@context, @type, name, url, atd.)
- ✓ Validita URL adres (musí začínat http:// nebo https://)
- ✓ Správnost @context (musí obsahovat schema.org)
- ✓ Podporu pro @graph strukturu

#### Omezení
⚠️ Tento skript provádí pouze **základní validaci**. Pro komplexní kontrolu použijte online validátory.

---

## 🚀 Jak implementovat na web

### 1. Vložení JSON-LD do HTML
Vložte JSON-LD do `<head>` sekce nebo na konec `<body>` před `</body>`:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "SICO RENT s.r.o.",
  ...
}
</script>
```

### 2. Kombinace více schémat
Pro kombinaci více schémat na jedné stránce použijte `@graph`:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      ...
    },
    {
      "@type": "WebSite",
      ...
    }
  ]
}
</script>
```

### 3. Propojení schémat pomocí @id
Pro propojení schémat použijte `@id` a reference:

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://www.sico.cz/#organization",
      "name": "SICO RENT s.r.o."
    },
    {
      "@type": "Product",
      "seller": {
        "@id": "https://www.sico.cz/#organization"
      }
    }
  ]
}
```

---

## ✅ Kontrolní seznam po implementaci

- [ ] Implementovat Organization + WebSite schema na homepage
- [ ] Implementovat CollectionPage + BreadcrumbList + ItemList na kategorie
- [ ] Implementovat Product + Offer + BreadcrumbList na produktové stránky
- [ ] Implementovat Article + BreadcrumbList na články
- [ ] Implementovat Blog + ItemList na hlavní stránku Zajímavostí
- [ ] Validovat všechna schémata v https://validator.schema.org/
- [ ] Otestovat v https://search.google.com/test/rich-results
- [ ] Zkontrolovat v Google Search Console (sekce Vylepšení)
- [ ] Otestovat mobilní zobrazení
- [ ] Monitorovat výskyt rich snippets ve vyhledávání (2-4 týdny)

---

## 📊 Očekávané výsledky

### Google Rich Results Test
- **Organization**: ✓ Správně rozpoznaná firma
- **WebSite**: ✓ Vyhledávací pole v rich results
- **Product**: ✓ Zobrazení ceny, dostupnosti
- **Article**: ✓ Rich snippet s obrázkem a datem
- **BreadcrumbList**: ✓ Navigační drobečková cesta

### Schema.org Validator
- ✓ Všechna schémata by měla projít bez chyb
- ⚠️ Případná varování jsou obvykle doporučení, ne kritické chyby

---

## 🔧 Řešení problémů

### Časté chyby

#### 1. Chybějící povinné pole
```
✗ Chybí povinné pole: image
```
**Řešení**: Přidejte chybějící pole do JSON-LD

#### 2. Neplatná URL
```
✗ Neplatná URL v logo.url: /images/logo.png
```
**Řešení**: Použijte absolutní URL: `https://www.sico.cz/images/logo.png`

#### 3. Chybný formát data
```
✗ Neplatný formát datePublished
```
**Řešení**: Použijte ISO 8601 formát: `2025-09-15`

#### 4. Chybějící @context
```
✗ Chybí @context
```
**Řešení**: Přidejte `"@context": "https://schema.org"`

---

## 📚 Dodatečné zdroje

### Dokumentace
- [Schema.org Documentation](https://schema.org/docs/documents.html)
- [Google Search Central - Structured Data](https://developers.google.com/search/docs/appearance/structured-data)
- [JSON-LD Specification](https://json-ld.org/spec/latest/json-ld/)

### Nástroje
- [Google Rich Results Test](https://search.google.com/test/rich-results)
- [Schema.org Validator](https://validator.schema.org/)
- [Google Search Console](https://search.google.com/search-console)

### Best Practices
- [Google's Structured Data Guidelines](https://developers.google.com/search/docs/appearance/structured-data/sd-policies)
- [Schema.org Best Practices](https://schema.org/docs/gs.html)

---

## 💡 Tipy pro SICO RENT

### Priorita implementace
1. **Homepage** - Organization + WebSite (nejvyšší priorita)
2. **Produktové stránky** - Product + Offer (vysoká priorita)
3. **Kategorie** - CollectionPage + ItemList (střední priorita)
4. **Články** - Article + Blog (střední priorita)

### Rozšířená funkčnost
- Přidejte **FAQPage** schema, pokud máte FAQ sekci
- Přidejte **VideoObject** schema pro instruktážní videa
- Přidejte **HowTo** schema pro návody k použití
- Zvažte přidání **Review** a **AggregateRating** pro hodnocení

### Monitoring
- Nastavte pravidelnou kontrolu v Google Search Console
- Sledujte CTR (Click-Through Rate) v Google Analytics
- Monitorujte výskyt rich snippets ve vyhledávání

---

## 📞 Podpora

Pro otázky ohledně strukturovaných dat:
- Google Search Central Help Community: https://support.google.com/webmasters/community
- Schema.org GitHub Issues: https://github.com/schemaorg/schemaorg/issues

---

**Datum vytvoření**: 2025-11-12
**Verze**: 1.0
**Autor**: Claude Code
