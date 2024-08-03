"""
    4. Write a recursive function to calculate the power of a given number.
"""


def power(num, p):
    if p == 0:
        return 1
    return num * power(num, p - 1)


print(power(4, 4))
