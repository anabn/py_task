# 9. Прибавить к элементам массива их индекс.
import operator
def array_increase_index(localArray):
    localArrayCopy = []
    for index, value in enumerate(localArray):
        if (isinstance(value, int) | isinstance(value, float)):
            localArrayCopy.append(index + value)
    return localArrayCopy