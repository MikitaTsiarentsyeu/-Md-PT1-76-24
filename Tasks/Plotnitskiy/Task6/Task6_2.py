def palindrome_check(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return palindrome_check(s[1:-1])


print(palindrome_check("tenet"))
print(palindrome_check("Good"))
