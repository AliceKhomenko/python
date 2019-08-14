#В три переменные a, b и c явно записаны программистом три целых попарно неравных между собой числа. Создать программу,
# которая переставит числа в переменных таким образом, чтобы при выводе на экран последовательность a, b и c
# оказалась строго возрастающей.

a=int(input("Input first number: "))
b=int(input("Input second number: "))
c=int(input("Input third number: "))
list=[]
max=c
medium=b
min =a
if a<b:
    if c<a:
        min=c
        medium=a
        max=b
    elif c==a:
        min,medium=a,a
        max=b
    else:
        if c<b:
            medium=c
            max=b
        elif c==b:
            medium,max=b,b
elif a==b:
    if c<a:
        min=c
        medium,max=a,a
    elif c>a:
        min,medium=a,a
        max=c
    else:
        min,medium,max=a,a,a
else:
    if c<b:
        min=c
        medium=b
        max=a
    elif c==b:
        min,medium=b,b
        max=a
    else:
        min=b
        if c<a:
            medium=c
            max=a
        elif c==a:
            medium,max=c,c
        else:
            medium=a
            max=c



print(min)
print(medium)
print(max)

