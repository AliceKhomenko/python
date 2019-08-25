d = {a+2: a * 2 for a in range(7)}
print(d)
print(d[3])

d[3]=11
print(d[3])

b=d.copy()

print(b)