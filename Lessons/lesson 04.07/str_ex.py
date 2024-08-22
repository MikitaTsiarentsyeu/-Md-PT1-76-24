s = "my very long string"

print(len(s))

print(s[0], s[1], s[2], s[3], s[4])
n = len(s)
print(s[n-1])
# print(s[n]) IndexError

print(s[-1], s[-2], s[-3])

#slicing

print(s[0:7])
print(s[3:])
print(s[:])
print(s[3:-3])
print(s[3:-3:1])
print(s[3:-3:2])
print(s[::-1])


# s[n+1] = "s" TypeError
# s[0] = 't'    TypeError

print('s' in s, "long" in s, "int" in s)

# print(repr("\ttest\t"))

print(s.count('s'), s.count(' '), s.count("long"), s.count("count"))

print(s.find('y'), s.find("very"), s.find("test"))

s = "TeSt_sTrInG"

print(s.upper(), s.lower(), s.capitalize(), s)

print(s.casefold())

print(s)

s = s.lower()

print(s)

print(s.replace('t', 'T', 1).replace('_', ' '))

print(s)

print(s.replace("test", 'my'))

s = "my very long string"
print(s.split())
print(s.split('o'))
print(s.split("long"))

s = "24324327_adidas_superstar_red"
print(s.split('_'))

print('_'.join(["test1", "test3", "test4"]))