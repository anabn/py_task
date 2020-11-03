# 4. Напишите функцию, которая принимает на вход три параметра: начальный год (a),
# конечный год (b), список годов (c). функцию должна вернуть список високосных лет между а і b, 
# кроме тех которые указаны у списку c.

def listOfLeapYearsOnRange(a, b, c):
    localList = []
    for year in range(a, b + 1):
        if year % 4 == 0 or (year % 100 != 0 and year % 400 == 0):
            localList.append(year)
    # exclude from list c
    return list(set(localList) - set(c))
    

