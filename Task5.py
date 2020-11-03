# 5. Найти сумму элементов массива.
def array_sum(localArray):
    sum = 0
    if len(localArray) == 0:
        return sum
    else:
        for i in localArray:
            if isinstance(i, int) | isinstance(i, float):
                sum += i
    return sum
                
