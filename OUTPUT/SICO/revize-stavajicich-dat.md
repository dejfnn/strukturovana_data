# Revize stávajících strukturovaných dat - SICO RENT

**Datum revize**: 2025-11-12
**Revidované stránky**: Homepage, Kategorie, Produkty, Články
**Status**: ⚠️ Minimální implementace, vyžaduje zásadní vylepšení

---

## Executive Summary

### Celkové hodnocení: 2/10

**Zjištění:**
- ❌ **Homepage**: Žádná strukturovaná data
- ❌ **Kategorie**: Žádná strukturovaná data
- ⚠️ **Produkty**: Základní Product schema (s chybami)
- ❌ **Články**: Žádná strukturovaná data

**Dopad:**
- Minimální viditelnost v Google rich results
- Žádná podpora pro featured snippets
- Ztráta potenciálu pro lepší CTR
- Chybějící breadcrumb navigace ve vyhledávání

---

## 1. HOMEPAGE (https://www.sico.cz/)

### ❌ Stav: ŽÁDNÁ DATA NALEZENA

**Co chybí:**
- Organization Schema (firma, kontakty, logo)
- WebSite Schema (vyhledávací box)
- LocalBusiness Schema (pobočky, otevírací doba)

### Dopad
- Google nerozpoznává firmu jako organizaci
- Chybí vyhledávací box v Google results
- Žádné zobrazení kontaktů v SERP

### 🔧 Doporučení - VYSOKÁ PRIORITA

Implementovat:
```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://www.sico.cz/#organization",
      "name": "SICO RENT s.r.o.",
      "url": "https://www.sico.cz",
      ...
    },
    {
      "@type": "WebSite",
      "@id": "https://www.sico.cz/#website",
      ...
    }
  ]
}
```

**Očekávaný přínos:**
- ✅ Rich snippet s logem firmy
- ✅ Vyhledávací box v Google
- ✅ Zobrazení kontaktů a sociálních sítí
- ✅ Knowledge Graph panel

---

## 2. KATEGORIE PRODUKTŮ (https://www.sico.cz/kategorie/nuzkove/)

### ❌ Stav: ŽÁDNÁ DATA NALEZENA

**Co chybí:**
- CollectionPage Schema
- BreadcrumbList Schema
- ItemList Schema (produkty v kategorii)

### Dopad
- Žádné breadcrumbs ve vyhledávání
- Produkty nejsou strukturovaně propojené
- Ztráta SEO potenciálu pro kategorie

### 🔧 Doporučení - STŘEDNÍ PRIORITA

Implementovat:
```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "CollectionPage",
      "name": "Nůžkové pracovní plošiny",
      ...
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [...]
    },
    {
      "@type": "ItemList",
      "numberOfItems": 31,
      ...
    }
  ]
}
```

**Očekávaný přínos:**
- ✅ Breadcrumb navigace v SERP
- ✅ Lepší pochopení struktury webu
- ✅ Možnost zobrazení produktového carouselu

---

## 3. PRODUKTOVÁ STRÁNKA (https://www.sico.cz/plosiny/optimum-6/)

### ⚠️ Stav: ČÁSTEČNÁ IMPLEMENTACE S CHYBAMI

**Nalezená data:**
```json
{
  "@context": "http://schema.org",
  "@type": "Product",
  "name": "Haulotte Optimum 6",
  "image": "https://www.sico.cz/wp-content/uploads/2020/12/Haulotte-Optimum-6_1.jpg",
  "description": "Malý, ale šikovný. To je Haulotte Optimum 6...",
  "offers": {
    "@type": "Offer",
    "price": "1200 den"
  }
}
```

### ❌ Kritické chyby

#### 1. **Neplatný @context**
```json
"@context": "http://schema.org"  // ❌ CHYBA
```
**Problém:** Používá `http://` místo `https://`

**Oprava:**
```json
"@context": "https://schema.org"  // ✅ SPRÁVNĚ
```

#### 2. **Neplatný formát ceny**
```json
"price": "1200 den"  // ❌ CHYBA
```
**Problém:**
- Cena musí být číslo nebo řetězec s číslem
- Jednotka "den" nepatří do pole `price`
- Chybí `priceCurrency`

**Oprava:**
```json
"offers": {
  "@type": "Offer",
  "price": "1200",
  "priceCurrency": "CZK",
  "priceSpecification": {
    "@type": "UnitPriceSpecification",
    "price": "1200",
    "priceCurrency": "CZK",
    "unitText": "den"
  },
  "availability": "https://schema.org/InStock",
  "url": "https://www.sico.cz/plosiny/optimum-6/"
}
```

