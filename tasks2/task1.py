#Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].

#Выведите все элементы, которые меньше 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a:
    if i<5:
        print(i)

print("Second variant")
i=0
while a[i]<5:
    print(a[i])
    i+=1


def fun(x):
    if (x<5):
        return 1
    else:
        return 0


print(list(filter(lambda x: x<5, a)))

print(list(filter(fun, a)))
print([i for i in a if i < 5])

print([i for i in a if i%2==0])



