# Strukturovaná data JSON-LD pro SICO RENT

## Návod k validaci

1. **Google Rich Results Test**: Otevřete https://search.google.com/test/rich-results, vložte JSON-LD kód nebo URL stránky
2. **Schema.org Validator**: Otevřete https://validator.schema.org/, vložte JSON-LD kód

**DŮLEŽITÉ**: V JSON-LD kódu níže jsou **vytučněné hodnoty** reálná data ze stránek SICO. Při kopírování odstraňte hvězdičky (\*\*) - jsou tam jen pro vizuální zvýraznění.

---

## HOMEPAGE

### URL STRÁNKY
https://www.sico.cz/

### Organization Schema

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://www.sico.cz/#organization",
  "name": "**SICO RENT s.r.o.**",
  "url": "**https://www.sico.cz**",
  "logo": {
    "@type": "ImageObject",
    "url": "**https://www.sico.cz/wp-content/themes/sico/images/logo.svg**",
    "width": "**250**",
    "height": "**60**"
  },
  "description": "**Specialista na pronájem pracovních plošin s více než 20 lety na trhu. 600 strojů ihned k dispozici, nejširší sortiment v ČR.**",
  "email": "**sico@sico.cz**",
  "telephone": "**+420724204100**",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "**Jenštejn**",
    "addressRegion": "**Praha**",
    "addressCountry": "**CZ**"
  },
  "contactPoint": [
    {
      "@type": "ContactPoint",
      "telephone": "**+420724204100**",
      "contactType": "**Pronájem**",
      "areaServed": "**CZ**",
      "availableLanguage": ["**cs**", "**en**", "**de**"]
    },
    {
      "@type": "ContactPoint",
      "telephone": "**+420602205951**",
      "contactType": "**Dispečink**",
      "areaServed": "**CZ**",
      "availableLanguage": ["**cs**"]
    }
  ],
  "sameAs": [
    "**https://www.facebook.com/sico.cz**",
    "**https://www.instagram.com/sico_rent_pracovni_plosiny/**",
    "**https://www.youtube.com/channel/UCnpcIYojppT48ea2pzVaqlg**",
    "**https://www.linkedin.com/company/sico-rent**"
  ]
}
```

### WebSite Schema (s SearchAction)

```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "@id": "https://www.sico.cz/#website",
  "url": "**https://www.sico.cz**",
  "name": "**SICO RENT - Pronájem pracovních plošin**",
  "description": "**Pronájem pracovních plošin, vysokozdvižných vozíků, manipulátorů a dalších pracovních zařízení**",
  "publisher": {
    "@id": "https://www.sico.cz/#organization"
  },
  "inLanguage": ["**cs-CZ**", "**en-GB**", "**de-DE**"],
  "potentialAction": {
    "@type": "SearchAction",
    "target": {
      "@type": "EntryPoint",
      "urlTemplate": "**https://www.sico.cz/?s={search_term_string}**"
    },
    "query-input": "required name=search_term_string"
  }
}
```

---

## KATEGORIE PRODUKTŮ

### URL STRÁNKY
https://www.sico.cz/kategorie/nuzkove/

### CollectionPage + ItemList + BreadcrumbList Schema (kombinované)

**Best Practice**: Pro kategorie použijte `CollectionPage` s `mainEntity` odkazujícím na `ItemList`. Tato struktura může aktivovat carousel rich results v Google.

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "CollectionPage",
      "@id": "https://www.sico.cz/kategorie/nuzkove/#collectionpage",
      "url": "**https://www.sico.cz/kategorie/nuzkove/**",
      "name": "**Pronájem Nůžkových Pracovních Plošin**",
      "description": "**Nůžkové plošiny vhodné především pro vnitřní práce na pevném, rovném podkladu. Dieselové varianty s pohonem všech kol a hydraulickými opěrami zvládají obtížný terén. Typické využití: rekonstrukce, stavby, montáže a práce ve skladech.**",
      "about": {
        "@type": "Product",
        "name": "**Nůžkové pracovní plošiny**"
      },
      "publisher": {
        "@id": "https://www.sico.cz/#organization"
      },
      "breadcrumb": {
        "@id": "https://www.sico.cz/kategorie/nuzkove/#breadcrumb"
      },
      "mainEntity": {
        "@type": "ItemList",
        "itemListOrder": "https://schema.org/ItemListUnordered",
        "numberOfItems": **31**,
        "itemListElement": [
          {
            "@type": "ListItem",
            "position": 1,
            "name": "**Haulotte Optimum 6**",
            "url": "**https://www.sico.cz/plosiny/optimum-6/**"
          },
          {
            "@type": "ListItem",
            "position": 2,
            "name": "**Genie GS 6**",
            "url": "**https://www.sico.cz/plosiny/gs-6/**"
          },
          {
            "@type": "ListItem",
            "position": 3,
            "name": "**Haulotte Compact 12**",
            "url": "**https://www.sico.cz/plosiny/haulotte-compact-12/**"
          }
        ]
      }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://www.sico.cz/kategorie/nuzkove/#breadcrumb",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "**Úvod**",
          "item": "**https://www.sico.cz/**"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "**Pronájem**",
          "item": "**https://www.sico.cz/pronajem/**"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "**Nůžkové pracovní plošiny**",
          "item": "**https://www.sico.cz/kategorie/nuzkove/**"
        }
      ]
    }
  ]
}
```

