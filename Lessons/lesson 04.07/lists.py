l = []

print(l, type(l), len(l))

l = [1,2,3,4, "five", 6.00000000000000000000000000000000001]

print(l, type(l), len(l))

print(str(l))

print([1,2,3]+[4,5,6])
print([1]*5)

print(l[0], l[1], l[2])
print(l[::-1])

l[0] = 1.0
print(l)

n = len(l)
# l[n] = "the last one" IndexError
# print(l)

l.append("the last one")
print(l)

l.extend("the last one")
print(l)

print(list("test str"))

l.insert(0, "new first one")
print(l)

l.remove(6.0)
print(l)

l.remove(' ')
print(l)

print(' ' in l)

print(l.pop())
print(l.pop(0))
print(l)

del l[0]
print(l)

del l[5]
print(l)

del l[:6]
print(l)

# del l
# print(l)

l.clear()
print(l)

l1 = [1,2,3,4,5]
l2 = [1,2,3,4,5]
print(l1 == l2)

l = [1]

m = l

del l
print(m)
