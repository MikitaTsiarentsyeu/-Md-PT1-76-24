def level1():
    print("level 1 started")
    level2()
    print("level 1 ended")

def level2():
    print("\tlevel 2 started")
    level3()
    print("\tlevel 2 ended")

def level3():
    print("\t\tlevel 3 started")
    level4()
    print("\t\tlevel 3 ended")

def level4():
    print("\t\t\tlevel 4 started")
    # level1()
    print("\t\t\tlevel 4 ended")

level1()


def level(n, counter=1):
    if counter == n+1:
        return
    print('\t'*(counter-1)+f"level {counter} started")
    level(n, counter+1)
    print('\t'*(counter-1)+f"level {counter} ended")

level(6)


l = [1,2,[3,4,5,[6,7,8,[10]]]]


# def flatten(l):

#     res = []
#     for i in l:
        
#         if isinstance(i, list):
#             for j in i:

#                 if isinstance(j, list):
#                     for k in j:

#                         if isinstance(k, list):

#                             for m in k:
#                                 res.append(m)
#                         else:
#                             res.append(k)
#                 else:
#                     res.append(j)
#         else:
#             res.append(i)

#     return res


def flatten(l, res=[]):
    
    for i in l:
        if isinstance(i, list):
            flatten(i)
        else:
            res.append(i)

    return res

print(flatten(l))