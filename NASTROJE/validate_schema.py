"""
Validátor strukturovaných dat JSON-LD pro Schema.org
Tento skript validuje JSON-LD data pomocí několika metod:
1. Základní JSON syntaxe
2. JSON-LD parsing
3. Schema.org validace (základní kontroly)
4. Kontrola prázdných hodnot

Podporuje validaci více souborů najednou pomocí glob vzorů (např. *.json)
"""

import json
import sys
import io
import glob
import os
from typing import Dict, List, Tuple

# Nastavení UTF-8 pro Windows konzoli
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

def validate_json_syntax(json_str: str) -> Tuple[bool, str]:
    """Validace základní JSON syntaxe"""
    try:
        json.loads(json_str)
        return True, "✓ JSON syntaxe je platná"
    except json.JSONDecodeError as e:
        return False, f"✗ JSON syntaxe chyba: {e}"

def validate_required_fields(data: Dict, schema_type: str) -> List[str]:
    """Validace povinných polí podle typu schématu"""
    errors = []
    required_fields = {
        "Organization": ["@type", "name", "url"],
        "Product": ["@type", "name", "image", "offers"],
        "Article": ["@type", "headline", "image", "datePublished", "author"],
        "WebSite": ["@type", "url", "name"],
        "BreadcrumbList": ["@type", "itemListElement"],
        "CollectionPage": ["@type", "url", "name"],
        "LocalBusiness": ["@type", "name", "address", "telephone"],
        "Service": ["@type", "name", "provider"],
        "FAQPage": ["@type", "mainEntity"],
    }

    if schema_type in required_fields:
        for field in required_fields[schema_type]:
            if field not in data:
                errors.append(f"✗ Chybí povinné pole: {field}")

    return errors


def validate_empty_values(data: Dict, path: str = "") -> List[str]:
    """Kontrola prázdných hodnot"""
    warnings = []

    if isinstance(data, dict):
        for key, value in data.items():
            current_path = f"{path}.{key}" if path else key

            # Přeskočit @context a @type
            if key in ["@context", "@type", "@id"]:
                continue

            if value is None:
                warnings.append(f"⚠ Prázdná hodnota (null): {current_path}")
            elif isinstance(value, str) and value.strip() == "":
                warnings.append(f"⚠ Prázdný řetězec: {current_path}")
            elif isinstance(value, str) and value.startswith("{{") and value.endswith("}}"):
                warnings.append(f"⚠ Nevyplněný placeholder: {current_path} = {value}")
            elif isinstance(value, (dict, list)):
                warnings.extend(validate_empty_values(value, current_path))

    elif isinstance(data, list):
        if len(data) == 0:
            warnings.append(f"⚠ Prázdné pole: {path}")
        else:
            for i, item in enumerate(data):
                warnings.extend(validate_empty_values(item, f"{path}[{i}]"))

    return warnings

def validate_urls(data: Dict, path: str = "") -> List[str]:
    """Validace URL adres"""
    errors = []

    if isinstance(data, dict):
        for key, value in data.items():
            current_path = f"{path}.{key}" if path else key

            if key in ["url", "image", "logo", "sameAs"] and isinstance(value, str):
                if not (value.startswith("http://") or value.startswith("https://")):
                    errors.append(f"✗ Neplatná URL v {current_path}: {value}")

            if isinstance(value, (dict, list)):
                errors.extend(validate_urls(value, current_path))

    elif isinstance(data, list):
        for i, item in enumerate(data):
            errors.extend(validate_urls(item, f"{path}[{i}]"))

    return errors

def validate_context(data: Dict) -> List[str]:
    """Validace @context"""
    errors = []

    if "@context" not in data:
        errors.append("✗ Chybí @context")
        return errors

    context = data["@context"]
    if isinstance(context, str):
        if context not in ["https://schema.org", "http://schema.org"]:
            errors.append(f"✗ Neplatný @context: {context}")
    elif isinstance(context, list):
        if "https://schema.org" not in context and "http://schema.org" not in context:
            errors.append("✗ @context neobsahuje schema.org")

    return errors

def validate_schema_type(data: Dict, check_context: bool = True) -> Tuple[bool, str, List[str], List[str]]:
    """Validace @type a dalších polí. Vrací (is_valid, schema_type, errors, warnings)

    Args:
        data: JSON-LD objekt k validaci
        check_context: Zda kontrolovat @context (False pro objekty uvnitř @graph)
    """
    errors = []
    warnings = []

    if "@type" not in data:
        errors.append("✗ Chybí @type")
        return False, None, errors, warnings

    schema_type = data["@type"]

    # Validace povinných polí
    field_errors = validate_required_fields(data, schema_type)
    errors.extend(field_errors)

    # Validace URL
    url_errors = validate_urls(data)
    errors.extend(url_errors)

    # Validace @context (pouze pokud není uvnitř @graph)
    if check_context:
        context_errors = validate_context(data)
        errors.extend(context_errors)

    # Kontrola prázdných hodnot (varování)
    empty_warnings = validate_empty_values(data)
    warnings.extend(empty_warnings)

    return len(errors) == 0, schema_type, errors, warnings

