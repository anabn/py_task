# 1.  Получить список всех нечётных чисел на отрезке [a, b].
def getOddNumbers(localA, localB):
    return list(filter(lambda i: i % 2, range(localA, localB + 1)))

def getOddNumbersFromRange(a, b):
    print("get the odd numbers from a range: ")
    if b < a:
        a, b = b, a
    elif a == b:
        print("It's not a range: {a} == {b}".format(a = a, b = b))
        return []
    print("Your range is : [ %s, %s ] " % (a, b)) 
    return getOddNumbers(a, b)  