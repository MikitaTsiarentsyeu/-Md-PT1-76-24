s = {1,1,1,2,2,3,3,4,4,4}

print(s, type(s))

s = set("test string")
print(s)

print(hash("test"))
print(hash("test"))

l = [1,1,1,2,2,3,34,4,5,56,7,7,5,3,12,1,23,43,5,7,8,8,"t","e","s","t"]

print(set(l))

l = list(set(l))
print(l)

s = "test str"
s = str(set(s))
print(s)

s = "test str"
s = ''.join(list(set(s)))
print(s)


print([1,2,3]==[3,2,1])
print(set([1,2,3])==set([3,2,1,1,1,1,1,1,1,1,1,1]))
print(set("test")==set(["t", "s", "e"]))

target = set("1234567890.")
print(target)

test_s = "234.235778"
print(set(test_s))
print(set(test_s).issubset(target))

s = {1,2,3,4,5}
s.add(1)
s.add(6)
print(s)

s.update([4,5,6,7,8,9])
print(s)

s.remove(7)
print(s)

if 7 in s:
    s.remove(7)
    print(s)

s.discard(7)
print(s)

print(s.pop(), s)
print(s.pop(), s)
print(s.pop(), s)

print({1,2,3,4,5}.issuperset({1}))
s = {}
print(s, type(s))

s = set()
print(s, type(s))

print({1,2,3,4,5}.intersection({3,4,5,6,7}))
print({1,2,3,4,5}.union({3,4,5,6,7}))