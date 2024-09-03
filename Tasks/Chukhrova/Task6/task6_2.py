"""
2. Write a recursive function to check whether a given string is a palindrome.
"""

def is_palindrome(my_string:str) -> bool:
    if not my_string:
        return True
    return is_palindrome(my_string[1:-1]) if my_string[0] == my_string[-1] else False


print(is_palindrome("madam"))
print(is_palindrome("python"))