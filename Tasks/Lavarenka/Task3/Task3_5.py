"""
    5. Write a program that takes a list of strings as input and
    returns a list with all strings that have a length greater than 5 characters.
"""

print([i for i in input("Write the text: ").split(' ') if len(i) > 5])
