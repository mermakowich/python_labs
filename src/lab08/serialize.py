import json
from pathlib import Path
from src.lab08.models import Student


def students_to_json(students, path):
    """
    Сохраняем список студентов в JSON
    """
    p = Path(path)
    data = [s.to_dict() for s in students]
    text = json.dumps(data, ensure_ascii=False, indent=2)
    p.write_text(text, encoding="utf-8")


def students_from_json(path: str | Path) -> list[Student]:
    """
    Читаем JSON и возвращает список Student
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Файл не найден: {p}")

    text = p.read_text(encoding="utf-8")
    data = json.loads(text)

    if not isinstance(data, list):
        raise ValueError("Ожидается JSON-массив объектов студентов")

    students = []

    for item in data:
        if not isinstance(item, dict):
            raise ValueError("Каждый элемент массива должен быть dict")
        student = Student.from_dict(item)
        students.append(student)

    return students


if __name__ == "__main__":
    print("проверка\n")

    students = students_from_json("data/lab08/students_input.json")
    print("прочитали студентов из JSON:")
    for s in students:
        print(s, " age:", s.age())

    students_to_json(students, "data/lab08/students_output.json")

    students2 = students_from_json("data/lab08/students_output.json")
    print()
    print("проверка, что всё хорошо записалось:")
    for s in students2:
        print(s)
