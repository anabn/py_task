# 11. Вывести элементы одного массива, которые не равны элементам второго массива.
def compareTwoArrays(arrayA, arrayB):
    return list(set(arrayA) - set(arrayB))