user_input = input("Ввод:")
count = 0
vowels = "AEIOUYaeiouyАЕЁИОУЫЭЮЯаеёиоуыэюя"
for letter in user_input:
    if letter in vowels:
        count += 1
print("Количество гласных:", f"{count}")