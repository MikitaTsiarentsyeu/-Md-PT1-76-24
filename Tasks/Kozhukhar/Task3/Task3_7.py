def convert_letters(input_str):
    """Convert all capital letters to lowercase and vice versa."""
    swap_str = ""
    for symbal in input_str:
        if symbal.isupper():
            swap_str += symbal.lower()
        elif symbal.islower():
            swap_str += symbal.upper()
        else:
            swap_str += symbal
    return swap_str


user_input = input("Enter a string: ")

print("String with swapped letters:", convert_letters(user_input))
