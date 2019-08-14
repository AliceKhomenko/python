# Создать программу, проверяющую и сообщающую на экран, является ли целое число записанное в переменную n, чётным либо нечётным.
try:
    a = int(input('Input your number:'))
    if a != 0:
        if a % 2 == 0:
            print('Even number')
        else:
            print('Not even number')
    else:
        print("Your nuamber is 0")
except ValueError:
    print("Wrong value")
