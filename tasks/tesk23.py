import random

list = []
chet = 0
nechet = 0
for i in range(10):
    list.append(random.randint(0,20))

for i in list:
    print(i)
    if i != 0:
        if i % 2 == 0:
            chet += 1
        else:
            nechet += 1

print("Chet:{} Nechet:{}".format(chet,nechet))
