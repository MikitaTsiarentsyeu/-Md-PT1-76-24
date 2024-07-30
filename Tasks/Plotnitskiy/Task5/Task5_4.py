def count_letters(string):
    low_count = 0
    upp_count = 0
    for symbol in string:
        if symbol.islower():
            low_count += 1
        elif symbol.isupper():
            upp_count += 1
    return low_count, upp_count


print(count_letters("Zen of Python"))