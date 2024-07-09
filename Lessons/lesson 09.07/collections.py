s = "test str"

l = [1,2,3,4,5,s]

d = {"one":[1,1,1,1,1,1,1]}

print(s[0], l[0], d["one"])

print(list(s))

print(list(d))

# print(dict(s)) #ValueError

print([1,2,3]==[1,2,3])
print([1,2,3]==[3,2,1])


l = [[1,2,3, ["t", "w", "r"]], (3,4,5), {7,8,9}]
l = [1]
l.append(l)
print(l[1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1])

l = [[1,2,3], [4,5,6], [7,8,9]]
print(l[0][0], l[0][1], l[0][2])

t = (l, "test")
t[0][0][0] = 111
print(t)

l = "test"
print(l)

print(t[0], t)

x = y = 10
print(x, y)

print(id(x), id(y))

d = {(1,2,3):"one, two, three"}
print(d)

print(d[(1,2,3)])

# d[t] = "test" TypeError

l = [1,2,3]
m = [1,2,3]
print(id(l), id(m))
print(id(l)==id(m))
print(l is m)


l = (1,2,3)
m = (1,2,3)
print(id(l), id(m))
print(id(l)==id(m))
print(l is m)

x = 44
y = 44
print(x is y)

x = 444
y = 444
print(x is y)

x = "test"
y = "test"
print(x is y)

x = "test"
y = "t"+"e"+"s"+"t"
print(x is y)
