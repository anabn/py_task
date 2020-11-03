# 7. Найти минимальный элемент, значение и индекс.
def array_min(localArray):
    min = 0
    if len(localArray) == 0:
        return min
    else:
        for i in localArray:
            if (isinstance(i, int) | isinstance(i, float)):
                if i <= min:
                    min = i
    answer = [min, localArray.index(min)]
    return answer