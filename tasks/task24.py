import random

list = []
chet = 0
nechet = 0
for i in range(20):
    list.append(random.randint(0,100))

print(list)
for i in list:
    if i >=70:
        print("Find! ",i)
        break

