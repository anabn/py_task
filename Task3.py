# 3. Напишите функцию, которая принимает на вход два параметра: a и b.
# если тип обоих переменных (a и b) - int, вывести большее из них
# если тип обоих переменных строка - сообщить, является ли строка b подстрокой строки a
# если переменные разного типа, вывести сообщение об ошибке (любое)

def functionInRequest(paramA, paramB):
    try:
        if isinstance(paramA, int) & isinstance(paramB, int):
            if paramA > paramB:
                print("our parameters are int; the bigger is : " + str(paramA))
            elif paramB > paramA:
                print("our parameters are int; the bigger is : " + str(paramB))
            else:
                print("our parameters are int and this parameters are equals")
        elif isinstance(paramA, str) & isinstance(paramB, str):
            if str(paramA).find(paramB) != -1:
                print("our parameters are str; the str b is a part str a")
            else:
                print("our parameters are str; the str b is NOT a part str a")
        else:
            raise TypeError("Error, incorrect parameters' type")
    except TypeError as e:
        print(e)
