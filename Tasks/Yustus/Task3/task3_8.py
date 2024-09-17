## Write a program that takes a list of numbers as input and returns the average of all numbers in the list.
user_input = input("Enter a list of numbers separated by spaces:\n")
numbers = list(map(int, user_input.split()))
average = sum(numbers) / len(numbers)
print(f"The average of the numbers in the list is: {average}")
