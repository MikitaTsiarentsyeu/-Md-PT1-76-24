def apply(l:list, action):
    for i in l:
        action(i)


apply("some test str", print)


def lower_sorting(x):
    return x.lower()

test_str = "Abc Aac aaa"
print(sorted(test_str.split(), key=lower_sorting))

my_sum = lambda x, y: x+y
print(my_sum, my_sum(2, 3))

print((lambda x, y: x+y)(2, 3))

test_str = "Abc Aac aaa"
print(sorted(test_str.split(), key=lambda x: x.lower()))
print(sorted(test_str.split(), key=str.lower))

l = [("three", 3), ("one", 1), ("two", 2)]
print(sorted(l))
print(sorted(l, key=lambda x: x[1]))