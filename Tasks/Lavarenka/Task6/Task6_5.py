"""
    5. Write a recursive function to find the Nth number in the Fibonacci sequence.

    0, 1, 1, 2, 3, 5, 8, 13, 21
    n = 6 => 5
"""


# def fib(n):
#     if n <= 2:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)


def fib(n):
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(6))
for i in range(6):
    print(fib(i))
