import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")
    text = " ".join((text.replace("\t", " ").replace("\r", " ").replace("\n", " ")).split())
    return text 

def tokenize(text: str) -> list[str]:
    tokens = re.findall(r'\b\w+(?:-\w+)*\b', text)
    return tokens

def count_freq(tokens: list[str]) -> dict[str, int]:
    dict_list = {}
    set_list = set(tokens)
    for token in set_list:
        dict_list[token] = tokens.count(token)
    return dict(sorted(dict_list.items()))

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sorted_items = sorted(freq.items())
    return sorted_items[:n]


def main():
    print("normalize")
    print(normalize("ПрИвЕт\nМИр\t"))
    print(normalize("ёжик, Ёлка", yo2e=True))
    print(normalize("Hello\r\nWorld"))
    print(normalize("  двойные   пробелы  "))
    print()

    print("tokenize")
    print(tokenize("привет мир"))
    print(tokenize("hello,world!!!"))
    print(tokenize("по-настоящему круто"))
    print(tokenize("2025 год"))
    print(tokenize("emoji 😀 не слово"))
    print()

    print("count_freq")
    print(count_freq(["a","b","a","c","b","a"]))
    print(count_freq(["bb","aa","bb","aa","cc"]))
    print()

    print("top_n")
    print(top_n({"a":3,"b":2,"c":1}, n=2))
    print(top_n({"aa":2,"bb":2,"cc":1}, n=2))

if __name__ == '__main__':
    main()