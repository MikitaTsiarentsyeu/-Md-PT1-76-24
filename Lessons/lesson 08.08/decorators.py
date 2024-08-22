

def do_twice(func):
    def wrapper():
        func()
        func()
    return wrapper

def test_func():
    print("I am test func")

# test_func_twice = do_twice(test_func)

# test_func_twice()

test_func = do_twice(test_func)

# test_func()


def do_twice(func):
    def wrapper():
        func()
        func()
    return wrapper


def authorize(func):
    CODE = 42
    def wrapper():
        code = input("Please enter the secret code\n")
        if int(code) == CODE:
            func()
        else:
            print("You don't have right to perform this operation")
    return wrapper


@authorize
# @do_twice
def new_test_func(x):
    print("I am new test func")

new_test_func()