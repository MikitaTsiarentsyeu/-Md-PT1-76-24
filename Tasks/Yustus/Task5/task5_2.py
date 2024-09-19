## Write a function that takes a list of strings as an argument and returns a new list of strings that are all reversed.
def reverse_strings(string_list: list) -> list:
    reversed_list = []
    for string in string_list:
        if isinstance(string, str):
            reversed_list.append(string[::-1])
        else:
            reversed_list.append(string)
    return reversed_list