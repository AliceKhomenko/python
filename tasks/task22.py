# Случайная строка вводится пользователем. Пользователь может вводить строки до тех пор,
# пока он не введет exit. после этого вывести все строки ,которые пользователь вводил.

s = input("Input your string:")
old_text = ""
result_string = ""
while s !='exit':
    # old_text = s
    text = old_text + s
    old_text = text
    s = input("Input your string:")

print(old_text)
