"""
4. Write a program that takes a list of numbers as input 
and returns the second largest number in the list.
"""

WARNING = "Incorrect input"

user_str = input("Enter numbers separated by commas:")
if user_str:
    user_array = user_str.split(",")
    if len(user_array) < 2:
        print(WARNING)
        exit()

    largest_number, second_largest_number = [int(user_array[0]), int(user_array[1])] \
        if int(user_array[0]) > int(user_array[1]) else [int(user_array[1]), int(user_array[0])]
    
    for i in range(2, len(user_array)):
        if not user_array[i].lstrip('-').isdigit():
            print(WARNING)
            break
        if int(user_array[i]) > largest_number:
            second_largest_number = largest_number
            largest_number = int(user_array[i])
        elif int(user_array[i]) > second_largest_number:
            second_largest_number = int(user_array[i])
    else:
        print(f'Second largest number: {second_largest_number}')
else:
    print("Empty!")