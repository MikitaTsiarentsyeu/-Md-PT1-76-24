def reverse_string(s):
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string(s[:-1])

input_string = "Good night!"
reversed_string = reverse_string(input_string)
print(reversed_string)