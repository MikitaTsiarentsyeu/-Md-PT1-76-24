import re

text = input("Введите строку для удаления гласных букв:").lower()
vowels = set("ауиоиэыяюеё")

text_new = ""
for letter in text:
    if letter not in vowels:
        text_new += letter
print (text_new)