"""
    7. Write a program that takes a string as input and returns
    the string with all capital letters converted to lowercase and vice versa.
"""

user_string = input("Write the text: ")
# user_string = 'aWwFgggGGG'


print(''.join([i.swapcase() for i in user_string]))
