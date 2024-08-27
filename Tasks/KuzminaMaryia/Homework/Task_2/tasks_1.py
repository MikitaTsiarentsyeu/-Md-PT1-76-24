from num2words import num2words #установка через консоль, команда 'pip install num2words'

V1_com = "incorrect format of inputted value, please try again"
V2_com = "incorrect format of inputted value, please try again"

MiN = {
    0 : ["двенадцатого"],
    1 : ["первого"],
    2 : ["второго"],
    3 : ["третьего"],
    4 : ["четвертого"],
    5 : ["пятого"],
    6 : ["шестого"],
    7 : ["седьмого"],
    8 : ["восьмого"],
    9 : ["девятого"],
    10 : ["десятого"],
    11 : ["одинадцатого"],
    12 : ["двенадцатого"]
}

hours = {
    0 : ["двенадцать"],
    1 : ["один"],
    2 : ["два"],
    3 : ["три"],
    4 : ["четыре"],
    5 : ["пять"],
    6 : ["шесть"],
    7 : ["семь"],
    8 : ["восемь"],
    9 : ["девять"],
    10 : ["десять"],
    11 : ["одиннадцать"],
    12 : ["двенадцать"]
}

while True:
    write_user = input ("Enter the time in the data in hh:mm format:")
    if len(write_user) != 5:
        print (V2_com)
        continue
    if write_user[2] != ':' or write_user.count(':') != 1:
        print (V1_com)
        continue
    hour, minutka = write_user.split(':')
    if not (hour.isdigit() and minutka.isdigit()):
        print(V1_com)
        continue
    hour, minutka = int(hour), int(minutka)
    if hour > 23 or minutka > 59:
        print(V1_com)
        continue
    break

min = num2words(minutka, lang="ru")
min_g = 60 - minutka
min_end = num2words(min_g, lang="ru")

def times (hour, minutka):
    if minutka == 0:
        h_str = hours [hour % 12]
        return (f"{h_str[0]} часов ровно")
    elif minutka < 30:
        m_str = MiN [(hour % 12) + 1]
        return (f"{min} минут {m_str[0]}")
    elif minutka == 30:
        return (f"половина {m_str[0]}")
    elif minutka > 30 and minutka < 45:
        return (f"{min} минут {m_str[0]}")
    elif  minutka >= 45:
        hp_str = hours [(hour % 12) + 1]
        return (f"без {min_end} минут {hp_str[0]}")
    
print(times(hour, minutka))