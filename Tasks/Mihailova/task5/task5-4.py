#4. Write a function that takes a string as an argument and returns two numbers, first for count of lower case letters, second for count
#of the upper case letters in the initial string.
def count_case_letters(s):
    lower_count = sum(1 for char in s if char.islower())
    upper_count = sum(1 for char in s if char.isupper())
    return lower_count, upper_count


input_string = "вадтЛАормрпПАСпсРПСПА"
lowercase_count, uppercase_count = count_case_letters(input_string)
print(f"Lowercase letters: {lowercase_count}, Uppercase letters: {uppercase_count}")
