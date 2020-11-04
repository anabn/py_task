# This is a sample Python script.
import Task1, Task2, Task3, Task4, Task5, Task6, Task7, Task8, Task9, Task10, Task11, Task12
# Press the green button in the gutter to run the script.
    if __name__ == '__main__':
        print(" Enter first number : ")
        inputNumber1 = int(input())
        print(" Enter second number : ")
        inputNumber2 = int(input())
    # 1. Получить список всех нечётных чисел на отрезке [a, b].
        print("<--------- Task 1 --------->")
        print(Task1.getOddNumbersFromRange(inputNumber1, inputNumber2))
    # 2. Получить список всех чисел Фибоначчи на отрезке [a, b].
        print("<--------- Task 2 --------->")
        print(Task2.cutByRangeFibonacci(inputNumber1, inputNumber2))
    # 3. Напишите функцию, которая принимает на вход два параметра: a и b.
        print("<--------- Task 3 --------->")
        a = 12
        b = "str"
        print(" out parameters are : {a}, {b}".format(a = a, b = b))
        Task3.functionInRequest(a, b)
    # 4. Напишите функцию, которая принимает на вход три параметра
        print("<--------- Task 4 --------->")
    #     # leap years 
        c = [1900, 1904, 1908, 1964, 2020]
        startYear = 1900
        finishYear = 2020
        print(" our years' range : [ {s}, {f} ]".format(s = startYear, f = finishYear))
        print(" exclude list from range : %s " % c )
        print(Task4.listOfLeapYearsOnRange(startYear, finishYear, c))
    #  array for task 5-9
        array = [1, "sd", 3, 1.2, 5.6, 0, -1]
    # 5. Найти сумму элементов массива
        print("<--------- Task 5 --------->")
        print(" given array : %s " % array)
        print(" array sum :  %s " % Task5.array_sum(array))    
    # # 6. Найти максимальный элемент, значение и индекс.
        print("<--------- Task 6 --------->")
        print(" max in array and index : %s " % Task6.array_max(array))
    # 7. Найти минимальный элемент, значение и индекс.
        print("<--------- Task 7 --------->")
        print(" min in array and index : %s " % Task7.array_min(array))
    # 8. Посчитать количество элементов больше нуля.
        print("<--------- Task 8 --------->")
        print(" the amount of numbers greater than 0 : %s " % Task8.array_count(array))
    # 9. Прибавить к элементам массива их индекс.
        print("<--------- Task 9 --------->")
        print(" increase array by adding their index: %s " % Task9.array_increase_index(array))
    # 10. Циклический сдвиг элементов массива на k- позиций вправо.
        print("<--------- Task 10 --------->")
        k = 2
        print(" right step: %s " % k)
        print(" array to compare:\t\t %s" % array)
        print(" using python fuction:\t\t %s " % Task10.shiftUsingPyFunction(array, k))
        print(" using created algorithm:\t %s " % Task10.shiftUsingPyFunction(array, k))
    # 11. Вывести элементы одного массива, которые не равны элементам второго массива.
        print("<--------- Task 11 --------->")
        first_array = ['word', 1, 4, 10, 'hello']
        second_array = ['hello', 2, 5, 1]
        print(" initial first array : %s " % first_array)
        print(" initial second array : %s " % second_array)
        print(Task11.compareTwoArrays(first_array, second_array))
    # 12. Из двух отсортированных массивов сделать третий отсортированный, не сортируя его.
        print("<--------- Task 12 --------->")
        sortedArrayA = [2, 4, 8]
        sortedArrayB = [5, 2, 1]
        print(" initial first array (sorted in fuction): %s" % sortedArrayA)
        print(" initial second array ((sorted in fuction): %s" % sortedArrayB)
        print(Task12.sortTwoArraysInOne(sortedArrayA, sortedArrayB))
