def palindrome(s: str) -> bool:
    """Check whether a given string is a palindrom"""

    if len(s) <= 1:
        return True

    elif s[0] != s[-1]:
        return False

    return palindrome(s[1:-1])


print(palindrome("level"))
print(palindrome("Ne polindrom"))
print(palindrome("tenet"))
print(palindrome("Hello friend"))
print(palindrome("madam"))
