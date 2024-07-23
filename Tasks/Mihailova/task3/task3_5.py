user_input = input("Введите слова: ")
words = user_input.split()
long_words = []

for word in words:
    if len(word) > 5:
        long_words.append(word)

print(long_words)