# 8. Посчитать количество элементов больше нуля.
import operator
def array_count(localArray):
    array = list(filter(lambda x: (isinstance(x, int) | isinstance(x, float)) and (x > 0), localArray))
    return len(array)