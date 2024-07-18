input_string = input("Please enter a list of numbers, separated by spaces:\n")

input_string = input_string.replace(",", ".")

string_numbers = input_string.split()

numbers = [float(number) for number in string_numbers]

sum_of_even = 0

for number in numbers:
    if number % 2 == 0:
        sum_of_even += number

print("Sum of even numbers in the entered list:\n", int(sum_of_even))
