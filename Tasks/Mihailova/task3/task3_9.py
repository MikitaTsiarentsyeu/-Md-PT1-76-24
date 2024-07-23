#9. Write a program that takes a string as input and returns the string reversed.
user_input = input("Введите слова: ")
words = user_input.split()
words.reverse()
reversed_sentence = ' '.join(words)
print(reversed_sentence)