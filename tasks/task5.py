# Для введённого пользователем с клавиатуры натурального числа посчитайте сумму всех его цифр
# (заранее не известно сколько цифр будет в числе).

number = input("Enter a number:")
count = 0
for i in number:
    count += int(i)
print("count=", count)