def validate_json_ld(json_str: str, filename: str = "") -> Tuple[bool, int, int]:
    """Hlavní validační funkce. Vrací (has_errors, error_count, warning_count)"""
    total_errors = 0
    total_warnings = 0

    if filename:
        print("=" * 70)
        print(f"SOUBOR: {filename}")
        print("=" * 70)
    else:
        print("=" * 70)
        print("VALIDACE STRUKTUROVANÝCH DAT JSON-LD")
        print("=" * 70)
    print()

    # 1. Validace JSON syntaxe
    is_valid, message = validate_json_syntax(json_str)
    print(f"1. JSON syntaxe: {message}")

    if not is_valid:
        print("\n❌ Validace selhala kvůli chybné JSON syntaxi")
        return True, 1, 0

    # Načtení JSON dat
    data = json.loads(json_str)

    # 2. Validace @graph struktury (pokud existuje)
    if "@graph" in data:
        # Nejprve zkontrolovat @context na root úrovni
        context_errors = validate_context(data)
        if context_errors:
            print("2. Kontrola @context:")
            for error in context_errors:
                print(f"   {error}")
            total_errors += len(context_errors)
            print()

        print("3. Detekována @graph struktura - validuji každý objekt:")
        print()

        for i, item in enumerate(data["@graph"], 1):
            print(f"   Objekt {i}:")
            # check_context=False protože @context je na root úrovni
            is_valid, schema_type, errors, warnings = validate_schema_type(item, check_context=False)

            if schema_type:
                print(f"   ✓ Typ: {schema_type}")

            if is_valid:
                print(f"   ✓ Objekt je validní")
            else:
                print(f"   ✗ Objekt obsahuje chyby:")
                for error in errors:
                    print(f"     {error}")
                total_errors += len(errors)

            if warnings:
                print(f"   ⚠ Varování:")
                for warning in warnings:
                    print(f"     {warning}")
                total_warnings += len(warnings)
            print()

    # 3. Validace jednotlivého objektu
    else:
        print("2. Validace schématu:")
        is_valid, schema_type, errors, warnings = validate_schema_type(data)

        if schema_type:
            print(f"   ✓ Typ: {schema_type}")

        if is_valid:
            print(f"   ✓ Schéma je validní")
        else:
            print(f"   ✗ Schéma obsahuje chyby:")
            for error in errors:
                print(f"     {error}")
            total_errors += len(errors)

        if warnings:
            print(f"   ⚠ Varování:")
            for warning in warnings:
                print(f"     {warning}")
            total_warnings += len(warnings)

    return total_errors > 0, total_errors, total_warnings

def print_summary(total_files: int, files_with_errors: int, total_errors: int, total_warnings: int):
    """Vytiskne souhrnné statistiky"""
    print()
    print("=" * 70)
    print("SOUHRN VALIDACE")
    print("=" * 70)
    print(f"Celkem souborů:    {total_files}")
    print(f"Soubory s chybami: {files_with_errors}")
    print(f"Celkem chyb:       {total_errors}")
    print(f"Celkem varování:   {total_warnings}")
    print()
    if files_with_errors == 0 and total_errors == 0:
        print("✅ Všechny soubory jsou validní!")
    else:
        print("❌ Některé soubory obsahují chyby.")
    print()
    print("DOPORUČENÍ:")
    print("• Pro komplexní validaci použijte:")
    print("  - https://validator.schema.org/")
    print("  - https://search.google.com/test/rich-results")
    print("• Tato validace kontroluje pouze základní strukturu")
    print("=" * 70)


def main():
    """Hlavní funkce"""
    if len(sys.argv) < 2:
        print("Použití:")
        print("  python validate_schema.py <soubor.json>      - validace jednoho souboru")
        print("  python validate_schema.py *.json             - validace více souborů")
        print("  python validate_schema.py test-*.json        - validace souborů podle vzoru")
        print()
        print("Příklady:")
        print("  python validate_schema.py organization.json")
        print("  python validate_schema.py OUTPUT/KLENOTA/*.json")
        sys.exit(1)

    # Získání seznamu souborů (podpora glob vzorů)
    files = []
    for pattern in sys.argv[1:]:
        # Zkusit glob expanzi
        matched = glob.glob(pattern)
        if matched:
            files.extend(matched)
        else:
            # Pokud glob nic nenašel, přidat jako konkrétní soubor
            files.append(pattern)

    # Odstranění duplicit a seřazení
    files = sorted(set(files))

    if not files:
        print("✗ Nebyly nalezeny žádné soubory")
        sys.exit(1)

    # Statistiky
    total_files = len(files)
    files_with_errors = 0
    total_errors = 0
    total_warnings = 0

    # Validace každého souboru
    for json_file in files:
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                json_str = f.read()

            has_errors, errors, warnings = validate_json_ld(json_str, os.path.basename(json_file))

            if has_errors:
                files_with_errors += 1
            total_errors += errors
            total_warnings += warnings

            print()

        except FileNotFoundError:
            print(f"✗ Soubor nenalezen: {json_file}")
            files_with_errors += 1
            total_errors += 1
        except Exception as e:
            print(f"✗ Chyba při čtení souboru {json_file}: {e}")
            files_with_errors += 1
            total_errors += 1

    # Souhrn (pouze pokud bylo více souborů)
    if total_files > 1:
        print_summary(total_files, files_with_errors, total_errors, total_warnings)

    sys.exit(1 if files_with_errors > 0 else 0)


if __name__ == "__main__":
    main()
