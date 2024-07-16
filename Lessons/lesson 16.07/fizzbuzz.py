for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz") 
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)

l = [("fizz"*(i % 3 == 0))+("buzz"*(i % 5 == 0)) or i for i in range(1, 100)]
print(l)