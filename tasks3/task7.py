# Написать функцию date, принимающую 3 аргумента — день, месяц и год. Вернуть True,
# если такая дата есть в нашем календаре, и False иначе.

import calendar


def date(year, month, day):
    try:
        calendar.weekday(year, month, day)
        return True
    except ValueError:
        return False


print(date(2019, 13, 25))
print(date(2019, 8, 25))

