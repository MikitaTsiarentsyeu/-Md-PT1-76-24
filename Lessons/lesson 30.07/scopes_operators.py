global_number = 5

def change_global_number():
    global global_number
    global_number = 2
    print(global_number)

change_global_number()
print(global_number)


global_list = [5]

def change_global_list():
    global_list[0] = 2
    print(global_list)

print(global_list)
change_global_list()
print(global_list)

def outer():

    outer_value = "outer"

    def inner():

        nonlocal outer_value
        outer_value = "new outer"
        print(outer_value)
        inner_value = "inner"

    print(outer_value)

    return inner

new_func = outer()
new_func()