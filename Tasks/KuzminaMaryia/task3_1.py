import re


text = input("Введите строку для подсчета гласных букв:").lower()
vowels = set("ауиоиэыяюеё")
coint = 0


for letter in text:
    if letter in vowels:
        coint += 1


print (f"Количество гласных равно:",{coint})