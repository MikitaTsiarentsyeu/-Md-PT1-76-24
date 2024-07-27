"""
    1. Write a function that takes two integers as arguments and returns their sum.
"""


def sum_numbers(a: int, b: int) -> int:
    """
    the function returns the sum of numbers
    """
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    return 'Wrong format'


print(sum_numbers(1, 2))
