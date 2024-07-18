"""
    8. Write a program that takes a list of numbers as input and
    returns the average of all numbers in the list.
"""

num_list = [int(i) for i in input('Write a list of numbers separated by spaces: ').split(' ')]
# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sum(num_list))
print(len(num_list))

res = sum(num_list) / len(num_list)

print(f'Average of all numbers in the list: {res}')
