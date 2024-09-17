## Write a recursive function to count the number of occurrences of a given character in a string.
def count_char(string, char):
    if not string:
        return 0
    count = 0
    if string[0] == char:
        count += 1
    return count + count_char(string[1:], char)

print(count_char('hello world!', 'l'))