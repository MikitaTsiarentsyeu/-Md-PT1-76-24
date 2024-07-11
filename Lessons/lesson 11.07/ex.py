a = 5
b = a

print(a, b, a==b)
print(id(a), id(b))

a += 2
# a = a + 2

print(a)
print(b)
print(id(a), id(b))

# b = a

b += 2
print(id(a), id(b))

c = 3+4
print(id(c))

d = 7
print(id(d))


a = [5]
b = a

print(a, b , id(a), id(b))

a[0] += 2
print(a, b , id(a), id(b))