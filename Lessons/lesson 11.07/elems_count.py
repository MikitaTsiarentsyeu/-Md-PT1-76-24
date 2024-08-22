l = [3,-1,5,6,78,7,5,3,2,3,5,76,8,90,0,63,1,26]

print(min(l), max(l))

min_elem = l[0]

for elem in l:
    if elem < min_elem:
        min_elem = elem

print(min_elem)

max_elem = l[0]

for elem in l:
    if elem > max_elem:
        max_elem = elem

print(max_elem)


min_elem = l[0]
min_index = 0
for i in range(1, len(l)):
    if l[i] < min_elem:
        min_elem = l[i]
        min_index = i

print(min_index, min_elem)

min_elem = l[0]
min_index = 0
for index, elem in enumerate(l):
    if elem < min_elem:
        min_elem = elem
        min_index = index

print(min_index, min_elem)


test_str = "some very long test string"

counts = []

for symbol in test_str:
    for pair in counts:
        if pair[0] == symbol:
            pair[1] += 1
            break
    else:
        counts.append([symbol, 1])

print(counts)


counts = {}

for symbol in test_str:
    if symbol in counts:
        counts[symbol] += 1
    else:
        counts[symbol] = 1

print(counts)   