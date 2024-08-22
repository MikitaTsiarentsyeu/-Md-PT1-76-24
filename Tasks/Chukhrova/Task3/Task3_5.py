"""
5. Write a program that takes a list of strings as input and returns a list with all strings 
that have a length greater than 5 characters.
"""

WARNING = "There is no string greater than 5 characters!"

user_str = input("Enter strings separated by commas:")

if user_str:
    user_array = user_str.split(",")
    new_user_array = []
    for word in user_array:
        if len(word) > 5:
            new_user_array.append(word)
    print(f'Strings: {new_user_array}' if new_user_array else WARNING)
else:
    print(WARNING)