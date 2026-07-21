# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "jsonschema",
#   "requests",
#   "tabulate",
# ]
# ///

# ! uv run validate.py

import json
import os
import pathlib
import re
import urllib.parse

import jsonschema
import requests
from tabulate import tabulate

os.chdir(pathlib.Path(__file__).resolve().parent)

# SCHEMA_URL = "https://datapackage.org/profiles/2.0/tableschema.json"

HEADERS = {
    "tablename": "Tabelle",
    "name": "Variable",
    "type": "Typ",
    "enum": "Ausprägungen",
    "description": "Beschreibung",
}


def datapackage_validate(data_file: str) -> None:
    """Validate data_file against the Table Schema profile named in its own "$schema" key."""
    with open(data_file) as f:
        data = json.load(f)

    schema = requests.get(data["$schema"]).json()

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


def _escape_md(value):
    """Escape a value for plain (non-code-span) Markdown table cell text."""
    if not isinstance(value, str):
        value = str(value)
    return value.replace("|", "\\|").replace("[", "&#91;").replace("]", "&#93;")


def _code(value) -> str:
    """Render value as backtick-wrapped segments, with "|" escaped outside any code span."""
    # backtick-wrap, but split on literal "|" first: a pipe *inside* a code span isn't
    # reliably protected by every renderer, so keep it outside any span and escape it there,
    # where backslash-escaping actually works.
    s = value if isinstance(value, str) else str(value)
    return "\\|".join(f"`{seg}`" for seg in s.split("|"))


def _enum_cell(field: dict, truncate: bool) -> str:
    """Render the "Werte" cell: labels > referenceUrl > enum > example > other constraints."""
    constraints = field.get("constraints", {})
    vals = constraints.get("enum", [])
    cats = {c["value"]: c["label"] for c in field.get("categories", [])}
    if cats:
        shown = vals[:5] if truncate else vals
        parts = [f'{_code(v)}="{_escape_md(cats[v])}"' if v in cats else _code(v) for v in shown]
        text = "<br>".join(parts)
        if truncate and len(vals) > 5:
            text += "<br>…"
        return text
    if field.get("referenceUrl"):
        url = field["referenceUrl"]
        if truncate:
            return _escape_md(url)
        label = pathlib.Path(urllib.parse.urlparse(url).path).stem
        return f"[`{label}`]({url})"
    if vals:
        return ", ".join(_code(v) for v in (vals[:5] if truncate else vals))
    if field.get("example"):
        return f"ex: {_code(field['example'])}"
    other = {k: v for k, v in constraints.items() if k != "enum"}
    if other:
        return ", ".join(f"{k}={_code(v)}" for k, v in other.items())
    return ""


def _cell(field: dict, header: str, truncate: bool):
    """Return the raw (unescaped) value for a single column of a field's row."""
    if header == "name":
        return field["name"]
    if header == "description":
        d = field.get("description", "")
        return d[:60] if truncate else d
    if header == "enum":
        return _enum_cell(field, truncate)
    if header == "#cat":
        return len(field.get("categories", [])) or ""
    return field.get(header, "")


def _build_rows(fields: list, columns: list = None, truncate: bool = False) -> list:
    """Build a table row (list of escaped cell strings) per field for the given columns."""
    cols = columns or list(HEADERS)

    def cell(f, h):
        v = _cell(f, h, truncate)
        return v if h == "enum" else _escape_md(v)

    return [[cell(f, h) for h in cols] for f in fields]


def print_json(data_file: str) -> None:
    """Print all fields of data_file as a table to the console."""
    with open(data_file) as f:
        fields = json.load(f).get("fields", [])
    rows = _build_rows(fields, truncate=True)
    headers = list(HEADERS.values())
    print(tabulate(rows, headers=headers, tablefmt="simple"))


def _render_table(fields: list, columns: list, heading: str, header_level: int) -> str:
    """Render one Markdown table for fields, with an optional "#" * header_level heading above it."""
    rows = _build_rows(fields, columns=columns, truncate=False)
    headers = [HEADERS.get(h, h) for h in columns]
    table = tabulate(rows, headers=headers, tablefmt="github")
    prefix = "#" * header_level
    return (f"{prefix} {heading}\n\n" if heading else "") + table + "\n"


