# 6. Найти максимальный элемент, значение и индекс.
import operator
def array_max(localArray):
    array = list(filter(lambda x: isinstance(x, int) | isinstance(x, float), localArray))
    index, value = max(enumerate(array), key=operator.itemgetter(1)) 
    return [index, value]