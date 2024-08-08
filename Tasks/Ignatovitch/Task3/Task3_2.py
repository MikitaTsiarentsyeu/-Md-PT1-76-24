user_input = input("Enter a list of numbers separated by spaces:\n")

numbers = list(map(int, user_input.split()))

sum_even = 0

for number in numbers:
    if number % 2 == 0:
        sum_even += number

print(f"The sum of all even numbers in the list is: {sum_even}")