## Лаба №7

### Задание A. Тесты для `src/lib/text.py`

Написаны автотесты для всех публичных функций модуля:

- `normalize(text: str) -> str`
- `tokenize(text: str) -> list[str]`
- `count_freq(tokens: list[str]) -> dict[str, int]`
- `top_n(freq: dict[str, int], n: int) -> list[tuple[str, int]]`

Проверены базовые и граничные случаи, одинаковые частоты слов  
Использован `@pytest.mark.parametrize`

#### Пример запуска теста

`python -m pytest tests/test_text.py`
![Картинка 1](./images/lab07/test_text.png)


### Задание B. Тесты для `src/lab05/json_csv.py`

Написаны автотесты для функций:
- `json_to_csv(src_path: str, dst_path: str)`
- `csv_to_json(src_path: str, dst_path: str)`

Функции корректно работают, 
- при пустом или некорректном входном файле получаем `ValueError`;
- при несуществующем пути к файлу получаем `FileNotFoundError`.

Использована фикстура `tmp_path` для создания тестовых файлов

#### Пример запуска теста

`python -m pytest tests/test_json_csv.py`
![Картинка 1](./images/lab07/test_json_csv.png)


#### Общее покрытие тестами

`pytest --cov=src --cov-report=term-missing`
![Картинка 1](./images/lab07/test_cov.png)

В строке `missing` видим, какие строки кода не покрыты тестами. Все тесты выполняются

### Задание C. Стиль

Отформатировано с помощью `black .`
![Картинка 1](./images/lab07/black.png)