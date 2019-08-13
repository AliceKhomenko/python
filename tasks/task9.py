# Создайте программу, вычисляющую факториал натурального числа n, которое пользователь введёт
# с клавиатуры.

def factorial(number):
    f = 1
    for i in range(number):
        f = f * (i+1)
    return f


number = int(input("Input your number:"))
if number > 0:
    print("Factorial is ", factorial(number))
else:
    print("Your number is too small")
