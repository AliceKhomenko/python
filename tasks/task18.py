#Создать программу, которая будет проверять попало ли случайно выбранное из отрезка [5;155] целое число в интервал
# (25;100) и сообщать результат на экран.

import random

a=random.randint(5,155)
print("Random number is ",a)
if a<25 or a>100:
    print("Out of range")
else:
    print("In range")

