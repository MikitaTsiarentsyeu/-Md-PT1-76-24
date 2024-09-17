##  Write a program that takes a list of numbers as input and returns the sum of all even numbers in the list.
user_input = input("Enter a list of numbers separated by spaces:\n")
sum_even = sum(num for num in map(int, user_input.split()) if num % 2 == 0)
print(f"The sum of all even numbers in the list is: {sum_even}")