"""
Модуль для конвертации CSV в XLSX.
"""

import csv
from pathlib import Path
from openpyxl import Workbook

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX (лист "Лист1", автоширина >=8).
    
    Читаем CSV через csv.reader().
    Создаем Workbook, лист "Лист1".
    Добавляем строки через ws.append().
    Устанавливает ширину колонок, равную 12 через ws.column_dimensions[].width
    
    Аргументы:
        csv_path: путь к CSV.
        xlsx_path: путь к XLSX.
    
    Ошибки:
        FileNotFoundError: если CSV не найден.
        ValueError: если CSV пустой.
    """
    path = Path(csv_path)
    if not path.exists():
        raise FileNotFoundError()
    
    wb = Workbook()
    ws = wb.active
    ws.title = "Лист1"
    
    with path.open("r", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows_count = 0
        for row in reader:
            if not row:
                continue
            ws.append(row)
            rows_count += 1
    
    if rows_count == 0:
        raise ValueError("CSV пустой")
    
    for col in ws.columns:
        for cell in col:
            ws.column_dimensions[cell.column_letter].width = 12

    wb.save(xlsx_path)

if __name__ == "__main__":
    csv_to_xlsx("data/lab05/samples/cities.csv", 
                "data/lab05/out/cities_from_csv.xlsx")
    csv_to_xlsx("data/lab05/samples/people.csv", 
                "data/lab05/out/people_from_csv.xlsx")