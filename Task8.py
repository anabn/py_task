# 8. Посчитать количество элементов больше нуля.
def array_count(localArray):
    count = 0
    if len(localArray) == 0:
        return count
    else:
        for i in localArray:
            if (isinstance(i, int) | isinstance(i, float)):
                if i > 0:
                    count += 1
    return count