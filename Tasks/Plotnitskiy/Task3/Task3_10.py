input_string = input("Please enter a list of numbers, separated by spaces:\n")

string_numbers = input_string.split()

numbers = []

for number in string_numbers:
    if number.isdigit():
        numbers.append(int(number))

max_prime = -1

for number in numbers:
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            if number > max_prime:
                max_prime = number

if max_prime != -1:
    print("The largest prime number in the entered list is:\n", max_prime)
else:
    print("There are no prime numbers in the entered list.")
