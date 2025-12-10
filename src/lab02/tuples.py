def format_record(rec: tuple[str, str, float]) -> str:
    fio = list(rec[0].split())
    group = rec[1]
    gpa = rec[2]

    if not fio or not group or not isinstance(gpa, float):
        return "TypeError"

    if len(fio) == 3:
        return f"{fio[0].capitalize()} {fio[1][0].upper()}.{fio[2][0].upper()}, гр. {group}, GPA {gpa:.2f}"
    if len(fio) == 2:
        return f"{fio[0].capitalize()} {fio[1][0].upper()}., гр. {group}, GPA {gpa:.2f}"


print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
