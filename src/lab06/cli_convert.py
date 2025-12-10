"""
CLI-конвертеры для JSON/CSV/XLSX.

Команды для запуска:
- python -m src.lab06.cli_convert json2csv --in data/lab05/samples/people.json --out data/out/people.csv
- python -m src.lab06.cli_convert csv2json --in data/lab05/samples/people.csv --out data/out/people.json
- python -m src.lab06.cli_convert csv2xlsx --in data/lab05/samples/people.json --out data/out/people.xlsx
"""

import argparse
from pathlib import Path

from ..lab05.json_csv import json_to_csv, csv_to_json
from ..lab05.csv_xlsx import csv_to_xlsx


def main() -> None:
    parser = argparse.ArgumentParser(
        description="CLI-утилиты, конвертирующие файлы JSON/CSV/XLSX"
    )
    subparsers = parser.add_subparsers(dest="command")

    json2csv = subparsers.add_parser("json2csv", help="JSON to CSV")
    json2csv.add_argument("--in", dest="input", required=True, help="Путь к input-JSON")
    json2csv.add_argument(
        "--out", dest="output", required=True, help="Путь к output-CSV"
    )

    csv2json = subparsers.add_parser("csv2json", help="CSV to JSON")
    csv2json.add_argument("--in", dest="input", required=True, help="Путь к input-CSV")
    csv2json.add_argument(
        "--out", dest="output", required=True, help="Путь к output-JSON"
    )

    csv2xlsx = subparsers.add_parser("csv2xlsx", help="CSV to XLSX")
    csv2xlsx.add_argument("--in", dest="input", required=True, help="Путь к input-CSV")
    csv2xlsx.add_argument(
        "--out", dest="output", required=True, help="Путь к output-XLSX"
    )

    args = parser.parse_args()

    """
    Проверка на указание команды и наличие файла в --in
    """
    if args.command is None:
        parser.error("Не указана команда")
    else:
        p = Path(args.input)
        if not p.exists():
            raise FileNotFoundError()

    try:
        if args.command == "json2csv":
            json_to_csv(args.input, args.output)
        elif args.command == "csv2json":
            csv_to_json(args.input, args.output)
        elif args.command == "csv2xlsx":
            csv_to_xlsx(args.input, args.output)
    except ValueError:
        parser.error("Ошибка конвертации")


if __name__ == "__main__":
    main()
