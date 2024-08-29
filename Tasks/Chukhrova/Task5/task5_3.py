"""
3. Write a function that takes a list of strings as an argument and 
returns a new list with all the strings that have a length greater than 5.
"""


def get_big_strings(l:list) -> list:
    # 1
    # return [elem for elem in l if len(elem) > 5]
    # 2
    return list(filter(lambda elem: len(elem)>5, l))


user_list = input("Enter strings separated by commas:")
print(get_big_strings(user_list.split(',')))