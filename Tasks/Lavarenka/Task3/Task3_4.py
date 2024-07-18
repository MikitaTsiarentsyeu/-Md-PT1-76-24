"""
    4. Write a program that takes a list of numbers as input and
    returns the second largest number in the list.
"""

num_list = [int(i) for i in input('Write a list of numbers separated by spaces: ').split(' ')]
# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


num_list.remove(min(num_list))

print(f'second largest number in the list: {min(num_list)}')
