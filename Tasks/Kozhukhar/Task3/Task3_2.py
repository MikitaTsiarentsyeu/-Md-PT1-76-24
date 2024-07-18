def sum_of_even_numbers(numbers):
    """Sum of even numbers"""
    sum_even = 0
    for num in numbers:
        if num % 2 == 0:
            sum_even += num
    return sum_even


def main():
    try:
        input_numbers = input("Enter numbers separated by spaces: ")
        numbers = list(map(int, input_numbers.split()))
        result = sum_of_even_numbers(numbers)
        print("Sum of even numbers: ", result)

    except ValueError:
        print("Error: Please enter numbers in the correct format.")


if __name__ == "__main__":
    main()
