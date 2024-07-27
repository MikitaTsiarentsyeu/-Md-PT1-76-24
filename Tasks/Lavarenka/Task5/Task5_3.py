"""
    3. Write a function that takes a list of strings as an argument and returns
    a new list with all the strings that have a length greater than 5.
"""


def length_str(input_list: list[str]) -> list[str]:
    """
    function that takes a list of strings as an argument and returns a new list with
    all strings whose length is greater than 5,
    if the list has another format the function will return a warning
    """
    for i in input_list:
        if not isinstance(i, str):
            return (f"There is a format in the list: '{type(i).__name__}', "
                    f"the function only accepts a list of strings.")

    res = [i for i in input_list if len(i) > 5]
    return res


print(length_str(['python', 'a', 'only', 'function', 'list']))
