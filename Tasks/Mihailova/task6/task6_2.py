#2. Write a recursive function to check whether a given string is a palindrome.
def is_palindrome(s):
    
    s = s.replace(" ", "").lower()
    
    if len(s) <= 1:
        return True
    
    if s[0] != s[-1]:
        return False
    
    return is_palindrome(s[1:-1])


print(is_palindrome("Was it a car or a cat I saw"))  

