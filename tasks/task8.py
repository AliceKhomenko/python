# Выведите на экран все положительные делители натурального числа, введённого пользователем
# с клавиатуры.
import math

number = int(input("Input your number: "))
d = 2
list = []
if number > 2:
    list.append(1)
    while d <= number:
        if number % d == 0:
            list.append(d)
        d += 1
        if len(list) == 1 and (d > math.sqrt(number)):
            list.append(number)
            print("It is a prime number")
            break
else:
    print("Your number is too small")
print(list)
