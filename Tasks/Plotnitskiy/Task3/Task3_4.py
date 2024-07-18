input_string = input("Please enter a list of numbers, separated by spaces:\n")

input_string = input_string.replace(",", ".")

string_numbers = input_string.split()

numbers = [float(number) for number in string_numbers]

first_max = float("-inf")
second_max = float("-inf")

for number in numbers:
    if number > first_max:
        second_max = first_max
        first_max = number
    elif number > second_max and number < first_max:
        second_max = number

print("The second largest number in the entered list is:\n", second_max)
