input_string = input("Please enter any phrase in English or Russian:\n")

vowels = "aeiouyAEIOUYаеёиоуыэюяАЕЁИОУЫЭЮЯ"

output_string = ""

for symbol in input_string:
    if symbol not in vowels:
        output_string += symbol

print("The entered phrase with all vowels removed:\n", output_string)
