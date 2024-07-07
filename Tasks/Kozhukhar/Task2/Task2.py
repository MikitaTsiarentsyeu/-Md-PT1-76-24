from num2words import num2words

# устанавливаем библтотеку в powershell или командной строке pip install num2words

# Словарь для часов
hour_dict = {
    0: "двенадцать",
    1: "час",
    2: "два",
    3: "три",
    4: "четыре",
    5: "пять",
    6: "шесть",
    7: "семь",
    8: "восемь",
    9: "девять",
    10: "десять",
    11: "одиннадцать",
    12: "двенадцать",
    13: "час",
    14: "два",
    15: "три",
    16: "четыре",
    17: "пять",
    18: "шесть",
    19: "семь",
    20: "восемь",
    21: "девять",
    22: "десять",
    23: "одиннадцать",
}

# Словарь для склонения минут
minutes_dict = {
    1: "одной",
    2: "двух",
    3: "трёх",
    4: "четырёх",
    5: "пяти",
    6: "шести",
    7: "семи",
    8: "восьми",
    9: "девяти",
    10: "десяти",
    11: "одиннадцати",
    12: "двенадцати",
    13: "тринадцати",
    14: "четырнадцати",
    15: "пятнадцати",
}

# Словарь для склонения часов
hours_for_half = {
    0: "двенадцатого",
    1: "первого",
    2: "второго",
    3: "третьего",
    4: "четвёртого",
    5: "пятого",
    6: "шестого",
    7: "седьмого",
    8: "восьмого",
    9: "девятого",
    10: "десятого",
    11: "одиннадцатого",
    12: "двенадцатого",
}

while True:
    try:
        time_str = input("Please, enter time in the hh:mm format: ")
        hours, minutes = map(int, time_str.split(":"))

        if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
            raise ValueError(
                "Invalid time format. Please enter the time in hh:mm format."
            )
        break
    except ValueError as e:
        print(e)


def time_to_words(hours, minutes):
    """Converts the time from digital format hh:mm into text form in Russian"""

    minutes_in_words = num2words(minutes, lang="ru", gender="feminine")

    if minutes == 0:
        hour_str = hour_dict[hours % 12]
        if (0 < hours < 2) or (12 < hours < 14):
            return f"{hour_str} ровно"
        elif (1 < hours < 5) or (13 < hours < 17):
            return f"{hour_str} часа ровно"
        elif (4 < hours < 13) or (hours == 0) or (16 < hours < 24):
            return f"{hour_str} часов ровно"
    elif (minutes < 30) or (30 < minutes < 45):
        if minutes % 10 == 1 and minutes != 11:
            return f"{minutes_in_words} минута {hours_for_half[hours % 12 + 1]}"
        elif minutes in {2, 3, 4} or (
            minutes % 10 in {2, 3, 4} and minutes % 100 not in {12, 13, 14}
        ):
            return f"{minutes_in_words} минуты {hours_for_half[hours % 12 + 1]}"
        return f"{minutes_in_words} минут {hours_for_half[hours % 12 + 1]}"
    elif minutes == 30:
        hours_str = hours_for_half[hours % 12 + 1]
        return f"половина {hours_str}"
    else:
        remaining_minutes = 60 - minutes
        minutes_str = minutes_dict[remaining_minutes]
        return f"без {minutes_str} минут {hour_dict[(hours % 12) + 1]}"


print(time_to_words(hours, minutes))