def datapackage_to_md(
    data_file: str,
    out_file: str = "data.md",
    chunk_tables: bool = False,
    include_vars_regex: str = None,
    print_title: bool = False,
    markdown_placeholder_start: str = None,
    markdown_placeholder_end: str = None,
    placeholder_file: str = None,
    title_header_level: int = 2,
) -> None:
    """Render data_file's fields to Markdown, either writing out_file or inserting between two markers.

    Args:
        data_file: path to the Table Schema JSON to render.
        out_file: path to write to when markdown_placeholder_start/_end are not set.
        chunk_tables: split output into one table per "tablename" (heading each).
        include_vars_regex: only include fields whose name matches this regex. eg: `^(?!z_)` to exclude `z_` fields
        print_title: prepend the JSON's top-level "title"/"description" as a heading/quote.
        markdown_placeholder_start: if set (together with markdown_placeholder_end and
            placeholder_file), find both literal markers in placeholder_file and overwrite
            everything between them with the rendered output, keeping the markers themselves
            in place so the file stays re-runnable.
        markdown_placeholder_end: end marker, see markdown_placeholder_start.
        placeholder_file: file to scan/update for the markers. Placeholder mode only activates
            when this is set; otherwise out_file is simply (re)written in full.
        initial_header_level: heading level for the title (e.g. 2 = "##"); table
            headings from chunk_tables use one level deeper (e.g. "###").
    """
    with open(data_file) as f:
        data = json.load(f)
    fields = data.get("fields", [])

    if include_vars_regex:
        pattern = re.compile(include_vars_regex)
        fields = [f for f in fields if pattern.search(f["name"])]

    parts = []
    if print_title:
        title = data.get("title")
        description = data.get("description")
        if title:
            parts.append(f"{'#' * title_header_level} {title}\n")
        if description:
            parts.append(f"> {description}\n")

    table_header_level = title_header_level + 1
    if not chunk_tables:
        parts.append(_render_table(fields, list(HEADERS), heading=None, header_level=table_header_level))
    else:
        groups: dict[str, list] = {}
        for f in fields:
            groups.setdefault(f.get("tablename") or None, []).append(f)
        columns = [h for h in HEADERS if h != "tablename"]
        for tablename, group_fields in groups.items():
            parts.append(_render_table(group_fields, columns, heading=tablename, header_level=table_header_level))

    content = "\n".join(parts)

    if placeholder_file and markdown_placeholder_start and markdown_placeholder_end:
        scan_file = placeholder_file
        existing = pathlib.Path(scan_file).read_text(encoding="utf-8")
        start_idx = existing.find(markdown_placeholder_start)
        end_idx = existing.find(markdown_placeholder_end)
        if start_idx == -1 or end_idx == -1:
            print(f"⚠️  start/end markers not found in {scan_file}, nothing written")
            return
        if end_idx < start_idx:
            print(f"⚠️  end marker appears before start marker in {scan_file}, nothing written")
            return
        insert_at = start_idx + len(markdown_placeholder_start)
        updated = f"{existing[:insert_at]}\n{content}\n{existing[end_idx:]}"
        pathlib.Path(scan_file).write_text(updated, encoding="utf-8")
        print(f"{scan_file} updated ({len(fields)} fields) [content between markers replaced]")
        return


        
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(content + "\n")
    print(f"{out_file} written ({len(fields)} fields)")


# FILE_JSON = "epi-de.json"
FILE_JSON = "obds-zfkd-de.json"
# FILE_JSON = "obds-zfkd-en.json"

print_json(FILE_JSON)
# datapackage_validate(FILE_JSON)
datapackage_to_md(
    data_file=FILE_JSON,
    # out_file="data.md",
    placeholder_file="../Readme.md",
    chunk_tables=True,
    # include_vars_regex='^(?!z_)'
    markdown_placeholder_start="<!-- TABLEINSERT-START -->",
    markdown_placeholder_end="<!-- TABLEINSERT-END -->",
    print_title=True,
    title_header_level=3,
)
