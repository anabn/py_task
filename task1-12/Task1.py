# 1.  Получить список всех нечётных чисел на отрезке [a, b].
def getOddNumbers(localA, localB):
    number_list = []
    for i in range(localA, localB + 1):
        if i % 2 != 0:
            number_list.append(i)
    return number_list

def getOddNumbersFromRange(a, b):
    print("get the odd numbers from a range: ")
    tempList = []
    if a < b:
        print("Your range is : [ " + str(a) + ", " + str(b) + " ] ")
        tempList = getOddNumbers(a, b)
    elif b < a:
        print("Your range is : [ " + str(b) + ", " + str(a) + " ] ")
        tempList = getOddNumbers(b, a)
    else:
        print("It's not a range: " + str(a) + " == " + str(b))
    return tempList