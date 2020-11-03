# 9. Прибавить к элементам массива их индекс.
def array_increase_index(localArray):
    localArrayCopy = []
    if len(localArray) == 0:
        return localArrayCopy[0]
    else:
        for i in localArray:
            if (isinstance(i, int) | isinstance(i, float)):
                localArrayCopy.append(i + localArray.index(i))
    return localArrayCopy