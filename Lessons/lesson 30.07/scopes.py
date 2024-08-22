for i in range(5):
    print(i)

print(i)

[print(j) for j in range(5)]
# print(j)

test_val = "test"

def scopes_test(test_val="default value"):
    print(test_val)
    test_val = "new value"
    print(test_val)

scopes_test()
print(test_val)


global_value = 10

def outer_local():

    outer_local_val = 5

    print([inner_local_val*outer_local_val for inner_local_val in range(10)])

    # print(inner_local_val)

    def inner_local():

        inner_local_val = "inner local val"
        print(global_value)
        print(outer_local_val)

    inner_local()


outer_local()




