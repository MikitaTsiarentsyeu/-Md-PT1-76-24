from validation import h, m


current_hours = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять", "одинадцать", "двенадцать"]
following_hours = ["", "первого", "второго", "третьего", "четвёртого", "пятого", "шестого",
"седьмого", "восьмого", "девятого", "десятого", "одиннадцатого", "двенадцатого"]
 
 
current_hour = h % 12 if h % 12 != 0 else 12  
next_hour = (current_hour % 12) + 1

if m == 0 and h in (1, 13):
    description = f"{current_hours[current_hour]} час ровно"
elif m == 0 and h in (2, 3, 4, 14, 15, 16):
    description = f"{current_hours[current_hour]} часа ровно"
elif m == 0 and h in (5, 6, 7, 8, 9, 10, 11, 12, 17, 18, 19, 20, 21, 22, 23):
    description = f"{current_hours[current_hour]} часов ровно"
elif m < 30:
    description = f"{m} минут {following_hours[next_hour]}"
elif m == 30:
    description = f"половина {following_hours[next_hour]}"
elif m < 45:
    description = f"{m} минут {following_hours[next_hour]}"
else:
    description = f"без {60 - m} минут {following_hours[next_hour]}"

print(description)

