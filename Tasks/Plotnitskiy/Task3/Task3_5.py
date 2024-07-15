input_string = input("Please enter a list of words, separated by spaces:\n")

words = input_string.split()

long_words = []

for word in words:
    if len(word) > 5:
        long_words.append(word)

print("Words in the entered list that have more than 5 characters:\n", long_words)
