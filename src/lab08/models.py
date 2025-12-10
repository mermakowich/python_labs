from datetime import date, datetime
from dataclasses import dataclass

DATE_FORMAT = "%Y-%m-%d"


@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        try:
            datetime.strptime(self.birthdate, DATE_FORMAT)
        except ValueError as e:
            raise ValueError(
                "Некорректный формат даты рождения: {self.birthdate}. "
                f"Введите в формате YYYY-MM-DD."
            ) from e

        if not (0 <= self.gpa <= 5):
            raise ValueError("gpa должен быть в диапазоне 0..5")

    def age(self):
        b = datetime.strptime(self.birthdate, DATE_FORMAT).date()
        today = date.today()
        years = today.year - b.year
        if (today.month, today.day) < (b.month, b.day):
            years -= 1
        return years

    def to_dict(self) -> dict:
        """
        Делаем dict, готовый для json
        """
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, d: dict):
        """
        Создаём Student из dict, например, полученного из json
        """
        return cls(
            fio=d["fio"],
            birthdate=d["birthdate"],
            group=d["group"],
            gpa=float(d["gpa"]),
        )

    def __str__(self):
        return f"{self.fio}, {self.group}, {self.gpa}"
