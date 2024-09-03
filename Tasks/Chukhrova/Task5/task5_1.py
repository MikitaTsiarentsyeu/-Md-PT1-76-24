"""
1. Write a function that takes two integers as arguments and returns their sum.
"""


def my_sum(a:int, b:int):
    return a+b if isinstance(a, int) and isinstance(b, int) else "I can't do it:("


print(my_sum(1, 2))
print(my_sum(1, 2.2))
print(my_sum(1, 'a'))