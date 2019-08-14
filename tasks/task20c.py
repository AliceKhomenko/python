#В три переменные a, b и c явно записаны программистом три целых попарно неравных между собой числа. Создать программу,
# которая переставит числа в переменных таким образом, чтобы при выводе на экран последовательность a, b и c
# оказалась строго возрастающей.

a=int(input("Input first number: "))
b=int(input("Input second number: "))
c=int(input("Input third number: "))
list=[a,b,c]
new_list=[]
is_sorted=False
while(is_sorted==False):
    is_sorted=True
    for j in range(len(list)-1):
        if list[j]>list[j+1]:
            is_sorted=False
            temp=list[j]
            list[j]=list[j+1]
            list[j+1]=temp
print(list)

