def times(a, b):
    return a*b


print(times(2, 3))
print(times([2], 3))
print(times("2", 3))

def times_for_int(a:int, b:int) -> int:
    """This function will multiply int values
    a: int - first param
    b: int - second param
    returns: int or None
    """
    if isinstance(a, int) and isinstance(b, int):
        return a*b
    
print(times_for_int(2, 3))
print(times_for_int(2, 3.01))


def eq(l1, l2):
    for i in l1:
        if i not in l2:
            return False
    for i in l2:
        if i not in l1:
            return False
    return True

# def eq(l1, l2):
#     return set(l1) == set(l2)

print(eq([1,2,3], (1,2,3)))
print(eq(["1","2","3"], "123"))


# def sum(a, b):
#     return a+b

# def sum(a, b, c):
#     return sum(sum(a, b), c)

# sum(1,2,3)