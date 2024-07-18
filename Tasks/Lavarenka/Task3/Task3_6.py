"""
    6. Write a program that takes a string as input and
    returns the string with all vowels removed.
"""

user_string = input("Write the text: ")
vowels = "AEIOUY" + "АУОИЭЫЯЮЕЁ"

res = [i for i in user_string if i.upper() not in vowels]

print(f"Line without vowels: {''.join(res)}")