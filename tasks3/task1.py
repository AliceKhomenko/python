# Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция,
# которая должна быть произведена над ними. Если третий аргумент +, сложить их; если —,
# то вычесть; * — умножить; / — разделить (первое на второе). В остальных случаях вернуть
# строку "Неизвестная операция".

def arithmetic(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b
    else:
        print("Unknown operation")
        return None



print(arithmetic(25,5,"+"))
print(arithmetic(25,5,"-"))
print(arithmetic(25,5,"*"))
print(arithmetic(10,5,"/"))
print(arithmetic(10,5,"x"))