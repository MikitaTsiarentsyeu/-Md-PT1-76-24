'''
Implement a text output of the time entered from the console (the user should input data in the format hh:mm).

Show the responses to the user in Russian according to the rules listed below:

min == 0: такое-то значение часа ровно (15:00 - три часа ровно)
min < 30: столько-то минут следующего часа (19:12 - двенадцать минут восьмого)
min == 30: половина такого-то (15:30 - половина четвёртого)
min > 30 and min < 45 столько-то минут следующего часа (12:38 - тридцать восемь минут первого)
min >= 45 без min такого-то (08:54 - без шести минут девять)
'''

time_numbers = {
    1: ["один", "одной", "первого", "одна"], 
    2: ["два", "двух", "второго", "две"],
    3: ["три", "трех", "третьего", "три"],
    4: ["четыре", "четырех", "четвертого", "четрые"],
    5: ["пять", "пяти", "пятого"],
    6: ["шесть", "шести", "шестого"],
    7: ["семь", "семи", "седьмого"],
    8: ["восемь", "восьми", "восьмого"],
    9: ["девять", "девяти", "девятого"],
    10: ["десять", "десяти", "десятого"],
    11: ["одиннадцать", "одиннадцати", "одиннадцатого"],
    12: ["двенадцать", "двенадцати", "двенадцатого"],
    13: ["тринадцать", "тринадцати"],
    14: ["четырнадцать", "четырнацати"],
    15: ["пятнадцать", "пятнадцати"],
    16: ["шестнадцать", "шестнадцати"],
    17: ["семнадцать", "семнадцати"],
    18: ["восемнадцать", "восемнадцати"],
    19: ["девятнадцать", "девятнадацати"],
    20: ["двадцать", "двадцати"],
    30: ["тридцать", "тридцати"],
    40: ["сорок", "сорока"]
}

def get_minutes_text(m):
    return "минута" if m == 1 else "минуты" if 2<= m <=4 else "минут"

time_str = input('Please, input time (format hh:mm): ')
if time_str.count(':') == 1:
    hour, min = time_str.split(':')
    if not hour.isdigit() or int(hour) >= 24:
        print("Incorrect hours")
        exit()
    elif not min.isdigit() or int(min) >= 60:
        print("Incorrect minutes")
        exit()
    min = int(min)
    hour = int(hour)

    hours = hour % 12 if hour % 12 != 0 else 12
    next_hour = (hour + 1) % 12 if (hour + 1) % 12 != 0 else 12

    if min == 0:
        extra_text = "час" if hours == 1 else "часа" if 2<= hours <=4 else "часов"
        print(f'{time_str} - {time_numbers[hours][0]} {extra_text} ровно')

    elif min < 30:
        if min in time_numbers:
            minutes = time_numbers[min][3] if 1<= min <=4 else time_numbers[min][0]
            print(f"{time_str} - {minutes} {get_minutes_text(min)} {time_numbers[next_hour][2]}")
        else:
            tens, units = divmod(min, 10)
            minutes = time_numbers[units][3] if 1<= units <=4 else time_numbers[units][0]
            print(f"{time_str} - {time_numbers[tens * 10][0]} {minutes} {get_minutes_text(units)} {time_numbers[next_hour][2]}")

    elif min == 30:
        print(f'{time_str} - половина {time_numbers[next_hour][2]}')

    elif 30 < min < 45:
        if min in time_numbers:
            print(f"{time_numbers[min][0]} минут {time_numbers[next_hour][2]}")
        else:
            tens, units = divmod(min, 10)
            minutes = time_numbers[units][3] if 1<= units <=4 else time_numbers[units][0]
            print(f"{time_numbers[tens * 10][0]} {minutes} {get_minutes_text(units)} {time_numbers[next_hour][2]}")

    else:
        minutes = 60 - min
        extra_text = "минуты" if minutes == 1 else "минут"
        print(f"{time_str} - без {time_numbers[minutes][1]} {extra_text} {time_numbers[next_hour][0]}")
    
else:
    print("Incorrect input")
    exit()
