# 7. Найти минимальный элемент, значение и индекс.
import operator
def array_min(localArray):
    array = list(filter(lambda x: isinstance(x, int) | isinstance(x, float), localArray))
    index, value = min(enumerate(array), key=operator.itemgetter(1)) 
    return [index, value]