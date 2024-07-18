input_string = input("Please enter a list of numbers, separated by spaces:\n")

input_string = input_string.replace(",", ".")

string_numbers = input_string.split()

numbers = [float(number) for number in string_numbers]

total_sum = 0

for number in numbers:
    total_sum += number

average = total_sum / len(numbers)

print("The average of all numbers in the entered list is:\n", average)
