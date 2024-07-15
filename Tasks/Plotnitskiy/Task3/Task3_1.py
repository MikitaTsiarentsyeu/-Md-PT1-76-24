input_string = input("Please enter any phrase in English or Russian:\n")

vowels = "aeiouyAEIOUYаеёиоуыэюяАЕЁИОУЫЭЮЯ"

counter = 0

for symbol in input_string:
    if symbol in vowels:
        counter += 1

print("Number of vowels in the entered phrase:\n", counter)
