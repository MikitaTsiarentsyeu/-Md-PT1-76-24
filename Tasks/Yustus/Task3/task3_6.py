## Write a program that takes a string as input and returns the string with all vowels removed.
user_input = input("Please enter the string: \n")
vowels = "aeiouAEIOU"
result = ""
for char in user_input:
    if char not in vowels:
        result += char
        print(char, end=" ")
print(f"\nString with all vowels removed: {result}")

