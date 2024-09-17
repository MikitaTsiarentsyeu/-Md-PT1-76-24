def count_occurrences(s, char):
    if not s:
        return 0
    
    count = 1 if s[0] == char else 0
    
    return count + count_occurrences(s[1:], char)

input_string = "hello world"
target_char = "o"
result = count_occurrences(input_string, target_char)
print(result) 