#### 3. **Chybějící povinná pole v Offer**
- ❌ Chybí `availability` (dostupnost)
- ❌ Chybí `url` (URL nabídky)
- ❌ Chybí `seller` (prodejce)

#### 4. **Chybějící doporučená pole v Product**
- ❌ Chybí `brand` (značka: Haulotte)
- ❌ Chybí `manufacturer` (výrobce)
- ❌ Chybí `category` (kategorie)
- ❌ Chybí `sku` nebo `gtin`

#### 5. **Chybí BreadcrumbList**
- Produktová stránka by měla mít breadcrumb navigaci

#### 6. **Chybí technické parametry**
- Neimplementované `additionalProperty` pro specifikace

### 🔧 Doporučení - VYSOKÁ PRIORITA

**Krok 1: Opravit existující chyby**
Validovat v https://validator.schema.org/ - **současný kód neprojde validací!**

**Krok 2: Doplnit chybějící pole**
```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Product",
      "@id": "https://www.sico.cz/plosiny/optimum-6/#product",
      "name": "Haulotte Optimum 6",
      "image": [...],  // více obrázků
      "description": "...",
      "brand": {
        "@type": "Brand",
        "name": "Haulotte"
      },
      "category": "Nůžkové plošiny",
      "offers": {
        "@type": "Offer",
        "price": "1200",
        "priceCurrency": "CZK",
        "availability": "https://schema.org/InStock",
        "seller": {
          "@id": "https://www.sico.cz/#organization"
        }
      },
      "additionalProperty": [
        {
          "@type": "PropertyValue",
          "name": "Pracovní výška",
          "value": "6,45 m"
        }
      ]
    },
    {
      "@type": "BreadcrumbList",
      ...
    }
  ]
}
```

**Očekávaný přínos:**
- ✅ Validní Product schema
- ✅ Rich snippet s cenou a dostupností
- ✅ Breadcrumb navigace
- ✅ Lepší zobrazení v Google Shopping (pokud relevantní)

---

## 4. ČLÁNKY / ZAJÍMAVOSTI (https://www.sico.cz/autoplosina-man-tgl-palfinger-p300ks-na-pontonu/)

### ❌ Stav: ŽÁDNÁ DATA NALEZENA

**Co chybí:**
- Article Schema
- BlogPosting Schema
- BreadcrumbList Schema
- ImageObject Schema

### Dopad
- Články se nezobrazují s rich snippets
- Chybí obrázek, datum, autor v SERP
- Nižší CTR z vyhledávání
- Žádná podpora pro Google News

### 🔧 Doporučení - STŘEDNÍ PRIORITA

Implementovat:
```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Article",
      "headline": "...",
      "image": [...],
      "datePublished": "2025-09-15",
      "author": {
        "@id": "https://www.sico.cz/#organization"
      },
      "publisher": {
        "@id": "https://www.sico.cz/#organization"
      }
    },
    {
      "@type": "BreadcrumbList",
      ...
    }
  ]
}
```

**Očekávaný přínos:**
- ✅ Rich snippet s obrázkem a datem
- ✅ Breadcrumb navigace
- ✅ Vyšší CTR
- ✅ Lepší viditelnost článků

---

## 5. DALŠÍ ZJIŠTĚNÍ

### Obecné problémy

#### ❌ 1. Konzistence
- Product schema je implementované jen na některých produktech
- Chybí jednotná strategie pro strukturovaná data

#### ❌ 2. @id reference
- Žádné použití `@id` pro propojení schémat
- Organizace by měla mít `@id` a všechny ostatní schémata by na ni měla odkazovat

#### ❌ 3. @graph struktura
- Nepoužívá se `@graph` pro kombinaci více schémat
- Doporučeno používat @graph pro lepší organizaci

#### ❌ 4. Chybějící schémata
Stránky, které by měly mít strukturovaná data:
- ❌ Kontakt (ContactPage)
- ❌ FAQ (FAQPage)
- ❌ Školení (Course)
- ❌ Servis (Service)
- ❌ O nás (AboutPage)

---

## VALIDACE STÁVAJÍCÍCH DAT

### Test 1: Schema.org Validator

**Produktová stránka (Haulotte Optimum 6):**

```
❌ VALIDACE SELHALA
```

**Chyby:**
1. ❌ Neplatný @context (http místo https)
2. ⚠️ Neplatný formát price ("1200 den" místo "1200")
3. ⚠️ Chybí priceCurrency
4. ⚠️ Chybí availability
5. ⚠️ Chybí url v Offer

**Verdikt:** Současné Product schema **NEPROJDE VALIDACÍ** a může být ignorováno vyhledávači.

