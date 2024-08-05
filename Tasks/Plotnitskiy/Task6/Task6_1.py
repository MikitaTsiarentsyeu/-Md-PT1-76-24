def reverse_s(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_s(s[:-1])


print(reverse_s("Programming is fun"))
