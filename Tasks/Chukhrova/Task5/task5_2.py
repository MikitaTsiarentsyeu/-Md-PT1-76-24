"""
2. Write a function that takes a list of strings as an argument and 
returns a new list of strings that are all reversed.
"""


def reverse_user_strings(l:list) -> list:
    # 1
    # return [elem[::-1] for elem in l] 
    # 2
    return list(map(lambda elem: elem[::-1], l))


user_list = input("Enter strings separated by commas:")
print(reverse_user_strings(user_list.split(',')))