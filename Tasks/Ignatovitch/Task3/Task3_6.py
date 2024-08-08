user_input = input("Please enter a string:\n")

result = ""

vowels = "aeiouyAEIOUY"

for letter in user_input:
    if letter not in vowels:
        result += letter

print("String without vowels :", result)