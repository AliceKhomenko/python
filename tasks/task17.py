# В три переменные a, b и c записаны три вещественных числа. Создать программу, которая будет находить и выводить на
# экран вещественные корни квадратного уравнения ax²+bx+c=0, либо сообщать, что корней нет.
import math

def abc(a, b, c):
    D = b * b - 4 * a * c
    print(math.sqrt(D))
    if (D < 0):
        print("There is no solutions")
    elif (D == 0):
        print("There is one solution:")
        x1 = (-b) / (2 * a)
        print("x1=x2=", x1)
    else:
        print("There are two solutions")
        x1 = (-b - math.sqrt(D)) / (2 * a)
        x2 = (-b + math.sqrt(D)) / (2 * a)
        print("x1=",x1)
        print("x2=", x2)


abc(3,-4,1)