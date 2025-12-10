import csv
from pathlib import Path

from src.lab08.models import Student

class Group:

    HEADER = ["fio", "birthdate", "group", "gpa"]

    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        # создаём файл с заголовком, если не существует
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with self.path.open("w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(self.HEADER)

    def list(self):
        """
        Возвращает всех студентов как объекты Student
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
        Добавляет студента в конец CSV
        """
        d = student.to_dict()
        row = {k: d[k] for k in self.HEADER}
        with self.path.open("a", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.HEADER)
            writer.writerow(row)

    def find(self, substr: str):
        """
        Находит студентов по подстроке fio, независимо от регистра
        """
        substr_lower = substr.lower()
        matched = []
        try:
            with self.path.open("r", encoding="utf-8", newline="") as f:
                rows = csv.DictReader(f)
                for r in rows:
                    if set(self.HEADER).issubset(r.keys()) and substr_lower in r["fio"].lower():
                        s = Student.from_dict(r)
                        matched.append(s)
        except FileNotFoundError:
            pass
        return matched

    def remove(self, fio: str):
        """
        Удаляем запись с данным fio при полном совпадении (регистр влияет)
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

        with self.path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.HEADER)
            writer.writeheader()
            for r in rows:
                writer.writerow(r)


    def update(self, fio: str, **fields):
        """
        Обновляем поля первого найденного студента по fio
        Поддерживаемые поля для обновления: fio, birthdate, group, gpa
        """
        allowed = set(self.HEADER)
        for k in fields.keys():
            if k not in allowed:
                raise ValueError("Неизвестное поле")

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

        with self.path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.HEADER)
            writer.writeheader()
            for r in rows:
                writer.writerow(r)