---

## PRODUKTOVÁ STRÁNKA

### URL STRÁNKY
https://www.sico.cz/plosiny/optimum-6/

### Product Schema

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "@id": "https://www.sico.cz/plosiny/optimum-6/#product",
  "name": "**Haulotte Optimum 6**",
  "description": "**Kompaktní, manévrovatelná nůžková plošina určená pro uzavřené prostory. Šířka průchodu 0,76 metru umožňuje průchod standardními dveřmi a poloměr otáčení 1,5 metru zajišťuje výjimečnou pohyblivost v těsných prostorách.**",
  "brand": {
    "@type": "Brand",
    "name": "**Haulotte**"
  },
  "manufacturer": {
    "@type": "Organization",
    "name": "**Haulotte**"
  },
  "image": [
    "**https://www.sico.cz/wp-content/uploads/optimum-6-01.jpg**",
    "**https://www.sico.cz/wp-content/uploads/optimum-6-02.jpg**",
    "**https://www.sico.cz/wp-content/uploads/optimum-6-03.jpg**",
    "**https://www.sico.cz/wp-content/uploads/optimum-6-04.jpg**"
  ],
  "category": "**Nůžkové plošiny**",
  "offers": {
    "@type": "Offer",
    "url": "**https://www.sico.cz/plosiny/optimum-6/**",
    "priceCurrency": "**CZK**",
    "price": "**1200**",
    "priceSpecification": {
      "@type": "UnitPriceSpecification",
      "price": "**1200**",
      "priceCurrency": "**CZK**",
      "unitText": "**den**"
    },
    "availability": "https://schema.org/InStock",
    "seller": {
      "@id": "https://www.sico.cz/#organization"
    },
    "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut"
  },
  "additionalProperty": [
    {
      "@type": "PropertyValue",
      "name": "**Pracovní výška**",
      "value": "**6,45 m**"
    },
    {
      "@type": "PropertyValue",
      "name": "**Nosnost plošiny**",
      "value": "**280 kg**"
    },
    {
      "@type": "PropertyValue",
      "name": "**Rozměry plošiny**",
      "value": "**1,65 m (2,57 m rozšířená) × 0,7 m**"
    },
    {
      "@type": "PropertyValue",
      "name": "**Hmotnost stroje**",
      "value": "**1 335 kg**"
    },
    {
      "@type": "PropertyValue",
      "name": "**Šířka průjezdu**",
      "value": "**0,76 m**"
    },
    {
      "@type": "PropertyValue",
      "name": "**Výška průjezdu**",
      "value": "**1,91 m**"
    },
    {
      "@type": "PropertyValue",
      "name": "**Výdrž baterie**",
      "value": "**až 10 hodin**"
    },
    {
      "@type": "PropertyValue",
      "name": "**Typ pohonu**",
      "value": "**Akumulátorový**"
    },
    {
      "@type": "PropertyValue",
      "name": "**Terén**",
      "value": "**Pevný, rovný povrch (interiér/exteriér)**"
    }
  ],
  "audience": {
    "@type": "PeopleAudience",
    "audienceType": "**Stavební firmy, montážní firmy, sklady**"
  }
}
```

### BreadcrumbList Schema

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "@id": "https://www.sico.cz/plosiny/optimum-6/#breadcrumb",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "**Úvod**",
      "item": "**https://www.sico.cz/**"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "**Pronájem**",
      "item": "**https://www.sico.cz/pronajem/**"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "**Pracovní plošiny**",
      "item": "**https://www.sico.cz/pronajem/pracovni-plosiny/**"
    },
    {
      "@type": "ListItem",
      "position": 4,
      "name": "**Haulotte Optimum 6**",
      "item": "**https://www.sico.cz/plosiny/optimum-6/**"
    }
  ]
}
```

