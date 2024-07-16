
l = [3,45,6,8,8,6,4,2,12,3,4,6,8,9,9]

# l.sort()

# print(l)

# m = sorted(l)
# print(l)
# print(m)

# is_sorted = True

# for i in range(len(m)-1):
#     if m[i] > m[i+1]:
#         is_sorted = False
#         break

# print(is_sorted)

print(l)

count = 0

for j in range(len(l)-1):
    for i in range(len(l)-1-j):
        count += 1
        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]

    print(l, j)

print(count)


l = [3,45,6,8,8,6,4,2,12,3,4,6,8,9,9]
count = 0
for j in range(len(l)):
    min_idx = j
    for i in range(j+1, len(l)):
        count += 1
        if l[i] < l[min_idx]:
            min_idx = i
    l[j], l[min_idx] = l[min_idx], l[j]
    print(l)

print(count)


# timsort
# merge sort
# insertion sort