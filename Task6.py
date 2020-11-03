# 6. Найти максимальный элемент, значение и индекс.
def array_max(localArray):
    max = 0
    if len(localArray) == 0:
        return max
    else:
        for i in localArray:
            if (isinstance(i, int) | isinstance(i, float)):
                if i >= max:
                    max = i
    answer = [max, localArray.index(max)]
    return answer