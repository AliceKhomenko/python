# Создать программу, выводящую на экран случайно сгенерированное трёхзначное натуральное число и его наибольшую цифру.

import random

number = random.randint(100, 999)
print("Random number is ",number)
a = number // 100

c = number % 10

b = number // 10 - a * 10
print(a)
print(b)
print(c)
max = a
if b > max:
    max = b
if c > max:
    max = c

print("The maximum value is ",max)