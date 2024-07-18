def prime_true_false(number):
    """Checks if a number is prime."""
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number**0.5) + 1, 2):  # for odd
        if number % i == 0:
            return False
    return True


def largest_prime(numbers):
    """The largest prime number in a list."""
    largest_number = None
    for number in numbers:
        if prime_true_false(number):
            if largest_number is None or number > largest_number:
                largest_number = number
    return largest_number


user_input = input("Enter numbers separated by spaces: ")
try:
    numbers = list(map(int, user_input.split()))
    result = largest_prime(numbers)
    if result is not None:
        print(f"Largest prime number in the list: {result}")
    else:
        print("There are no prime numbers in the list.")
except ValueError:
    print("Error: Please enter numbers in the correct format.")
