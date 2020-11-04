# 5. Найти сумму элементов массива.
import operator
def array_sum(localArray):
    array = list(filter(lambda x: isinstance(x, int) | isinstance(x, float), localArray))
    return sum(array)
                
