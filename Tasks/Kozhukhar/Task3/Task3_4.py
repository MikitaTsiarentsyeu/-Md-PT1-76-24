def find_second_largest(numbers):
    """Find second largest number in list"""

    sorted_numbers = sorted(numbers, reverse=True)
    second_largest = sorted_numbers[1]

    return second_largest


def main():
    try:
        input_numbers = input("Enter a list of numbers separated by spaces: ")
        numbers = list(map(float, input_numbers.split()))
        second_largest = find_second_largest(numbers)
        print("The second largest number is:", second_largest)

    except ValueError:
        print("Error: Please enter valid numbers separated by spaces.")


if __name__ == "__main__":
    main()
