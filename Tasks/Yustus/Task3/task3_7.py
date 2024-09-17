## Write a program that takes a string as input and returns the string with all capital letters converted to lowercase and vice versa.
user_input = input("Please enter the string: \n")
result = ""
for char in user_input:
    if char.isupper():
        result += char.lower()
    elif char.islower():
        result += char.upper()
    else:
        result += char
print(f"String with swapped letters: {result}")








