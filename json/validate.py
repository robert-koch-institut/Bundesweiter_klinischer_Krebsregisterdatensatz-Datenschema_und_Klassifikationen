# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "jsonschema",
#   "requests",
#   "tabulate",
# ]
# ///

# ! must be run in json/ folder
# ! uv run validate.py

import json
import pathlib

import jsonschema
import requests
from tabulate import tabulate

SCHEMA_URL = "https://datapackage.org/profiles/2.0/tableschema.json"


def validate_against_tableschema(data_file: str) -> None:
    schema = requests.get(SCHEMA_URL).json()

    with open(data_file) as f:
        data = json.load(f)

    try:
        jsonschema.validate(instance=data, schema=schema)
        print(f"✅ File is valid! ({data_file})")
    except jsonschema.ValidationError as e:
        print("❌ Validation error:")
        print(f"  Path:    {' -> '.join(str(p) for p in e.absolute_path) or '(root)'}")
        print(f"  Rule:    {e.validator} = {e.validator_value}")
        print(f"  Message: {e.message}")


# def validate_against_tableschema_local(data_file: str) -> None:
#     with open(data_file) as f:
#         data = json.load(f)

#     schema_rel = data["$schema"].lstrip("/")
#     schema_path = pathlib.Path(data_file).parent / schema_rel
#     with open(schema_path) as f:
#         schema = json.load(f)

#     try:
#         jsonschema.validate(instance=data, schema=schema)
#         print("✅ Data is valid!")
#     except jsonschema.ValidationError as e:
#         print("❌ Validation error:")
#         print(f"  Path:    {' -> '.join(str(p) for p in e.absolute_path) or '(root)'}")
#         print(f"  Rule:    {e.validator} = {e.validator_value}")
#         print(f"  Message: {e.message}")


def print_json(data_file: str) -> None:
    with open(data_file) as f:
        data = json.load(f)
    rows = [
        [
            f["name"],
            f.get("type", ""),
            f.get("description", "")[:60],
            ", ".join(str(v) for v in f.get("constraints", {}).get("enum", [])[:5]) or "",
            len(f.get("categories", [])) or "",
        ]
        for f in data.get("fields", [])
    ]
    print(tabulate(rows, headers=["name", "type", "description", "enum", "#cat"], tablefmt="simple"))


def create_md(data_file: str, out_file: str = "data.md") -> None:
    with open(data_file) as f:
        data = json.load(f)
    rows = [
        [
            f["name"],
            f.get("type", ""),
            f.get("description", ""),
            ", ".join(str(v) for v in f.get("constraints", {}).get("enum", [])) or "",
            len(f.get("categories", [])) or "",
        ]
        for f in data.get("fields", [])
    ]
    table = tabulate(rows, headers=["name", "type", "description", "enum", "#cat"], tablefmt="github")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(table + "\n")
    print(f"✅ {out_file} written ({len(rows)} fields)")

# FILE_JSON = "epi-de.json"
# FILE_JSON = "obds-origin-en.json"
FILE_JSON = "obds-origin-de.json"

# validate_against_tableschema_local(FILE_JSON)
validate_against_tableschema(FILE_JSON)
# print_json(FILE_JSON)
# create_md(FILE_JSON)
