# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую
# время года, которому этот  месяц принадлежит (зима, весна, лето или осень).

def season(i):
    if i == 1 or i == 2 or i == 12:
        return 'Winter'
    elif i == 3 or i == 4 or i == 5:
        return 'Spring'
    elif i == 6 or i == 7 or i == 8:
        return 'Summer'
    elif i == 9 or i == 10 or i == 11:
        return 'Fall'
    else:
        print ('Unknown month')
        return None


print(season(12))
print(season(3))
print(season(8))
print(season(10))
print(season(-1))
