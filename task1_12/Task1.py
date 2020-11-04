# 1.  Получить список всех нечётных чисел на отрезке [a, b].
class Task1:
    def __init__(self):
        pass
    def getOddNumbersFromRange(self, a, b):
        print("get the odd numbers from a range: ")
        if b < a:
            a, b = b, a
        elif a == b:
            print("It's not a range: {a} == {b}".format(a = a, b = b))
            return []
        print("Your range is : [ %s, %s ] " % (a, b)) 
        return self._getOddNumbers(a, b)  
    
    def _getOddNumbers(self, localA, localB):
        return list(filter(lambda i: i % 2, range(localA, localB + 1)))