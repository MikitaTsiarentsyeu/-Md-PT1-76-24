"""
2. Write a program that takes a list of numbers as input and 
returns the sum of all even numbers in the list.
"""

WARNING = "Incorrect input"

user_str = input("Enter numbers separated by commas:")
if user_str:
    user_array = user_str.split(",")
    sum_even_numbers = 0
    for elem in user_array:
        if not elem.lstrip('-').isdigit():
            print(WARNING)
            break
        if int(elem) % 2 == 0:
            sum_even_numbers += int(elem)
    else:
        print(f'Sum of even numbers: {sum_even_numbers}')
else:
    print("Empty!")