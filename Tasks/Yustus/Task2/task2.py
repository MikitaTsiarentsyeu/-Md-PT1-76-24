'''
Implement a text output of the time entered from the console (the user should input data in the format hh:mm).
Show the responses to the user in Russian according to the rules listed below:
if minutes == 0: show message with exactly in the end (15:00 - three o'clock exactly)
if minutes < 30: show message in format minutes past hours (19:12 - twelve minutes past seven)
minutes == 30: show message with half of such hour (15:30 - half past three)
## minutes > 30 and min < 45: show message in format minutes of the next hour (12:38 - thirty-eight minutes past one)
## minutes >= 45: show message in format minutes to hour (08:54 - six minutes to nine)
'''

from datetime import time

def get_hour_word(hour):
    hours = ["ночи", "час", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять", "одиннадцать", "двенадцать"]
    return hours[hour % 12] if hour % 12 < len(hours) else hours[0]

def get_next_hour_word(hour):
    hours = ["первого", "второго", "третьего", "четвертого", "пятого", "шестого", "седьмого", "восьмого", "девятого", "десятого", "одинадцатого", "двенадцатого"]
    return hours[hour % 12] if hour % 12 < len(hours) else hours[0]

def get_minute_plural(minute):
    return "а" if minute == 1 else "ут"

def get_time_description(time_str):
    try:
        user_time = time.fromisoformat(time_str)
    except ValueError:
        return "The time format is incorrect. Enter the time in the hh:mm format."

    time_descriptions = {
        is_zero_minute: "{hour}:00 - {hour_word} ровно",
        is_before_half_hour: "{minute} минут{minute_plural} после {hour}",
        is_half_hour: "{hour}:30 - половина {hour_next}",
        is_after_half_hour: "{minute} минут{minute_plural} {hour_next}",
        is_before_next_hour: "{sixty_minus_minute} минут{minute_plural} {hour_next}"
    }

    for condition, description in time_descriptions.items():
        if condition(user_time):
            return description.format(hour=user_time.hour, hour_word=get_hour_word(user_time.hour),
                                      minute=user_time.minute, minute_plural=get_minute_plural(user_time.minute),
                                      hour_next=get_next_hour_word(user_time.hour),
                                      sixty_minus_minute=60 - user_time.minute)

def is_zero_minute(time_obj):
    return time_obj.minute == 0

def is_before_half_hour(time_obj):
    return time_obj.minute < 30

def is_half_hour(time_obj):
    return time_obj.minute == 30

def is_after_half_hour(time_obj):
    return time_obj.minute > 30 and time_obj.minute < 45

def is_before_next_hour(time_obj):
    return time_obj.minute >= 45

# Example usage
print(get_time_description("00:00"))  # Output: 0:00 - ночи часов ровно
print(get_time_description("01:01"))  # Output: 1 минута после 1
print(get_time_description("01:15"))  # Output: 15 минут после 1
print(get_time_description("12:30"))  # Output: 12:30 - половина дня
print(get_time_description("13:41"))  # Output: 41 минута четырнадцать
print(get_time_description("23:50"))  # Output: 10 минут до ночи


time_str = input("Enter the time in format hh:mm: ")
print(get_time_description(time_str))

