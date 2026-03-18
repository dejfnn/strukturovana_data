---
description: "Validace vytvořených JSON-LD strukturovaných dat. Použij po /create-schemas, nebo když uživatel chce zvalidovat existující JSON-LD soubory. Spustí lokální validátor a připraví soubory pro online validaci."
---

# /validate — Validace strukturovaných dat

## Vstup

- **Povinné:** Adresář klienta `OUTPUT/{KLIENT}/` s `test-*.json` soubory
- Pokud test soubory neexistují, upozorni a doporuč nejdřív `/create-schemas`

## Postup

### 1. Lokální validace

Spusť hromadnou validaci všech test souborů:

```bash
python NASTROJE/validate_schema.py OUTPUT/{KLIENT}/test-*.json
```

### 2. Analýza výsledků

Pro každý soubor zkontroluj:

**Chyby (MUSÍ se opravit):**
- ✗ Neplatná JSON syntaxe
- ✗ Chybí povinná pole (@context, @type, name, url...)
- ✗ Neplatné URL (relativní, nevalidní formát)
- ✗ Chybí @context

**Varování (DOPORUČENO opravit):**
- ⚠ Prázdné řetězce
- ⚠ Nevyplněné placeholdery (`{{...}}`)
- ⚠ Chybějící doporučená pole

### 3. Oprava chyb

Pokud validace odhalí chyby:
1. Oprav chybu v příslušném `test-*.json`
2. Oprav odpovídající sekci v `strukturovana-data-{klient}.md`
3. Spusť validaci znovu
4. Opakuj dokud nejsou všechny soubory bez chyb

### 4. Kontrola konzistence

Ověř napříč všemi schématy:
- Jsou `@id` reference konzistentní? (Organization @id na homepage = seller @id na produktech)
- Je `@context` všude `https://schema.org`?
- Jsou base URL všude stejné?
- Jsou kontaktní údaje (telefon, email, adresa) konzistentní?

### 5. Příprava pro online validaci

Pro každý test soubor připrav JSON-LD kód k vložení do:
1. **Schema.org Validator:** https://validator.schema.org/
2. **Google Rich Results Test:** https://search.google.com/test/rich-results

Uživateli předlož:
- Odkaz na validátory
- Připravený JSON-LD kód k vložení (pro každý typ stránky)
- Pokyny co kontrolovat

### 6. Zápis výsledků

Doplň sekci VALIDACE do `strukturovana-data-{klient}.md`:

```markdown
## VALIDACE

### Lokální validace (validate_schema.py)

| Soubor | Status | Chyby | Varování |
|--------|--------|-------|----------|
| test-homepage.json | ✓ Validní | 0 | 0 |
| test-product.json | ✓ Validní | 0 | 0 |
| test-category.json | ✓ Validní | 0 | 0 |
| test-article.json | ✓ Validní | 0 | 0 |
| ... | ... | ... | ... |

**Celkem:** {n} souborů, {0} chyb, {0} varování

### Online validace (provést manuálně)

Pro každý typ stránky vložte JSON-LD kód do:
- Schema.org Validator: https://validator.schema.org/
- Google Rich Results Test: https://search.google.com/test/rich-results

#### Očekávané výsledky

| Typ | Rich Result | Detekované entity |
|-----|-------------|-------------------|
| Homepage | Organization, Sitelinks Search Box | Organization, WebSite |
| Produkty | Product snippet (cena, dostupnost) | Product, Offer |
| Kategorie | Carousel (volitelné) | CollectionPage, ItemList |
| Články | Article snippet (datum, autor) | Article |
| ... | ... | ... |
```

## Výstup

- Opravené `test-*.json` soubory (pokud byly chyby)
- Aktualizovaná sekce VALIDACE v `strukturovana-data-{klient}.md`
- Připravené JSON-LD bloky pro online validaci

## Přechod na další krok

Po úspěšné validaci doporuč pokračovat s `/document` pro finální dokumentaci a HTML export.
