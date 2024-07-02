

x = 1

if x == 0:
    print("it's zero")

    # if x != 10:
    #     print("x is not ten")
    
    # print("after nested if")
elif x == 1:
    print("it's one")

elif x == 2:
    print("it's two")

elif True:
    print("will execute if no other if/elif works")

else:
    print("it's not zero")

print("the end")


print("it's true") if x else print("it's not true")
# if x:
#     print("it's true")
# else:
#     print("it's not true")

res = "it's true" if x else "it's not true"
print(res)

