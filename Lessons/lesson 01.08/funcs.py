from functools import reduce

l = [1,2,3,4,5,6,7,8,9]
map_obj = map(print, l)
print(map_obj)

print(range(10))

for i in map_obj: pass

print(list(map(int, "12345")))

print([x**2 for x in map(int, "12345")])

print(list(map(lambda n: chr(n*10), range(10))))

print([(lambda n: chr(n*10))(x) for x in range(10)])

print(list(map(lambda n: chr(n*10), filter(lambda x: x>5, map(lambda x: x+1, range(10))))))

print(reduce(lambda x, y: x+y, [1,2,3,4,5]))

print(reduce(lambda x, y: f"{x}-{y}", [1,2,3,4,5]))
"1-2"
"1-2-3"
"1-2-3-4"
"1-2-3-4-5"

l = [2,4,5,56,32,1,3,5,7,9,9]

print(reduce(lambda x, y: x if x < y else y, l))