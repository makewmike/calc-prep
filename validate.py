#!/usr/bin/env python3
"""
validate.py
Validates progress/mastery.json and progress/streak.json against their schemas.
Run before any commit to catch malformed state files early.

Usage:
    python validate.py

Exit codes:
    0 — all files valid
    1 — one or more validation errors found
"""

import json
import sys
from pathlib import Path

try:
    import jsonschema
except ImportError:
    print("⚠️  jsonschema not installed. Run: pip install jsonschema")
    sys.exit(1)

REPO_ROOT = Path(__file__).parent

FILES = [
    (
        REPO_ROOT / "progress" / "mastery.json",
        REPO_ROOT / "progress" / "mastery.schema.json",
    ),
    (
        REPO_ROOT / "progress" / "streak.json",
        REPO_ROOT / "progress" / "streak.schema.json",
    ),
]

def validate_file(data_path: Path, schema_path: Path) -> list[str]:
    errors = []
    try:
        data   = json.loads(data_path.read_text())
        schema = json.loads(schema_path.read_text())
    except json.JSONDecodeError as e:
        return [f"JSON parse error in {data_path.name}: {e}"]

    validator = jsonschema.Draft7Validator(schema)
    for error in sorted(validator.iter_errors(data), key=lambda e: list(e.path)):
        path = " → ".join(str(p) for p in error.path) or "(root)"
        errors.append(f"  [{data_path.name}] {path}: {error.message}")
    return errors

def main():
    all_errors = []
    for data_path, schema_path in FILES:
        if not data_path.exists():
            all_errors.append(f"  Missing file: {data_path}")
            continue
        if not schema_path.exists():
            all_errors.append(f"  Missing schema: {schema_path}")
            continue
        errs = validate_file(data_path, schema_path)
        all_errors.extend(errs)

    if all_errors:
        print("❌ Validation failed:\n")
        for e in all_errors:
            print(e)
        sys.exit(1)
    else:
        print("✅ All progress files valid.")
        sys.exit(0)

if __name__ == "__main__":
    main()
