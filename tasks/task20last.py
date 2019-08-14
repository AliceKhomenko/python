# В три переменные a, b и c явно записаны программистом три целых попарно неравных между собой числа. Создать программу,
# которая переставит числа в переменных таким образом, чтобы при выводе на экран последовательность a, b и c
# оказалась строго возрастающей.

a = int(input("Input first number: "))
b = int(input("Input second number: "))
c = int(input("Input third number: "))
list = []
max = c
medium = b
min = a
if a < b:
    if c < a:
        min = c
        medium = a
        max = b
    elif c<b:
        medium = c
        max = b
else:
    if c < b:
        min = c
        medium = b
        max = a
    else:
        min = b
        if c < a:
            medium = c
            max = a
        else:
            medium = a
            max = c

print(min)
print(medium)
print(max)