### Service Schema (Doplňkové služby)

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "**Pronájem pracovních plošin s kompletním servisem**",
  "provider": {
    "@id": "https://www.sico.cz/#organization"
  },
  "areaServed": {
    "@type": "Country",
    "name": "**Česká republika**"
  },
  "offers": {
    "@type": "Offer",
    "priceCurrency": "**CZK**",
    "availability": "https://schema.org/InStock"
  },
  "termsOfService": "**https://www.sico.cz/obchodni-podminky/**",
  "additionalType": "RentalService",
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "**Služby zahrnuté v pronájmu**",
    "itemListElement": [
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "**Dálková diagnostika**",
          "description": "**Vzdálený monitoring a diagnostika strojů**"
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "**Školení obsluhy**",
          "description": "**Profesionální školení pro obsluhu pracovních plošin**"
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "**Mobilní servisní jednotka**",
          "description": "**Výjezd servisního týmu k zákazníkovi**"
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "**Asistence obsluhy**",
          "description": "**Odborná pomoc při obsluze strojů**"
        }
      }
    ]
  }
}
```

---

## ZAJÍMAVOSTI / RADCE (Článek)

### URL STRÁNKY
https://www.sico.cz/autoplosina-man-tgl-palfinger-p300ks-na-pontonu/

### Article Schema

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "@id": "https://www.sico.cz/autoplosina-man-tgl-palfinger-p300ks-na-pontonu/#article",
  "headline": "**Autoplošina MAN TGL Palfinger P300KS na pontonu pod Čechovým mostem**",
  "description": "**Autoplošina MAN TGL Palfinger P300KS se podílela na údržbě konstrukce Čechova mostu. Zařízení bylo umístěno na speciální ponton pro dosažení obtížně přístupných míst nad Vltavou.**",
  "image": [
    "**https://www.sico.cz/wp-content/uploads/2025/09/SICO-RENT-zajimavosti-man-tgl-palfinger-p300ks-cechuv-most-01.jpg**",
    "**https://www.sico.cz/wp-content/uploads/2025/09/SICO-RENT-zajimavosti-man-tgl-palfinger-p300ks-cechuv-most-02.jpg**",
    "**https://www.sico.cz/wp-content/uploads/2025/09/SICO-RENT-zajimavosti-man-tgl-palfinger-p300ks-cechuv-most-03.jpg**"
  ],
  "author": {
    "@type": "Organization",
    "@id": "https://www.sico.cz/#organization"
  },
  "publisher": {
    "@type": "Organization",
    "@id": "https://www.sico.cz/#organization",
    "name": "**SICO RENT s.r.o.**",
    "logo": {
      "@type": "ImageObject",
      "url": "**https://www.sico.cz/wp-content/themes/sico/images/logo.svg**"
    }
  },
  "datePublished": "**2025-09-15**",
  "dateModified": "**2025-09-15**",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://www.sico.cz/autoplosina-man-tgl-palfinger-p300ks-na-pontonu/"
  },
  "articleSection": "**Zajímavá místa**",
  "keywords": ["**autoplošina**", "**Palfinger P300KS**", "**Čechův most**", "**pracovní plošiny**", "**údržba mostů**"],
  "about": [
    {
      "@type": "Thing",
      "name": "**Čechův most**",
      "description": "**Most postavený v letech 1905–1908, nejkratší most přes Vltavu v Praze**"
    },
    {
      "@type": "Product",
      "name": "**Autoplošina MAN TGL Palfinger P300KS**",
      "description": "**Pracovní výška 30 metrů, dosah přes 20 metrů, stranový dosah až 20,5 metru**"
    }
  ],
  "mentions": [
    {
      "@type": "Place",
      "name": "**Čechův most**",
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": "**50.0925**",
        "longitude": "**14.4181**"
      }
    }
  ]
}
```

