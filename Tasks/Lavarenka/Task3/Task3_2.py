"""
    2. Write a program that takes a list of numbers as input and
    returns the sum of all even numbers in the list.
"""

num_list = [int(i) for i in input('Write a list of numbers separated by spaces: ').split(' ')]
# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(num_list)
res = sum([i for i in num_list if i % 2 == 0])

print(f'Sum of all even numbers in the list: {res}')
