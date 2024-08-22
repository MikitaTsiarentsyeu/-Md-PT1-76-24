
def evaluate(param1, param2, param3):
    print(param1, param2, param3)
    return param1*param2+param3


evaluate(2, 3, 4)
evaluate(param2=5, param1=1, param3=8)
evaluate(1, 5, 8)



def evaluate(param2, param1=1, param3=10):
    print(param1, param2, param3)
    return param1*param2+param3

evaluate(1, 2)
evaluate(1, param3=5)


def collect_items(item, items=[]):
    items.append(str(item))
    return items

items_list = []
collect_items(print, items_list)
print(items_list)

new_items = collect_items("test item")
print(new_items)

old_items = collect_items("another item")
print(old_items)



#args
print(1,2,3,4,5,6,7,8,9,10)

def my_sum(*args, sign="+"):
    print(args, type(args))
    res = 0 if sign == "+" else 1
    for i in args:
        res = res + i if sign == "+" else res * i
    return res

print(my_sum(1,2,3,4,5,6,7,8,9,10))

def my_print(*args, **kwargs):
    print(*args, sep=kwargs["separator"], end=kwargs["end"])

my_print(1,2,3,4,5,param1="one",param2="two",separator=',',end='.\n')

