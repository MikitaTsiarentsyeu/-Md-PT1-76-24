user_input = input("Please enter a list of numbers separated by spaces:\n")

numbers = list(map(float, user_input.split()))

first_largest = float('-inf')
second_largest = float('-inf')

for number in numbers:
    if number > first_largest:
        first_largest = number
    else:
        number > second_largest and number < first_largest
        second_largest = number

print("The second largest number is:", second_largest)