### BreadcrumbList Schema

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "@id": "https://www.sico.cz/autoplosina-man-tgl-palfinger-p300ks-na-pontonu/#breadcrumb",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "**Úvod**",
      "item": "**https://www.sico.cz/**"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "**Zajímavosti**",
      "item": "**https://www.sico.cz/radce-sico-rent/**"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "**Autoplošina MAN TGL Palfinger P300KS na pontonu**",
      "item": "**https://www.sico.cz/autoplosina-man-tgl-palfinger-p300ks-na-pontonu/**"
    }
  ]
}
```

---

## ZAJÍMAVOSTI / RADCE (Hlavní stránka sekce)

### URL STRÁNKY
https://www.sico.cz/radce-sico-rent/

### Blog Schema

```json
{
  "@context": "https://schema.org",
  "@type": "Blog",
  "@id": "https://www.sico.cz/radce-sico-rent/#blog",
  "url": "**https://www.sico.cz/radce-sico-rent/**",
  "name": "**SICO RENT - Zajímavosti**",
  "description": "**Novinky, zajímavá místa, reference a případové studie použití pronajímané techniky**",
  "publisher": {
    "@id": "https://www.sico.cz/#organization"
  },
  "inLanguage": "**cs-CZ**",
  "blogPost": [
    {
      "@type": "BlogPosting",
      "headline": "**SICO RENT se stává součástí STATECH s.r.o.**",
      "url": "**https://www.sico.cz/sico-rent-s-r-o-se-stava-soucasti-statech-s-r-o/**"
    },
    {
      "@type": "BlogPosting",
      "headline": "**Autoplošina MAN TGL na pontonu pod Čechovým mostem**",
      "url": "**https://www.sico.cz/autoplosina-man-tgl-palfinger-p300ks-na-pontonu/**"
    },
    {
      "@type": "BlogPosting",
      "headline": "**Kostel sv. Mikuláše a autoplošina SOCAGE 75TJJ**",
      "url": "**https://www.sico.cz/kostel-sv-mikulase-v-chebu-a-autoplosina-socage/**"
    }
  ]
}
```

### ItemList Schema (Seznam článků)

```json
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "@id": "https://www.sico.cz/radce-sico-rent/#itemlist",
  "name": "**Články a zajímavosti SICO RENT**",
  "description": "**98 článků o novinkách, zajímavých místech a referencích**",
  "numberOfItems": **98**,
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "item": {
        "@type": "Article",
        "name": "**SICO RENT se stává součástí STATECH s.r.o.**",
        "url": "**https://www.sico.cz/sico-rent-s-r-o-se-stava-soucasti-statech-s-r-o/**"
      }
    },
    {
      "@type": "ListItem",
      "position": 2,
      "item": {
        "@type": "Article",
        "name": "**Autoplošina MAN TGL na pontonu pod Čechovým mostem**",
        "url": "**https://www.sico.cz/autoplosina-man-tgl-palfinger-p300ks-na-pontonu/**"
      }
    },
    {
      "@type": "ListItem",
      "position": 3,
      "item": {
        "@type": "Article",
        "name": "**Kostel sv. Mikuláše a autoplošina SOCAGE 75TJJ**",
        "url": "**https://www.sico.cz/kostel-sv-mikulase-v-chebu-a-autoplosina-socage/**"
      }
    }
  ]
}
```

---

## POZNÁMKY K IMPLEMENTACI

### 1. Kombinace více schémat na jedné stránce
Na jedné stránce můžete kombinovat více schémat pomocí `@graph`:

```json
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
    },
    {
      "@type": "BreadcrumbList",
      ...
    }
  ]
}
```

### 2. Jak implementovat na web
Vložte JSON-LD do `<head>` nebo na konec `<body>` před `</body>`:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Product",
  ...
}
</script>
```

