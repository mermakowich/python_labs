import sys
import argparse
from pathlib import Path

"""
Делаем относительный импорт
"""
from .io_txt_csv import *
from ..lib.text import *

"""
Скрипт читает входной файл data/lab04/input.txt,
Нормализует, токенизирует и считает частоты слов прочитанного файла,
Сохраняет data/lab04/report.csv c колонками: word,count, отсортированными: count ↓, слово ↑ (при равенстве),
Выводит в консоль краткое резюме.
"""


def main():
    """
    С помощью библиотеки parser читаем команду из командной строки,
    По умолчанию ставим базовые пути и кодировку UTF-8,
    Записываем аргументы в args
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--in", "-i", dest="input_path", default="data/lab04/input.txt")
    parser.add_argument(
        "--out", "-o", dest="output_path", default="data/lab04/report.csv"
    )
    parser.add_argument("--encoding", default="utf-8")
    args = parser.parse_args()

    """
    Читаем текст, с помощью read_text из io_txt_csv.py
    """
    try:
        text = read_text(args.input_path, encoding=args.encoding)
    except FileNotFoundError:
        print(f"Ошибка: файл {args.input_path} не найден", file=sys.stderr)
        sys.exit(1)
    except UnicodeDecodeError:
        print(
            f"Ошибка: невозможно прочитать файл с кодировкой {args.encoding}",
            file=sys.stderr,
        )
        sys.exit(1)

    """
    Нормализуем, токенизируем, считаем частоту, сортируем count ↓, слово ↑ (при равенстве) с помощью lambda-функции
    """
    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    freq = count_freq(tokens)
    sorted_freq = sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))

    """
    Если файл пустой - записываем csv только с header
    """
    if sorted_freq:
        rows = [(w, str(c)) for w, c in sorted_freq]
        write_csv(rows, args.output_path, header=("word", "count"))
    else:
        write_csv([], args.output_path, header=("word", "count"))

    """
    Выводим саммари
    """
    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    freq = count_freq(tokens)
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, count in top_n(freq, 5):
        print(f"{word}:{count}")


if __name__ == "__main__":
    main()
