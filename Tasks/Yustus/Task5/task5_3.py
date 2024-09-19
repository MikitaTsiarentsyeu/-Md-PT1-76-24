## Write a function that takes a list of strings as an argument and returns a new list with all the strings that have a length greater than 5.
def filter_long_strings(string_list: list) -> list:
    filtered_list = []
    for string in string_list:
        if isinstance(string, str) and len(string) > 5:
            filtered_list.append(string)
        else:
            filtered_list.append(string)
    return filtered_list
