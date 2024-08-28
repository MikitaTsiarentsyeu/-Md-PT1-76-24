"""
1. Write a recursive function to reverse a string.
"""

def reverse_strings(string_to_reverse:str) -> str:
    if not string_to_reverse:
        return ""
    return reverse_strings(string_to_reverse[1:]) + string_to_reverse[0]


print(reverse_strings("I love cats"))
