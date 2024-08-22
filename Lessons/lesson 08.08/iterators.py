for i in "test str":
    print(i)

for i in [1,2,3,4,5]:
    print(i)

for i in {1:"one", 2:"two"}:
    print(i)


print("")

l = [1,2,3,4,5]
# for i in l:
#     print(i)


l_iter = iter(l)
while True:
    try:
        i = next(l_iter)
    except StopIteration:
        break
    print(i)


r = range(10)
print(r, type(r))

r_iter = iter(r)
print(next(r_iter))
print(next(r_iter))
print(next(r_iter))
print(next(r_iter))