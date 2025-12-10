import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("Hello\r\nWorld", "hello world"),
        ("", ""),
        ("\n\t ", ""),
    ],
)
def test_normalize(source, expected):
    assert normalize(source) == expected


@pytest.mark.parametrize(
    "source, expected",
    [
        ("Привет, мир!", ["привет", "мир"]),
        ("Москва-город", ["москва-город"]),
        ("test-case", ["test-case"]),
        ("hello world", ["hello", "world"]),
        ("", []),
        ("123 abc 456", ["123", "abc", "456"]),
    ],
)
def test_tokenize(source, expected):
    tokens = tokenize(normalize(source))
    assert tokens == expected


@pytest.mark.parametrize(
    "tokens, expected",
    [
        (["привет", "мир", "привет"], {"мир": 1, "привет": 2}),
        (["a", "b", "a", "a"], {"a": 3, "b": 1}),
        ([], {}),
        (["test"], {"test": 1}),
    ],
)
def test_count_freq(tokens, expected):
    assert count_freq(tokens) == expected


def test_count_freq_sorted():
    """
    Проверка сортировки по алфавиту
    """
    tokens = ["b", "a", "b", "c"]
    result = count_freq(tokens)
    assert list(result.keys()) == ["b", "a", "c"]


@pytest.mark.parametrize(
    "freq, n, expected",
    [
        ({"a": 3, "b": 1}, 2, [("a", 3), ("b", 1)]),
        ({"x": 1, "y": 1, "z": 1}, 2, [("x", 1), ("y", 1)]),
        ({"c": 5, "a": 10, "b": 7}, 3, [("a", 10), ("b", 7), ("c", 5)]),
        ({}, 5, []),
    ],
)
def test_top_n(freq, n, expected):
    assert top_n(freq, n) == expected


def test_top_n_tie_breaker():
    """
    Проверка сортировки по алфавиту при равной частоте
    """
    freq = {"c": 5, "a": 5, "b": 5}
    result = top_n(freq, 3)
    assert result == [("a", 5), ("b", 5), ("c", 5)]
