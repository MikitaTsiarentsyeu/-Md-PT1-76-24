## Write a program that takes a string as input and returns a dictionary with the count of each word in the string.
user_input = input("Please enter the string: \n")
word_count = {}

for word in user_input.split():
    word_count[word] = word_count.get(word, 0) + 1

print(*[word for word, count in word_count.items() if count == 1], sep=" ")
print(f"\nDictionary of word count: {word_count}")

