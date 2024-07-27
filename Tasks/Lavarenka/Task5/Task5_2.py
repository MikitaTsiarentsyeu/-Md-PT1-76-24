"""
    2. Write a function that takes a list of strings as an argument and returns
    a new list of strings that are all reversed.
"""


def reverse_str(input_list: list[str]) -> list[str]:
    """
    the function that takes a list of strings as an argument and returns
    a new list of strings that are all reversed
    if the list contains a non-string value, the function will not return it
    """

    res = [i[::-1] for i in input_list if isinstance(i, str)]
    return res


print(reverse_str([1, 'abc', 'abc', 'abc', 'afg', 'arg']))
