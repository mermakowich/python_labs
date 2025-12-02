"""
Модуль для конвертации между форматом JSON и CSV.
Функция write_csv импортирована из io_helpers.py (ЛР4).
"""

import json
import csv
from pathlib import Path
from ..lib.io_helpers import write_csv

def json_to_csv(json_path, csv_path):
    """
    Преобразует JSON-файл в CSV.
    Заголовки берутся из первого объекта. Отсутствующие значения заменяются на пустую строку.
    Файл записывается в UTF-8.

    Аргументы:
        json_path: путь к входному JSON.
        csv_path: путь к выходному CSV.

    Ошибки:
        FileNotFoundError: если файл отсутствует.
        ValueError: если структура неверная, нет заголовков, не всё словари или файл пустой.
    """
    path = Path(json_path)
    if not path.exists():
        raise FileNotFoundError()

    with path.open(encoding="utf-8") as f:
        try:
            data = json.load(f)
        except Exception as e:
            raise ValueError("Неверный тип файла")

    if not isinstance(data, list) or not data:
        raise ValueError("Пустой JSON или неподдерживаемая структура")
    if not all(isinstance(obj, dict) for obj in data):
        raise ValueError()

    """
    Получаем ключи из первого объекта
    """
    headers = data[0].keys()

    rows = []
    for obj in data:
        row = []
        for col in headers:
            row.append(str(obj.get(col, "")))
        rows.append(row)

    write_csv(rows, csv_path, header=tuple(headers))


def csv_to_json(csv_path, json_path):
    """
    Преобразует CSV-файл в JSON.
    Все значения сохраняются как строки.

    Аргументы:
        csv_path: путь к входному CSV-файлу.
        json_path: путь к выходному JSON-файлу.

    Исключения:
        FileNotFoundError: если файл отсутствует.
        ValueError: если нет заголовка или файл пустой.
    """
    path = Path(csv_path)
    if not path.exists():
        raise FileNotFoundError()

    with path.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise ValueError("CSV не содержит заголовка")
        data = []
        for row in reader:
            """
            Превращаем значения в строки
            """
            data.append({k: str(v) for k, v in row.items()})

    if not data:
        raise ValueError()

    with Path(json_path).open("w", encoding="utf-8") as out:
        json.dump(data, out, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    json_to_csv("data/lab05/samples/people.json",
                "data/lab05/out/people_from_json.csv")
    csv_to_json("data/lab05/samples/people.csv",
                "data/lab05/out/people_from_csv.json")
