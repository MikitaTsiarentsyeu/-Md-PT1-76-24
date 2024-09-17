## Write a recursive function to check whether a given string is a palindrome.
def is_palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] == string[-1]:
        return is_palindrome(string[1:-1])
    return False


print(is_palindrome("Hello World!"))
print(is_palindrome("level"))
print(is_palindrome("tenet"))