"""
    3. Write a recursive function to count the number of occurrences of a given character in a string.
"""



def count_occurrences(string, let, count=0):
    """
        goes through the string and compares the characters,
        if true, adds the counter
    """
    if len(string) == 0:
        return count
    if string[-1] == let:
        return count_occurrences(string[0:-1], let, count + 1)
    else:
        return count_occurrences(string[0:-1], let, count)


print(count_occurrences('characteristics', 'a'))
print(count_occurrences('gggggggkggg', 'g'))
