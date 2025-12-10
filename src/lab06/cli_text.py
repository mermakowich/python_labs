"""
CLI-утилиты для работы с текстом (лабораторная №6).
Использует функции анализа текста из лабораторной №3.
"""

import argparse
from pathlib import Path
import re

from ..lib.text import normalize, tokenize, count_freq, top_n


def main() -> None:
    parser = argparse.ArgumentParser(description="CLI‑утилиты")
    subparsers = parser.add_subparsers(dest="command")

    cat_parser = subparsers.add_parser(
        "cat", help="Вывод содержимого файла построчно (с нумерацией при -n)"
    )
    cat_parser.add_argument("--input", required=True, help="Путь к файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Анализ частот слов в тексте")
    stats_parser.add_argument("--input", required=True, help="Путь к файлу txt")
    stats_parser.add_argument("--top", type=int, default=5, help="Топ слов по частотам")

    args = parser.parse_args()

    if args.command == "cat":
        path = Path(args.input)
        if not path.exists():
            raise FileNotFoundError("Файл не найден")
        with path.open(encoding="utf-8") as f:
            if args.n:
                for num, line in enumerate(f, 1):
                    print(f"{num:6}  {line.rstrip()}")
            else:
                for line in f:
                    print(line.rstrip())

    elif args.command == "stats":
        path = Path(args.input)
        if not path.exists():
            raise FileNotFoundError("Файл не найден")

        with path.open(encoding="utf-8") as f:
            text = f.read()

        normalized = normalize(text)
        tokens = tokenize(normalized)
        freq = count_freq(tokens)
        top_words = top_n(freq, args.top)

        for word, count in top_words:
            print(f"{word}\t{count}")


if __name__ == "__main__":
    main()
