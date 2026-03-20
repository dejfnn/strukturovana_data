# OUTPUT - Vypracované projekty

Tato složka obsahuje **vypracované projekty strukturovaných dat**. Každý projekt je ve složce pojmenované podle domény klienta.

---

## 📁 Struktura složky

Každý projekt má složku pojmenovanou podle domény (velkými písmeny):

```
OUTPUT/
├── SICO/               ← www.sico.cz (vzorový projekt)
└── [NAZEV-DOMENY]/     ← další projekty...
```

**Pravidlo pojmenování:**
- `www.example.cz` → `OUTPUT/EXAMPLE/`
- `www.moje-firma.cz` → `OUTPUT/MOJE-FIRMA/`

---

## 📁 Obsah projektové složky

Každá projektová složka obsahuje:

```
OUTPUT/NAZEV-DOMENY/
├── analyza-webu.md              ← Analýza struktury webu (Krok 1)
├── revize-stavajicich-dat.md    ← Revize stávajících dat (Krok 2)
├── strukturovana-data-*.md      ← Hotová strukturovaná data (Krok 3)
├── README.md                    ← Dokumentace pro klienta (Krok 5)
├── test-*.json                  ← Testovací soubory (Krok 4)
└── *.html                       ← HTML verze pro Word (volitelné)
```

---

## Vzorové projekty

### SICO/
**Vzorový projekt pro SICO RENT (www.sico.cz)**

Kompletní příklad projektu strukturovaných dat pro firmu zabývající se pronájmem pracovních plošin.

**Co obsahuje:**
- ✅ `strukturovana-data-sico.md` - Hotová strukturovaná data pro všechny typy stránek
- ✅ `revize-stavajicich-dat.md` - Revize stávajících dat s komentáři a chybami
- ✅ `README.md` - Dokumentace projektu pro klienta
- ✅ `test-*.json` - Validované testovací soubory
- ✅ `*.html` - HTML verze dokumentů pro Word
- ✅ `validate_schema.py` - Validační skript
- ✅ `md_to_html.py` - Konvertor MD → HTML

**Proč se podívat:**
- Vidíte finální výstup projektu
- Inspirace pro strukturu dokumentů
- Příklad reálných dat ze stránek
- Ukázka revize s kritickými chybami
- Vzor pro dokumentaci klienta

---

## 🎯 Jak používat vzorové projekty

### 1. Před zahájením nového projektu
Prohlédněte si vzorový projekt SICO, abyste věděli:
- Jak má vypadat finální výstup
- Jakou strukturu mají dokumenty
- Jak formátovat strukturovaná data
- Jak psát revizi

### 2. Během projektu
Používejte jako referenci:
- Kontrolujte formátování JSON-LD
- Inspirujte se strukturou dokumentů
- Srovnávejte s vašimi výstupy

### 3. Před předáním klientovi
Porovnejte váš projekt s vzorovým:
- Máte všechny potřebné soubory?
- Je dokumentace kompletní?
- Jsou data validovaná?

---

## 📝 Co najdete v každém projektu

### Strukturovaná data
- JSON-LD schémata pro všechny typy stránek
- Reálná data ze stránek klienta
- Vytučněné hodnoty pro lepší orientaci
- Poznámky k implementaci

### Revize stávajících dat
- Analýza současného stavu
- Identifikované chyby a problémy
- Doporučení k opravě
- Prioritizace úkolů

### README pro klienta
- Instrukce k implementaci
- Validační návod
- Kontrolní seznam
- Prioritizace implementace

### Testovací soubory
- Validované příklady JSON-LD
- Připravené k testování
- Různé typy schémat

---

## 🚀 Přidání vlastního projektu

Pokud chcete přidat váš vypracovaný projekt jako vzor:

1. Vytvořte složku s názvem klienta:
   ```bash
   cd OUTPUT
   mkdir NAZEV-KLIENTA
   ```

2. Zkopírujte všechny finální soubory:
   - strukturovana-data-*.md
   - revize-stavajicich-dat.md
   - README.md
   - test-*.json
   - *.html (pokud jsou)
   - validační skripty

3. Ujistěte se, že projekt obsahuje:
   - ✅ Kompletní dokumentaci
   - ✅ Validovaná data
   - ✅ Reálné příklady
   - ✅ Instrukce pro klienta

---

## 💡 Tipy

### Pro začátečníky
1. Začněte prohlédnutím SICO/strukturovana-data-sico.md
2. Podívejte se na formátování JSON-LD
3. Všimněte si vytučněných hodnot
4. Prostudujte strukturu dokumentu

### Pro pokročilé
1. Prohlédněte SICO/revize-stavajicich-dat.md
2. Všimněte si, jak jsou popsány chyby
3. Podívejte se na prioritizaci
4. Inspirujte se doporučeními

---

## 📋 Checklist pro vzorový projekt

Než přidáte projekt do OUTPUT:

- [ ] Projekt je kompletní a validovaný
- [ ] Obsahuje reálná data (ne placeholder)
- [ ] Dokumentace je jasná a srozumitelná
- [ ] Má README s instrukcemi
- [ ] Obsahuje testovací soubory
- [ ] Je vhodný jako vzor pro ostatní

---

**Aktualizováno**: 2025-12-04
**Počet vzorových projektů**: 1 (SICO)
