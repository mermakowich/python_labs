# python_labs
## Лаба №1
### Задание 1
```python
name = input("Имя: ")
age = int(input("Возраст: "))
print(f"Привет, {name}! Через год тебе будет {age+1}.")
```
![Картинка 1](./images/lab01/01.png)

### Задание 2
```python
a = float(input("a: "))
b = float(input("b: "))
print(f"sum={a+b:.2f}; avg={(a+b)/2:.2f}")
```
![Картинка 2](./images/lab01/02.png)

### Задание 3
```python
price, discount, vat = map(float, input("Введите price (руб.), discount (%), vat (%) через запятую: ").split(","))
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f"База после скидки: {base:.2f} ₽")
print(f"НДС:               {vat_amount:.2f} ₽")
print(f"Итого к оплате:    {total:.2f} ₽")
```
![Картинка 3](./images/lab01/03.png)

### Задание 4
```python
m = int(input("Минуты: "))
hours = m // 60
minutes = m % 60
print(f"{hours}:{minutes:02d}")
```
![Картинка 4](./images/lab01/04.png)

### Задание 5
```python
m = list(input("ФИО: ").split())
print(f"Инициалы: {m[0][0]+m[1][0]+m[2][0]}.")
print(f"Длина (символов): {len(m[0])+len(m[1])+len(m[2]) + 2}")
```
![Картинка 5](./images/lab01/05.png)

## Лаба №3
### Задание А - text.py

1. Функция normalize. Возвращает нормализованную строку.
```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """
    Функция нормализует строку через casefold, меняет все ё/Ë на е/Е и убирает лишние пробелы
    """
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")
    text = " ".join((text.replace("\t", " ").replace("\r", " ").replace("\n", " ")).split())
    return text
```
Исходные данные
- `"ПрИвЕт\nМИр\t"`
- `"ёжик, Ёлка" (yo2e=True) `
- `"Hello\r\nWorld"`
- `"  двойные   пробелы  "`

Выходные данные
![Картинка 1](./images/lab03/normalize.png)

2. Функция tokenize. Возвращает масив токенов по маске.
```python
def tokenize(text: str) -> list[str]:
    """
    Функция разбивает на «слова» по небуквенно-цифровым разделителям, возвращает массив токенов
    """
    tokens = re.findall(r'\w+(?:-\w+)*', text)
    return tokens
```
Исходные данные
- `"привет мир"`
- `"hello,world!!!"`
- `"по-настоящему круто"`
- `"2025 год"`
- `"emoji 😀 не слово"`

Выходные данные
![Картинка 2](./images/lab03/tokenize.png)

3. Функция count_freq. Возвращает словарь `слово → количество`.
```python
def count_freq(tokens: list[str]) -> dict[str, int]:
    """
    Функция создаёт множество из полученного массива токенов, для каждого элемента множества считает частоту в исходном массиве
    и записывает в словарь
    """
    dict_list = {}
    set_list = set(tokens)
    for token in set_list:
        dict_list[token] = tokens.count(token)
    return dict(sorted(dict_list.items()))
```
Исходные данные
- `["a","b","a","c","b","a"]`
- `["bb","aa","bb","aa","cc"]`

Выходные данные
![Картинка 3](./images/lab03/count_freq.png)

4. Функция top_n. Возвращает массив кортежей топ-N по убыванию частоты, при равенстве - по алфавиту.
```python
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """
    Функция сортирует items словаря частот и выводит первые N значений
    """
    sorted_items = sorted(freq.items())
    return sorted_items[:n]
```
Исходные данные
- `["a","b","a","c","b","a"], n=2`
- `["bb","aa","bb","aa","cc"], n=2`

Выходные данные
![Картинка 3](./images/lab03/top_n.png)

### Задание 2 - text_stats.py

Вводим через `stdin` через команду `sys.stdin.read()`

Далее вызываем команды из text.py

```python
import sys
from text import normalize, tokenize, count_freq, top_n

text = sys.stdin.read()
    
normalized_text = normalize(text)
tokens = tokenize(normalized_text)
freq = count_freq(tokens)

print(f"Всего слов: {len(tokens)}")
print(f"Уникальных слов: {len(freq)}")
print("Топ-5:")
for word, count in top_n(freq, 5):
    print(f"{word}:{count}")
```

Ввод
`$ echo "Привет, мир! Привет!!!" | python src/text_stats.py`

Вывод
![Картинка 7](./images/lab03/text_stats.png)
