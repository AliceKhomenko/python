# Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,
# и возвращающую True, если оно простое, и False - иначе.
from math import sqrt


def is_prime(a):
    if type(a) is not int:
        print("It's not number")
        return None
    elif a < 0 or a > 10000:
        print("Not in range")
    else:
        return all(a % i for i in range(2, int(sqrt(a))))


print(is_prime(17))
print(is_prime(10))
print(is_prime('x'))
