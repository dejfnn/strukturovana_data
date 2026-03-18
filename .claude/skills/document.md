---
description: "Generování finální dokumentace a HTML verzí pro klienta. Použij po /validate jako poslední krok, nebo když uživatel chce vygenerovat README a HTML soubory pro klientský projekt strukturovaných dat."
---

# /document — Dokumentace a HTML export

## Vstup

- **Povinné:** Adresář klienta `OUTPUT/{KLIENT}/` s:
  - `analyza-webu.md`
  - `revize-stavajicich-dat.md`
  - `strukturovana-data-{klient}.md`
  - `test-*.json`
- Pokud chybí, upozorni a doporuč příslušný krok

## Postup

### 1. Vytvoření README.md

Přečti všechny existující soubory v adresáři klienta a vytvoř `README.md` podle šablony níže.

Inspiruj se vzorem z `OUTPUT/SICO/README.md`, ale přizpůsob obsah konkrétnímu klientovi.

### 2. Kontrola kompletnosti

Před generováním HTML ověř, že všechny .md soubory obsahují:
- Správné nadpisy a strukturu
- Validní JSON-LD bloky v code fences
- Kompletní tabulky a checklisty
- Žádné nevyplněné placeholdery

### 3. Generování HTML verzí

Spusť konverzi VŠECH .md souborů na HTML:

```bash
cd OUTPUT/{KLIENT} && python ../../NASTROJE/md_to_html.py
```

To vygeneruje:
- `analyza-webu.html`
- `revize-stavajicich-dat.html`
- `strukturovana-data-{klient}.html`
- `README.html`

### 4. Ověření HTML výstupů

Zkontroluj, že:
- Všechny .md soubory mají odpovídající .html
- HTML soubory nejsou prázdné
- JSON bloky jsou správně formátované v HTML

### 5. Finální kontrola celého projektu

Projdi celý adresář klienta a ověř:

- [ ] `analyza-webu.md` — kompletní analýza s identifikovanými typy stránek
- [ ] `revize-stavajicich-dat.md` — kompletní revize s hodnocením
- [ ] `strukturovana-data-{klient}.md` — všechna schémata s validačními výsledky
- [ ] `test-*.json` — validní testovací soubory pro každý typ stránky
- [ ] `README.md` — klientská dokumentace s instrukcemi
- [ ] `*.html` — HTML verze všech .md souborů
- [ ] Žádné nevyplněné placeholdery v žádném souboru
- [ ] Konzistentní URL, kontakty a názvy napříč soubory

## Šablona README.md

```markdown
# Strukturovaná data JSON-LD pro {Název klienta}

## Vytvořené soubory

### Hlavní dokumentace
- **strukturovana-data-{klient}.md** — Kompletní přehled všech strukturovaných dat s reálnými údaji
- **revize-stavajicich-dat.md** — Analýza současného stavu implementace
- **analyza-webu.md** — Analýza struktury webu a typů stránek

### Testovací soubory
{seznam test-*.json souborů s popisem}

### HTML verze (pro Word)
{seznam .html souborů}

---

## Obsah strukturovaných dat

{pro každý typ stránky:}

### {#}. {TYP STRÁNKY} ({vzorová URL})
- ✓ {Schema typ 1}
- ✓ {Schema typ 2}
- ✓ BreadcrumbList

---

## Jak implementovat na web

### 1. Vložení JSON-LD do HTML
Vložte JSON-LD do `<head>` sekce nebo před `</body>`:

```html
<script type="application/ld+json">
{JSON-LD kód}
</script>
```

### 2. Kombinace více schémat
Pro kombinaci více schémat na jedné stránce použijte `@graph` strukturu (viz hlavní dokument).

### 3. Propojení schémat
Schémata se propojují pomocí `@id` reference — nikdy nekopírujte celé schéma, odkazujte na `@id`.

---

## Jak validovat

### Online validátory (doporučeno)
1. **Google Rich Results Test:** https://search.google.com/test/rich-results
2. **Schema.org Validator:** https://validator.schema.org/

### Lokální validace
```bash
python validate_schema.py test-*.json
```

---

## Priorita implementace

1. **KRITICKÁ:** {typ stránky} — {schema typy}
2. **KRITICKÁ:** BreadcrumbList — všechny stránky
3. **VYSOKÁ:** {typ stránky} — {schema typy}
4. ...

---

## Kontrolní seznam po implementaci

- [ ] {úkol pro každý typ stránky}
- [ ] Validovat všechna schémata v online validátorech
- [ ] Zkontrolovat v Google Search Console (sekce Vylepšení)
- [ ] Monitorovat výskyt rich snippets (2-4 týdny)

---

## Očekávané výsledky v Google

| Typ stránky | Rich Result | Popis |
|-------------|-------------|-------|
| Homepage | Organization, Sitelinks Search Box | Firemní info ve vyhledávání |
| Produkty | Product snippet | Cena, dostupnost, hodnocení |
| Články | Article snippet | Datum, autor, obrázek |
| ... | ... | ... |

---

## Řešení problémů

### Časté chyby
1. **Chybějící povinné pole** → Přidejte chybějící pole do JSON-LD
2. **Neplatná URL** → Použijte absolutní URL (https://...)
3. **Chybný formát data** → Použijte ISO 8601 (YYYY-MM-DD)
4. **Chybějící @context** → Přidejte `"@context": "https://schema.org"`

---

## Zdroje

- [Schema.org Documentation](https://schema.org/docs/documents.html)
- [Google Search Central — Structured Data](https://developers.google.com/search/docs/appearance/structured-data)
- [Google Rich Results Test](https://search.google.com/test/rich-results)
- [Schema.org Validator](https://validator.schema.org/)

---

**Datum vytvoření:** {YYYY-MM-DD}
**Verze:** 1.0
```

## Výstup

Po dokončení shrň uživateli:
- Celkový počet souborů v projektu
- Seznam všech vytvořených souborů
- Stav finální kontroly
- Projekt je připraven k předání klientovi
