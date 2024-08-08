user_input = input("Enter a string:\n")

reversed_string = ""

for letter in reversed(user_input):
    reversed_string += letter

print("Reversed string:", reversed_string)