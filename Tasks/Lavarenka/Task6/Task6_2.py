"""
    2. Write a recursive function to check whether a given string is a palindrome.
"""


def is_palindrome(word):
    """
        with each iteration compares the first and last symbol,
        if true then removes the symbols and starts a new iteration
    """
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])

print(is_palindrome("abab"))
print(is_palindrome("abyba"))


