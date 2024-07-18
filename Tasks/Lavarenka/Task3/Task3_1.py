"""
    1. Write a program that takes a string as input from
    a user and returns the number of vowels in the string.
"""

user_string = input("write the text: ")

vowels = "AEIOUY" + "АУОИЭЫЯЮЕЁ"

res = [i for i in user_string if i.upper() in vowels]

print(res)
print(f'Number of vowels: {len(res)}')
