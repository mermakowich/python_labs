import csv
from pathlib import Path

from src.lab08.models import Student
from src.lib.io_helpers import write_csv


class Group:
    """
    Класс для работы с базой данных студентов в формате CSV
    Реализует CRUD-операции: Create, Read, Update, Delete
    """

    HEADER = ["fio", "birthdate", "group", "gpa"]

    def __init__(self, storage_path: str):
        """
        Инициализирует группу и создаёт CSV-файл с заголовком, если не существует

        Параметры:
        storage_path - путь к CSV-файлу с данными студентов
        """
        self.path = Path(storage_path)
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            write_csv([], self.path, header=tuple(self.HEADER))

    def list(self) -> list[Student]:
        """
        READ: возвращает всех студентов как объекты Student

        Возвращает:
        список объектов Student
        """
        students = []
        try:
            with self.path.open("r", encoding="utf-8", newline="") as f:
                reader = csv.DictReader(f)
                for r in reader:
                    if set(self.HEADER).issubset(r.keys()):
                        s = Student.from_dict(r)
                        students.append(s)
        except FileNotFoundError:
            pass
        return students

    def add(self, student: Student):
        """
        CREATE: добавляет студента в конец CSV

        Параметры:
        student - объект Student для добавления
        """
        d = student.to_dict()
        row = [d[k] for k in self.HEADER]

        with self.path.open("a", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(row)

    def find(self, substr: str) -> list[Student]:
        """
        READ: находит студентов по подстроке в ФИО (без учёта регистра)

        Параметры:
        substr - подстрока для поиска в ФИО

        Возвращает:
        список найденных студентов
        """
        substr_lower = substr.lower()
        matched = []

        try:
            with self.path.open("r", encoding="utf-8", newline="") as f:
                reader = csv.DictReader(f)
                for r in reader:
                    if set(self.HEADER).issubset(r.keys()) and substr_lower in r["fio"].lower():
                        s = Student.from_dict(r)
                        matched.append(s)
        except FileNotFoundError:
            pass

        return matched

    def remove(self, fio: str):
        """
        DELETE: удаляет запись с данным ФИО при полном совпадении

        Параметры:
        fio - ФИО студента для удаления (точное совпадение)
        """
        rows = []
        try:
            with self.path.open("r", encoding="utf-8", newline="") as f:
                reader = csv.DictReader(f)
                for r in reader:
                    if set(self.HEADER).issubset(r.keys()):
                        rows.append(r)
        except FileNotFoundError:
            return

        for i, r in enumerate(rows):
            if r["fio"] == fio:
                rows.pop(i)
                break

        rows_as_tuples = [tuple(r[k] for k in self.HEADER) for r in rows]
        write_csv(rows_as_tuples, self.path, header=tuple(self.HEADER))

    def update(self, fio: str, **fields):
        """
        UPDATE: обновляет поля первого найденного студента по ФИО

        Параметры:
        fio - ФИО студента для обновления (точное совпадение)
        **fields - аргументы с новыми значениями полей CSV-файла

        Поднимаем ошибки:
        ValueError - если указано неизвестное поле
        """
        allowed = set(self.HEADER)
        for k in fields.keys():
            if k not in allowed:
                raise ValueError(f"Неизвестное поле: {k}")

        rows = []
        try:
            with self.path.open("r", encoding="utf-8", newline="") as f:
                reader = csv.DictReader(f)
                for r in reader:
                    if set(self.HEADER).issubset(r.keys()):
                        rows.append(r)
        except FileNotFoundError:
            return

        for r in rows:
            if r["fio"] == fio:
                for k, v in fields.items():
                    r[k] = str(v)
                Student.from_dict(r)
                break

        rows_as_tuples = [tuple(r[k] for k in self.HEADER) for r in rows]
        write_csv(rows_as_tuples, self.path, header=tuple(self.HEADER))


def main():
    group = Group("data/lab09/students.csv")

    print("CRUD-операции с базой данных студентов")
    print("\n1. READ: Список всех студентов")
    students = group.list()
    for s in students:
        print(f"  {s.fio} | {s.group} | GPA: {s.gpa}")

    print("\n2. CREATE: Добавление нового студента")
    new_student = Student(
        fio="Тестов Тест Тестович",
        birthdate="2004-05-15",
        group="БИВТ-21-3",
        gpa=4.0
    )
    group.add(new_student)
    print(f"  Добавлен: {new_student.fio}")
    students = group.list()
    for s in students:
        print(f"  {s.fio} | {s.group} | GPA: {s.gpa}")

    print("\n3. FIND: Поиск студентов по подстроке 'Тест'")
    found = group.find("Тест")
    for s in found:
        print(f"  {s.fio} | {s.group} | GPA: {s.gpa}")

    print("\n4. UPDATE: Обновление GPA студента")
    group.update("Тестов Тест Тестович", gpa=4.5)
    updated = group.find("Тестов")
    for s in updated:
        print(f"  {s.fio} | GPA: {s.gpa}")
    students = group.list()
    for s in students:
        print(f"  {s.fio} | {s.group} | GPA: {s.gpa}")

    print("\n5. DELETE: Удаление студента")
    group.remove("Тестов Тест Тестович")
    print("   Студент удалён")

    print("\n6. Финальный список студентов")
    students = group.list()
    for s in students:
        print(f"  {s.fio} | {s.group} | GPA: {s.gpa}")

if __name__ == "__main__":
    main()