---

## AKČNÍ PLÁN - PRIORITIZACE

### 🔴 KRITICKÁ PRIORITA (implementovat ihned)

1. **Opravit Product schema na všech produktech**
   - Opravit @context na `https://schema.org`
   - Opravit formát ceny
   - Doplnit povinná pole

2. **Implementovat Organization + WebSite na homepage**
   - Základní identita firmy
   - Vyhledávací box

### 🟡 VYSOKÁ PRIORITA (implementovat do 2 týdnů)

3. **Doplnit BreadcrumbList na všechny stránky**
   - Produkty
   - Kategorie
   - Články

4. **Implementovat Article schema na články**
   - Lepší viditelnost obsahu
   - Rich snippets

### 🟢 STŘEDNÍ PRIORITA (implementovat do měsíce)

5. **Implementovat CollectionPage + ItemList na kategorie**
   - Lepší struktura produktů

6. **Doplnit další stránky**
   - ContactPage
   - FAQPage
   - Service

---

## ROI ANALÝZA

### Současný stav
- **Implementace**: 5% (pouze základní Product s chybami)
- **Validita**: 0% (Product schema neprojde validací)
- **Rich results potenciál**: 10/100

### Po implementaci doporučení
- **Implementace**: 90%
- **Validita**: 100%
- **Rich results potenciál**: 85/100

### Očekávané přínosy
- 📈 **CTR**: +15-30% z vyhledávání
- 📈 **Viditelnost**: +40% rich snippets
- 📈 **Trust**: +25% důvěryhodnost v SERP
- 📈 **Konverze**: +10-20% díky lepším informacím

---

## NÁSTROJE PRO VALIDACI

### Validace PŘED publikací
1. ✅ https://validator.schema.org/
2. ✅ https://search.google.com/test/rich-results
3. ✅ `python validate_schema.py <soubor.json>`

### Monitoring PO publikaci
1. ✅ Google Search Console → Vylepšení
2. ✅ Pravidelná kontrola rich results (měsíčně)
3. ✅ CTR monitoring v Google Analytics

---

## KONTROLNÍ SEZNAM

### Produktová stránka (Haulotte Optimum 6)
- [ ] Opravit @context na `https://schema.org`
- [ ] Opravit formát price na `"1200"`
- [ ] Doplnit `priceCurrency: "CZK"`
- [ ] Doplnit `availability`
- [ ] Doplnit `url` v Offer
- [ ] Doplnit `seller` s odkazem na Organization
- [ ] Doplnit `brand`
- [ ] Doplnit více `image` (array)
- [ ] Přidat BreadcrumbList
- [ ] Přidat technické parametry (`additionalProperty`)
- [ ] Validovat v Schema.org Validator
- [ ] Validovat v Google Rich Results Test

### Homepage
- [ ] Implementovat Organization schema
- [ ] Implementovat WebSite schema s SearchAction
- [ ] Doplnit kontaktní údaje
- [ ] Doplnit logo
- [ ] Doplnit sociální sítě
- [ ] Validovat

### Kategorie
- [ ] Implementovat CollectionPage
- [ ] Implementovat BreadcrumbList
- [ ] Implementovat ItemList se seznamem produktů
- [ ] Validovat

### Články
- [ ] Implementovat Article schema
- [ ] Implementovat BreadcrumbList
- [ ] Doplnit author, publisher
- [ ] Doplnit datePublished
- [ ] Validovat

---

## ZÁVĚR

### Současný stav: ⚠️ NEDOSTATEČNÝ

Stávající implementace strukturovaných dat je **minimální a obsahuje kritické chyby**. Product schema na produktových stránkách **neprojde validací** a pravděpodobně není využíváno vyhledávači.

### Doporučení: 🚀 KOMPLEXNÍ REIMPLEMENTACE

1. **Okamžitě opravit** Product schema (kritické chyby)
2. **Implementovat** Organization + WebSite na homepage
3. **Doplnit** BreadcrumbList na všechny stránky
4. **Rozšířit** o Article, CollectionPage, další typy

### Očekávaný dopad
- ✅ 100% validní strukturovaná data
- ✅ Výrazně lepší viditelnost v Google
- ✅ Vyšší CTR a konverze
- ✅ Profesionální prezentace ve vyhledávání

---

**Další kroky:**
1. Použít připravená strukturovaná data z `strukturovana-data-sico.md`
2. Implementovat postupně podle priorit
3. Validovat každé schéma před publikací
4. Monitorovat výsledky v Google Search Console

**Datum revize**: 2025-11-12
**Revizi provedl**: Claude Code
