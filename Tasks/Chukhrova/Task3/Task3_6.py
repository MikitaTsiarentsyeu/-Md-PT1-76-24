"""
6. Write a program that takes a string as input and 
returns the string with all vowels removed.
"""

vowels = "aeiouyауоыиэяюёе"
user_str = input("Please enter a string:")
new_user_str = ""
for letter in user_str:
    if not (letter in vowels or letter in vowels.upper()):
        new_user_str += letter
print(f'String without vowels: {new_user_str}')