def reverse_string(input_string):
    """Reversed string"""
    new_string = ""
    l = len(input_string) - 1
    while l >= 0:
        new_string += input_string[l]
        l -= 1
    return new_string


def main():
    user_input = input("Enter string: ")
    print("Reversed string: ", reverse_string(user_input))


if __name__ == "__main__":
    main()
