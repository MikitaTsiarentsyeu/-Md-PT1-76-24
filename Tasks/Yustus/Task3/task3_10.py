## Write a program that takes a list of numbers as input and returns the largest prime number in the list.
## Write a program that takes a list of numbers as input and returns the largest prime number in the list.
input_string = input("Please enter a list of numbers, separated by spaces:\n")

# Convert input string to list of integers
numbers = [int(num) for num in input_string.split() if num.isdigit()]

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Find the largest prime number in the list
max_prime = max(filter(is_prime, numbers), default=-1)

if max_prime != -1:
    print(f"The largest prime number in the list is: {max_prime}")
else:
    print("There are no prime numbers in the list.")



