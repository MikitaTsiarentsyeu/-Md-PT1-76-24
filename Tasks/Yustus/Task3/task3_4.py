## Write a program that takes a list of numbers as input and returns the second largest number in the list.
user_input = input("Enter a list of numbers separated by spaces:\n")
numbers = list(map(int, user_input.split()))
numbers.sort(reverse=True)
print(f"The second largest number in the list is: {numbers[1]}")
