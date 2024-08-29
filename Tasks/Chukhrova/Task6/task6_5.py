"""
5. Write a recursive function to find the Nth number in the Fibonacci sequence.
0, 1, 1, 2, 3, 5, 8, 13, 21
n = 6 => 5
"""

# n = 6 => 8
# def fibonacci_seq(num:int) -> int:
#     if num < 2:
#         return num
#     else:
#         return fibonacci_seq(num-1) + fibonacci_seq(num-2)

# n = 6 => 5
def fibonacci_seq(num:int) -> int:
    if num == 1:
        return 0
    if num == 2:
        return 1
    else:
        return fibonacci_seq(num-1) + fibonacci_seq(num-2)

print(fibonacci_seq(6))