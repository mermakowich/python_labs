from pathlib import Path
import csv
from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    '''
    Функция читает текст и из файла и возвращает как одну строку.
    Каждая новая строка склеивается с предыдущей через пробел.

    Если файл не найден, возникает FileNotFoundError, функция падает.
    Если кодировка не подходит, возникает UnicodeDecodeError, функция падает.

    Параметры:
    path - путь к файлу
    encoding - кодировка, по умолчанию "utf-8"
    '''
    p = Path(path).read_text(encoding=encoding)
    return p.replace("\n", " ")

def write_csv(rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    '''
    Функция создаёт или перезаписывает CSV с разделителем ",".
    header (если есть), всегда записывается первой строкой.

    Если rows имеют разную длину, то поднимаем ValueError 
    Если rows пустой и header=None создаётся пустой CSV

    Параметры:
    rows - строки CSV файла
    path - путь к файлу
    header - заголовки столбцов
    '''
    p = Path(path)
    rows = list(rows)
    with p.open('w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        if not rows:
            if header is not None:
                writer.writerow(header)
            return
        row_len = len(rows[0])
        for r in rows:
            if len(r) != row_len:
                raise ValueError("Все строки в rows должны иметь одинаковую длину")
        if header is not None:
            writer.writerow(header)
        writer.writerows(rows)


def main():
    print("read_text")
    print(read_text("data/lab04/input.txt", "utf-8"))
    print()
    
    

if __name__ == '__main__':
    main()