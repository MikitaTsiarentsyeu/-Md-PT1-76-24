input_string = input("Please enter any phrase in English or Russian:\n")

words = input_string.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Count of each word in the entered phrase:\n", word_count)
