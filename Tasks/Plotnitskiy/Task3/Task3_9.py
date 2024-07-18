input_string = input("Please enter any phrase in English or Russian:\n")

output_string = ""

for symbol in reversed(input_string):
    output_string += symbol

print("The entered phrase reversed:\n", output_string)
