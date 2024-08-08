def bad_generator():
    print("first yield")
    yield 1
    print("second yield")
    yield "test"

    return "final value?"

    print("third yield")
    yield False

# bg = bad_generator()

for i in bad_generator():
    print(i)


def my_range(finish, start=0, stride=1):
    while start < finish:
        yield start
        start += stride

for i in my_range(10):
    print(i)

for i in my_range(10, 1, 3):
    print(i)




def fibonacci(n):
    a, b = 0, 1
    count = 0
    while True:
        yield a
        count += 1
        if count == n:
            break
        a, b = b, a + b

fib = iter(fibonacci(5))
while True:
    try:
        print(next(fib))
    except StopIteration:
        break

l = [2,3,5,4, [8,6,9, [4,5,6,7]]]

def flatten(l, res=[]):
    for i in l:
        if isinstance(i, list):
            flatten(i)
        else:
            res.append(i)

    return res

print(flatten(l))


def flatten_gen(l):
    for i in l:
        if isinstance(i, list):
            yield from flatten_gen(i)
        else:
            yield i

for i in flatten_gen(l):
    print(i)


# def infinity():
#     while True:
#         yield "infinity"

res = (x for x in range(10))
print(res)

# def test():
#     for x in range(10):
#         yield x

def even_cubes(n):
    for i in range(n):
        if i % 2 == 0:
            yield i**3

print(list(even_cubes(11)))

even_cubes = (i**3 for i in range(11) if i % 2 == 0)

print(list(even_cubes))
print(list(even_cubes))