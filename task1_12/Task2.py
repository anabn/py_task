# 2. Получить список всех чисел Фибоначчи на отрезке [a, b].
def _fibonacci_numbers(localMax):
    if localMax == 0:
        return 0
    elif localMax == 1:
        return 1
    else:
        return _fibonacci_numbers(localMax - 1) + _fibonacci_numbers(localMax - 2)

def cutByRangeFibonacci(a, b):
    print("get the Fibonacci numbers in a range: ")
    tempFibonacciList = []
    if b < a:
        a, b = b, a
    elif a == b:
        print("It's not a range: {a} == {b}".format(a = a , b = b))
        return []
    print("Your range is : [ %s, %s ] " % (a, b)) 

    for i in range(1, b + 1):
        tempFibonacciList.append(_fibonacci_numbers(i))
    return tempFibonacciList[a:b]
