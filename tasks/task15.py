# Создать программу, выводящую на экран ближайшее к 10 из двух чисел, записанных в переменные m и n.
# Например, среди чисел 8,5 и 11,45 ближайшее к десяти 11,45.


def compare(a, b, total_number=10):
    if abs(total_number - a) == abs(total_number - b):
        print('The numbers are equal')
    elif abs(total_number - a) > abs(total_number - b):
        print('Second number')
    else:
        print('First number')


try:
    a = int(input('Input first number: '))
    b = int(input('Input second number: '))
    compare(a, b)
except ValueError:
    print("Your numbers are incorrect")
