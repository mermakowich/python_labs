def isrectangle(mat: list[list[float or int]]):
    """
    Функция проверяет прямоугольность НЕПУСТОЙ матрицы
    """
    lenstr = len(mat[0])
    for line in mat:
        if len(line) == lenstr:
            continue
        else:
            return False
    return True

print("transpose")
def transpose(mat: list[list[float or int]]) -> list[list]:
    """
    Проверка на пустой массив и непрямоугольность
    """
    if mat == []:
        return []
    if not isrectangle(mat):
        return "ValueError"
    """
    Меняет строки и столбцы местами, trans - новый массив
    """
    trans = [[] for k in range(len(mat[0]))]
    for i in range(len(mat)):
        for k in range(len(mat[i])):
            trans[k].append(mat[i][k])
    return trans

print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))


print()
print("row_sums")

def row_sums(mat: list[list[float or int]]) -> list[float]:
    """
    Проверка на пустой массив и непрямоугольность
    """
    if mat == []:
        return []
    if not isrectangle(mat):
        return "ValueError"
    """
    Заходим в каждую строку и получаем сумму элементов строки, которую помещаем в массив row_sum
    """
    row_sum = []
    for i in range(len(mat)):
        lensum = 0
        for k in range(len(mat[i])):
            lensum += mat[i][k]
        row_sum.append(lensum)
    return row_sum
    
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))


print()
print("col_sums")

def col_sums(mat: list[list[float or int]]) -> list[float]:
    """
    Проверка на пустой массив и непрямоугольность
    """
    if mat == []:
        return []
    if not isrectangle(mat):
        return "ValueError"

    """
    Заходит в каждый столбец и суммирует элементы, сумма помещается в col_sum
    """
    col_sum = []
    for i in range(len(mat[0])):
        lencol = 0
        for k in range(len(mat)):
            lencol += mat[k][i]
        col_sum.append(lencol)
    return col_sum

print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))