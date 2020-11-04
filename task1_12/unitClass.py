import unittest 
from random import randint
import Task2, Task11
from Task1 import Task1

def fill(lst, elements = 10, max_int = 100):
    elem = []
    for _ in range(elements):
        elem.append(randint(0, max_int))
    return elem

class classForTest(unittest.TestCase):
    def setUp(self):
        self.task1 = Task1()

    def test_task1_equalsInRange(self):
        self.assertEqual(self.task1.getOddNumbersFromRange(2, 2), [])

    def test_task1_valueInArray(self):
        x = 4
        self.assertFalse(x in self.task1.getOddNumbersFromRange(randint(-x, x), randint(-x, x)))
    
    def test_task2_zeroInFib(self):
        self.assertTrue(0 not in Task2.cutByRangeFibonacci(0, 3))

    def test_task2_fibValueForOne(self):
        self.assertTrue(1 in Task2.cutByRangeFibonacci(0, 3))
    
    def test_task11_checkSet(self):
        arrayA = [1, 2, 34, "hello"]
        arrayB = ["hello"]
        self.assertEqual(Task11.compareTwoArrays(arrayA, arrayB=[1, 2, 34]), arrayB)

if __name__ == '__main__':
    unittest.main()
