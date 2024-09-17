## Write a function that takes a string as an argument and returns two numbers, first for count of lower case letters, second for count of the upper case letters in the initial string.
def count_case_letters(input_string: str) -> tuple:
    lower_count = 0
    upper_count = 0
    for char in input_string:
        if char.isalpha():
            if char.islower():
                lower_count += 1
            else:
                upper_count += 1
    return lower_count, upper_count