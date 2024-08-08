user_input = input("Please enter the string: \n")

word_count = {}

words = user_input.split()

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(f"Word count dictionary: {word_count}")
