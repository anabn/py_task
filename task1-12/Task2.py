# 2. Получить список всех чисел Фибоначчи на отрезке [a, b].
def fibonacci_numbers(localMax):
    if localMax == 0:
        return 0
    elif localMax == 1:
        return 1
    else:
        return fibonacci_numbers(localMax - 1) + fibonacci_numbers(localMax - 2)

def cutByRangeFibonacci(a, b):
    print("get the Fibonacci numbers in a range: ")
    tempFibonacciList = []
    if a < b:
        print("Your range is : [ " + str(a) + ", " + str(b) + " ] ")
        for i in range(1, b + 1):
            tempFibonacciList.append(fibonacci_numbers(i))
    elif b < a:
        print("Your range is : [ " + str(b) + ", " + str(a) + " ] ")
        for i in range(1, b + 1):
            tempFibonacciList.append(fibonacci_numbers(i))
    else:
        print("It's not a range: " + str(a) + " == " + str(b))
    return tempFibonacciList[a:b]
