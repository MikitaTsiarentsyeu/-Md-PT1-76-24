def reverse_string(s: str) -> str:
    """Recursive function to reverse a string"""
    if s == "":
        return ""
    return reverse_string(s[1:]) + s[0]


user_string = "test for this task"
print(reverse_string(user_string))
