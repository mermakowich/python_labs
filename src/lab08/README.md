## Лаба №8

### Задание A `src/lab08/models.py`

Создан класс **`Student`**, содержащий:

- декоратор `@dataclass`
- поля:
  - `fio`
  - `birthdate`
  - `group`
  - `gpa`
- методы:
  - `age()`. Высчитывает возраст с помощью библиотеки `datetime`
  - `to_dict()`. Создаёт словарь, готовый для конвертации в JSON-файл
  - `from_dict()`. Используем `@classmethod` для создания нового словаря
  - `__str__()`. Делаем красивый вывод через f-строку
- валидацию в `__post_init__`:
  - формата даты (`YYYY-MM-DD`)
  - диапазона среднего балла `0 ≤ gpa ≤ 5`


### Задание B `serialize.py`

`students_to_json(students, path)`

Сохраняет список студентов в JSON.

`students_from_json(path) -> list[Student]`

-   читает JSON-массив
-   валидирует
-   создаёт список `Student`

#### Пример запуска теста

students_input.json
![Картинка 1](./images/lab08/json_input.png)

тесты в `serialize.py`
![Картинка 1](./images/lab08/tests.png)

вывод в теримнал
![Картинка 1](./images/lab08/output_tests.png)

students_output.json
![Картинка 1](./images/lab08/json_output.png)