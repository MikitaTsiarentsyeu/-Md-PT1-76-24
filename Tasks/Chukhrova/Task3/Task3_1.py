"""
1. Write a program that takes a string as input from a user and 
returns the number of vowels in the string.
"""

vowels = "aeiouyауоыиэяюёе"
user_str = input("Please enter a string:")
count_vowels = 0
for letter in user_str:
    if letter in vowels or letter in vowels.upper():
        count_vowels += 1
print(f'Number of vowels: {count_vowels}')