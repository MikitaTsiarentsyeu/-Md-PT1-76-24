"""
    4. Write a function that takes a string as an argument and returns two numbers,
    first for count of lower case letters, second for count of the upper case letters in the initial string.
"""


def number_of_letters(string):
    """
    A function that takes a string as an argument and returns two numbers:
    the first is the number of lowercase letters,
    the second is the number of uppercase letters in the original string
    """
    if isinstance(string, str):
        lowercase_letter = [i for i in string if i.islower()]
        uppercase_letter = [i for i in string if i.isupper()]
        return (f'Number of lowercase letters: {len(lowercase_letter)}',
                f'Number of capital letters: {len(uppercase_letter)}')
    return f'{string} is not a string'


print(number_of_letters("Hello_%$12_World"))

print(number_of_letters(2323))
