from random import randint

"""
5.Write a program that generates a random number in a given range,
and shows the answer to a user, ask a user for the left and right border.
"""

# The randint() function takes two required arguments a and b and returns
# a random integer from the range

a = int(input())
b = int(input())

res = randint(a, b) if a < b else randint(b, a)  # if B is greater than A then swap places

print(f'A random number in a given range {a} and {b} is equal to: {res}')
