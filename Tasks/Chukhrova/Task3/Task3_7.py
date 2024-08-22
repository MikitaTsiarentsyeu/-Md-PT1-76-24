"""
7. Write a program that takes a string as input and 
returns the string with all capital letters converted to lowercase and vice versa.
"""

user_str = input("Please enter a string:")
new_user_str = ""
for letter in user_str:
    new_user_str += letter.lower() if letter.isupper() else letter.upper()
print(f'New string: {new_user_str}')