input_string = input("Please enter any phrase in English or Russian:\n")

output_string = ""

for symbol in input_string:
    if symbol.isupper():
        output_string += symbol.lower()
    else:
        output_string += symbol.upper()

print(
    "The entered phrase with all capital letters converted to lowercase and vice versa:\n",
    output_string,
)
