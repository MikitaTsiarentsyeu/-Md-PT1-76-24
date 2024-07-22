#8. Write a program that takes a list of numbers as input and returns the average of all numbers in the list.
user_input = input("Введите числа:")
numbers = list(map(int, user_input.split()))
average = sum(numbers) / len(numbers)
print(average)