#2. Write a function that takes a list of strings as an argument and returns a new list of strings that are all reversed.
def reverse_strings(string_list):
    return [s[::-1] for s in string_list]
strings = ["one", "five", "zero"]
reversed_strings = reverse_strings(strings)
print(reversed_strings) 