def count_characters(s, char, count=0):
    if len(s) == 0:
        return count
    else:
        if s[0] == char:
            count += 1
        return count_characters(s[1:], char, count)


print(count_characters("Hello world", "l"))
