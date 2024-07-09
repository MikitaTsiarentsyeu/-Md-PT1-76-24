t = (1,2,3,4,5,"test",[7,8,9])
t = 1,2,3,4,5

print(t, type(t))

l = (1,)
l = 1,
print(l, type(l))

t = tuple("test string")
print(t, type(t))

print((1,2,3)+(4,5,6)*3)

print(t[0], t[2:7:2])

print(len(t))

# t[0] = 0 TypeError

# t.append(10) AttributeError

del t