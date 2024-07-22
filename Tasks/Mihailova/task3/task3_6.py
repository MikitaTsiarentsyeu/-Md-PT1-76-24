user_input = input("Ввод:")
vowels = "AEIOUYaeiouyАЕЁИОУЫЭЮЯаеёиоуыэюя"
for vowel in vowels:
    user_input = user_input.replace(vowel, "")
print(user_input)
    
