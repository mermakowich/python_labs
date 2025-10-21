print("min-max")

def min_max(nums: list[float or int]) -> tuple[float or int, float or int]:
    """
    Вовзвращаем минимальное и максмальное значение массива
    """
    if not nums:
        return "ValueError"
    return (min(nums), max(nums))

print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([]))
print(min_max([1.5, 2, 2.0, -3.1]))


print()
print("unique_sorted")

def unique_sorted(nums: list[float or int]) -> list[float or int]:
    """
    Возвращаем отсортированный список уникальных значений
    """
    if not nums:
        return []
    return sorted(set(nums))

print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))


print()
print("flatten")

def flatten(mat: list[list or tuple]) -> list:
    """
    <Плющим> строки списка списков/кортежей в один список
    """
    row_major = []
    for i in range(len(mat)):
        if isinstance(mat[i], list) or isinstance(mat[i], tuple):
            
            for k in range(len(mat[i])):
                row_major.append(mat[i][k])
        else:
            return "TypeError"
    return row_major

print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))
