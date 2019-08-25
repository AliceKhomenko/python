#Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если
# год високосный, и False иначе

def is_year_leap(year):
    if year%4==0 and year%100==0:
        return True
    else:
        return False

print(is_year_leap(2016))
print(is_year_leap(2000))
print(is_year_leap(2019))