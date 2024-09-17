## Write a program that takes a list of strings as input and returns a list with all strings that have a length greater than 5 characters.
user_input = input("Please enter the list of strings separated by spaces: \n")
long_strings = [string for string in user_input.split() if len(string) > 5]
print(f"List of strings with length greater than 5: {long_strings}")

