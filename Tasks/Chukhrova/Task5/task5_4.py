"""
4. Write a function that takes a string as an argument and 
returns two numbers, first for count of lower case letters, 
second for count of the upper case letters in the initial string.
"""


def count_letters(user_str:str):
    lower = 0
    upper = 0
    for elem in user_str:
        lower += elem.islower()
        upper += elem.isupper()
    return lower, upper


user_str = input("Enter string: ")
print(count_letters(user_str))