**DŮLEŽITÉ**: Při kopírování JSON-LD kódu **odstraňte hvězdičky (\*\*)** - jsou tam jen pro vizuální zvýraznění v této dokumentaci!

### 3. Časté chyby k vyvarování se
- **Chybějící povinné pole**: Některé typy vyžadují konkrétní pole (např. Product vyžaduje `name`, `image`, `offers`)
- **Neplatné URL**: Všechny URL musí být absolutní (začínat `http://` nebo `https://`)
- **Chybějící @id**: Pokud odkazujete na jiný objekt, použijte `@id` pro propojení
- **Špatný formát data**: Používejte ISO 8601 formát (YYYY-MM-DD)

### 4. Doporučení pro SICO RENT
1. **Homepage**: Implementujte Organization + WebSite schema
2. **Kategorie**: Implementujte CollectionPage + BreadcrumbList + ItemList
3. **Produkty**: Implementujte Product + Offer + BreadcrumbList + Service
4. **Články**: Implementujte Article + BreadcrumbList
5. **Sekce Zajímavosti**: Implementujte Blog + ItemList

### 5. Kontrolní seznam po implementaci
- [ ] Validovat všechna schémata v https://validator.schema.org/
- [ ] Otestovat v https://search.google.com/test/rich-results
- [ ] Zkontrolovat v Google Search Console (sekce Vylepšení)
- [ ] Otestovat mobilní zobrazení rich results
- [ ] Monitorovat výskyt rich snippets ve vyhledávání (může trvat 2-4 týdny)

---

## DODATEČNÉ TYPY PRO ROZŠÍŘENÍ

### FAQPage (pokud máte FAQ sekci)
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "**Jaká je minimální doba pronájmu?**",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "**Minimální doba pronájmu je 1 den.**"
      }
    }
  ]
}
```

### VideoObject (pokud máte videa)
```json
{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "**Jak používat nůžkovou plošinu**",
  "description": "**Instruktážní video pro bezpečné používání nůžkových plošin**",
  "thumbnailUrl": "**https://www.sico.cz/video-thumbnail.jpg**",
  "uploadDate": "**2025-01-15**",
  "duration": "**PT5M30S**",
  "contentUrl": "**https://www.youtube.com/watch?v=...**"
}
```

### HowTo (návody)
```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "**Jak správně používat pracovní plošinu**",
  "description": "**Bezpečnostní postupy pro práci s pracovními plošinami**",
  "step": [
    {
      "@type": "HowToStep",
      "name": "**Kontrola stroje**",
      "text": "**Před použitím zkontrolujte stav stroje...**"
    }
  ]
}
```

---

## VALIDACE - OČEKÁVANÉ VÝSLEDKY

### Google Rich Results Test
- **Organization**: Žádné chyby, správně rozpoznaná firma
- **WebSite**: Vyhledávací pole v rich results
- **Product**: Zobrazení ceny, dostupnosti a hodnocení (pokud jsou)
- **Article**: Rich snippet s obrázkem a datem publikace
- **BreadcrumbList**: Navigační drobečková cesta ve výsledcích

### Schema.org Validator
- Všechna schémata by měla projít bez chyb
- Případná varování jsou obvykle doporučení, ne kritické chyby
- Zkontrolujte, že všechny reference (@id) jsou správně propojené

---

**Datum vytvoření**: 2025-11-12
**Autor**: Claude Code
**Verze**: 1.0
