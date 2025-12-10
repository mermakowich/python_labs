import json
import csv
import pytest
from pathlib import Path
from src.lab05.json_csv import json_to_csv, csv_to_json


def test_json_to_csv_roundtrip(tmp_path: Path):
    src_json = tmp_path / "test.json"
    dst_csv = tmp_path / "test.csv"

    test_data = [
        {"name": "Alice", "age": 22, "city": "SPb"},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 30, "city": "Moscow"},
    ]

    src_json.write_text(
        json.dumps(test_data, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    json_to_csv(str(src_json), str(dst_csv))

    with dst_csv.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        result = list(reader)

    assert len(result) == 3
    assert set(result[0].keys()) == {"name", "age", "city"}
    assert result[0]["name"] == "Alice"
    assert result[1]["name"] == "Bob"
    assert result[1]["city"] == ""


def test_csv_to_json_roundtrip(tmp_path: Path):
    src_csv = tmp_path / "test.csv"
    dst_json = tmp_path / "test.json"

    test_data = [
        {"name": "Alice", "age": "22", "city": "SPb"},
        {"name": "Bob", "age": "25", "city": ""},
    ]

    with src_csv.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age", "city"])
        writer.writeheader()
        writer.writerows(test_data)

    csv_to_json(str(src_csv), str(dst_json))

    with dst_json.open(encoding="utf-8") as f:
        result = json.load(f)

    assert len(result) == 2
    assert result[0]["name"] == "Alice"
    assert result[1]["city"] == ""


def test_json_to_csv_empty(tmp_path: Path):
    src = tmp_path / "empty.json"
    dst = tmp_path / "empty.csv"

    src.write_text("[]", encoding="utf-8")

    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst))


def test_csv_to_json_no_header(tmp_path: Path):
    src = tmp_path / "noheader.csv"
    dst = tmp_path / "noheader.json"

    src.write_text("", encoding="utf-8")

    with pytest.raises(ValueError):
        csv_to_json(str(src), str(dst))


def test_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        json_to_csv("nonexistent.json", "out.csv")
