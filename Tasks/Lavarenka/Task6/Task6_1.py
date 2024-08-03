"""
    1. Write a recursive function to reverse a string.
"""


def string_reverse(string):
    """
        with each iteration remove the first character,
        after recursion return everything in reverse order
    """
    if len(string) == 0:
        return string
    return string_reverse(string[1:]) + string[0]


print(string_reverse("Hello World"))
