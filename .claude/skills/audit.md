---
description: "Revize stávajících strukturovaných dat na webu klienta. Použij po /analyze, nebo když uživatel chce zkontrolovat existující JSON-LD implementaci. Vyžaduje existující analyza-webu.md v adresáři klienta."
---

# /audit — Revize stávajících strukturovaných dat

## Vstup

- **Povinné:** Adresář klienta `OUTPUT/{KLIENT}/` s hotovou `analyza-webu.md`
- Pokud `analyza-webu.md` neexistuje, upozorni uživatele a doporuč nejdřív spustit `/analyze`

## Postup

### 1. Načtení kontextu

1. Přečti `OUTPUT/{KLIENT}/analyza-webu.md`
2. Identifikuj všechny vzorkové URL z analýzy
3. Pokud existuje předchozí `revize-stavajicich-dat.md` (update projekt), přečti i tu

### 2. Paralelní extrakce JSON-LD

Použij agenta `schema-extractor` pro paralelní stažení všech vzorkových stránek.

Pro každou stránku:
1. Stáhni HTML přes WebFetch
2. Najdi všechny `<script type="application/ld+json">` bloky
3. Zparsuj a vypiš kompletní JSON-LD
4. Pokud žádná data nejsou → zapiš "Žádná JSON-LD data nenalezena"

### 3. Hodnocení nalezených dat

Pro každý nalezený JSON-LD blok zhodnoť:

**Správnost:**
- Je `@context` správně (`https://schema.org`)?
- Jsou všechna povinná pole vyplněna?
- Jsou URL absolutní?
- Je formát dat správný (ceny, datumy, telefony)?

**Kompletnost:**
- Chybí důležité Schema.org typy pro daný typ stránky?
- Jsou využité @id reference pro provázání?
- Je použit @graph pro kombinaci schémat?

**Kvalita:**
- Obsahují data reálné hodnoty (ne placeholder)?
- Odpovídají data obsahu stránky?
- Je využit plný potenciál Schema.org pro daný typ?

### 4. Validace existujících dat

Pokud existují JSON-LD data:
1. Ulož je do dočasných test-*.json souborů
2. Spusť `python NASTROJE/validate_schema.py test-*.json`
3. Zapiš výsledky do revize

### 5. Porovnání s předchozí implementací (update projekt)

Pokud existuje předchozí verze v `OUTPUT/{KLIENT}/`:
- Porovnej stávající implementaci s předchozími doporučeními
- Identifikuj co bylo implementováno a co ne
- Zhodnoť kvalitu implementace

## Výstupní soubor

Zapiš do `OUTPUT/{KLIENT}/revize-stavajicich-dat.md`:

```markdown
# Revize stávajících strukturovaných dat: {Název klienta}

**URL:** {url}
**Datum revize:** {YYYY-MM-DD}

## Executive Summary

| Typ stránky | Stav JSON-LD | Kvalita | Priorita opravy |
|-------------|--------------|---------|-----------------|
| Homepage | ✗ Chybí | — | KRITICKÁ |
| Produkty | ⚠ Částečná | Nízká | VYSOKÁ |
| Kategorie | ✓ Kompletní | Dobrá | — |
| ... | ... | ... | ... |

**Celkové hodnocení:** {Žádná implementace / Částečná / Dobrá / Kompletní}
**Počet typů stránek bez dat:** {číslo} z {celkem}
**Kritické problémy:** {číslo}

## Detailní rozbor

### 1. Homepage ({URL})

**Status:** ✗ Žádná JSON-LD data / ⚠ Částečná / ✓ Kompletní

**Nalezená data:**
```json
{nalezený JSON-LD kód nebo "Žádná data"}
```

**Problémy:**
- ✗ {kritický problém}
- ⚠ {varování}

**Doporučení:**
- Implementovat: Organization, WebSite
- Opravit: {co opravit}

---

### 2. Produkty ({vzorová URL})
(stejná struktura)

---

## Validace existujících dat

### Lokální validace (validate_schema.py)
{výsledky validace}

## Akční plán

### KRITICKÁ priorita (implementovat ihned)
1. {akce}

### VYSOKÁ priorita
1. {akce}

### STŘEDNÍ priorita
1. {akce}

## Kontrolní seznam

- [ ] {úkol 1}
- [ ] {úkol 2}
- ...
```

## Přechod na další krok

Po dokončení revize informuj uživatele o zjištěních a doporuč pokračovat s `/create-schemas`.
