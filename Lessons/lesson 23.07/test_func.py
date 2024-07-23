

def my_sum(a, b):
    res = a + b
    return res

print(my_sum(2, 3))

def second_func():
    print("the second function")

def first_func():
    print("the first function")
    second_func()

first_func()

print(type(first_func), first_func, id(first_func))

# my_sum(1,2,3) error
# my_sum(1) error

def test_args_func(a, b, c):
    print(f"a={a}, b={b}, c={c}")

test_args_func(1, True, "test")
test_args_func(True, 1, "test")

# a = 5
# b = a
# print(a is b)

def test_ref(obj):
    print(id(obj))

value = 5
print(id(value))

test_ref(value)

def test_immutable_obj(obj):
    print(id(obj), obj)
    obj += 2
    print(id(obj), obj)

test_immutable_obj(value)
print(id(value), value)


def test_mutable_obj(obj):
    print(id(obj), obj)
    obj[0] += 2
    print(id(obj), obj)

value = [6]
print(id(value), value)
test_mutable_obj(value)
print(id(value), value)


# sign = "-"
# if sign == "+":
#     def operator(a, b):
#         return a+b
# elif sign == "*":
#     def operator(a, b):
#         return a*b
# else:
#     def operator(a, b):
#         return a+b

def operator(a, b, sign):
    if sign == "+":
        return a+b
    elif sign == "*":
        return a*b
    
    # return
    
print(operator(1, 2, "-"))

def test_return():
    print("without a return")
    # return 1
    # return 2
    # return 3

test_return()

print("it's over")