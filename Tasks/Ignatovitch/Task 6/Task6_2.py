def is_palindrome(s):
    s = s.replace(" ", "").lower()
    
    if len(s) <= 1:
        return True
    
    if s[0] != s[-1]:
        return False

    return is_palindrome(s[1:-1])

input_string = "A man a plan a canal Panama"
result = is_palindrome(input_string)
print(result) 