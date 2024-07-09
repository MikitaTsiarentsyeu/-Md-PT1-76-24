from datetime import time

"""
Implement a text output of the time entered from the console
(the user should input data in the format hh:mm).

Show the responses to the user in Russian according to the rules listed below:

min == 0: такое-то значение часа ровно (15:00 - три часа ровно)
min < 30: столько-то минут следующего часа (19:12 - двенадцать минут восьмого)
min == 30: половина такого-то (15:30 - половина четвёртого)
min > 30 and min < 45 столько-то минут следующего часа (12:38 - тридцать восемь минут первого)
min >= 45 без min такого-то (08:54 - без шести минут девять)
"""

plural_dict = {0: ("час", "часа", "часов"), 1: ("минута", "минуты", "минут")}

time_dict = {
    1: ['один', 'одной', 'второго', 'десять', 'одна', 'час'],
    2: ['два', 'двух', 'третьего', 'двадцать', 'две'],
    3: ['три', 'трех', 'четвертого', 'тридцать'],
    4: ['четыре', 'четырех', 'пятого', 'сорок'],
    5: ['пять', 'пяти', 'шестого', 'пятьдесят'],
    6: ['шесть', 'шести', 'седьмого', 'шестьдесят'],
    7: ['семь', 'семи', 'восьмого'],
    8: ['восемь', 'восьми', 'девятого'],
    9: ['девять', 'девяти', 'десятого'],
    10: ['десять', 'десяти', 'одиннадцатого'],
    11: ['одиннадцать', 'одиннадцати', 'двенадцатого'],
    12: ['двенадцать', 'двенадцати', 'первого'],
    13: ['тринадцать', 'тринадцати', ],
    14: ['четырнадцать', 'четырнадцати', ],
    15: ['пятнадцать', 'пятнадцати', ],
    16: ['шестнадцать', ],
    17: ['семьнадцать', ],
    18: ['восемнадцать', ],
    19: ['девятнадцать', ],

}


def choose_plural(amount, declensions):
    """
    return correct declination
    declinations takes hours or minutes
    """
    amount = amount % 100 if 11 <= amount % 100 <= 14 else amount % 10
    # returns the last number by which it will be inclined
    if amount == 1:
        return declensions[0]
    elif 1 < amount <= 4:
        return declensions[1]
    else:
        return declensions[2]


def word_time(minute):
    """
    return minutes with words
    """
    first_num = (minute // 10) % 10
    last_num = minute % 10

    if 10 <= minute < 20:
        return time_dict[minute][0]
    elif minute <= 2:
        return time_dict[minute][4]
    elif 2 < minute < 10:
        return time_dict[minute][0]
    elif last_num == 0:
        return time_dict[first_num][3]
    else:
        return f'{time_dict[first_num][3]} {time_dict[last_num][0]}'


def end_hour(minute):
    """
    return correct declination for min >= 45
    """
    last_min = 60 - minute
    if last_min == 1:
        return plural_dict[1][1]
    else:
        return plural_dict[1][2]


while True:
    # checking for correctness, if not correct, try again
    # 24 hour time - change the time to 12
    try:
        hour, min = input('введите время в формате HH:MM: ').split(':')
        min = int(min)
        i_hour = int(time(int(hour)).strftime('%I'))
        break
    except:
        print('Введенное время не является корректной, используйте формат HH:MM')

if min == 00:
    print(f'{time_dict[i_hour][0].capitalize()} {choose_plural(i_hour, plural_dict[0])} ровно.')
elif (min < 30) or (min > 30 and min < 45):
    print(f'{word_time(min).capitalize()} {choose_plural(min, plural_dict[1])} {time_dict[i_hour][2]}.')
elif min == 30:
    print(f'Половина {time_dict[i_hour][2]}.')
else:
    res = time_dict[i_hour + 1][0] if i_hour != 12 else time_dict[1][3]
    print(f'Без {time_dict[60 - min][1]} {end_hour(min)} {res}.')
