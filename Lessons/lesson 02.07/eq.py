a = float(input("Please enter the a value\n"))
b = float(input("Please enter the b value\n"))
c = float(input("Please enter the c value\n"))

D = b*b - 4*a*c
print(D)

if D > 0:
    x1 = (-b + D**0.5)/(2*a)
    x2 = (-b - D**0.5)/(2*a)
    print("There are two roots -", x1, x2)
elif D == 0:
    x = -b/(2*a)
    print("There is one root -", x)
else:
    print("There are no roots")