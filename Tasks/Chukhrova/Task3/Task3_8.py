"""
8. Write a program that takes a list of numbers as input and 
returns the average of all numbers in the list.
"""

WARNING = "Incorrect input"

user_str = input("Enter numbers separated by commas:")
if user_str:
    user_array = user_str.split(",")
    sum_numbers = 0
    for elem in user_array:
        if not elem.lstrip('-').isdigit():
            print(WARNING)
            break
        sum_numbers += int(elem)
    else:
        print(f'Average: {sum_numbers / len(user_array)}')
else:
    print("Empty!")