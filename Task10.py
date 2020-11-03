# 10. Циклический сдвиг элементов массива на k- позиций вправо.
def shiftUsingPyFunction(localArray, k):
    k %= len(localArray)
    return localArray[-k:] + localArray[:-k]

def shift_algorithm(localArray, k):
    size = len(localArray)
    if size == 0 or size == 1: 
        return localArray
    else:
        lst = localArray[:]
        k %= size
        if k > 0:
            for i in range(k):
                lst.insert(0, lst.pop())
        elif k < 0:
            k = abs(k)
            for i in range(k):
                lst.append(lst.pop(0))
    return lst



