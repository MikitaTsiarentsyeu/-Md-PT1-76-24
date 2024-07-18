def calculate_average(numbers):
    """Calculate the average of a list of numbers"""
    if not numbers:
        return 0

    total = 0
    amount = 0

    for n in numbers:
        total += n
        amount += 1

    average = total / amount
    return average


input_numbers = input("Enter numbers separated by spaces: ").split()

numbers = [float(n) for n in input_numbers]

print("Average of all numbers in the list: ", calculate_average(numbers))
