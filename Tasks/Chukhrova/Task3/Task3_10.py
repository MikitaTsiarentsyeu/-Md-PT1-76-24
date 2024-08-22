"""
10. Write a program that takes a list of numbers as input and 
returns the largest prime number in the list.
"""
import math

WARNING = "Incorrect input"

user_str = input("Enter numbers separated by commas:")
if user_str:
    user_array = user_str.split(",")
    largest_prime_number = 0
    for elem in user_array:
        if not elem.lstrip('-').isdigit():
            print(WARNING)
            break
        if int(elem) < 2:
            continue
        max_range = round(math.sqrt(int(elem))) + 1
        for i in range(2, max_range):
            if int(elem) % i == 0:
                break
        else:
            largest_prime_number = int(elem) if int(elem) > largest_prime_number else largest_prime_number
    else:
        print(f'Largest prime number: {largest_prime_number if largest_prime_number else "doesn't exist"}')
else:
    print("Empty!")