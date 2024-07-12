"""
    10. Write a program that takes a list of numbers as input and
    returns the largest prime number in the list.
"""

# num_list = [int(i) for i in input('Write a list of numbers separated by spaces: ').split(' ')]
num_list = [int(i) for i in range(1, 100)]

print(num_list)

prime_number = []

for number in num_list:
    # run through all the numbers from 1 to the current one, looking for the number of divisors
    num_divisors = [j for j in range(1, number + 1) if number % j == 0]
    if len(num_divisors) == 2:
        prime_number.append(number)

print(prime_number)
print(f'Largest prime number in the list: {max(prime_number)}')

# good decision?