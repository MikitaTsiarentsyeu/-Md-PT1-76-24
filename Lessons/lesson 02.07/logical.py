import math

x = True
print(type(x))

x = False
print(type(x))

print(False == 0)
print(False + False + False + True)

print(isinstance(False, bool))
print(isinstance(False, float))
print(isinstance(False, int))

print(bool(278), bool(-110.01152), bool("ytrfytfy"))
print(bool(0), bool(""), bool(None))

print(type(None))

print(math.pow(2, 3))
x = math.pow(2, 3)
print(x)

x = print("test print")
print("test print result was", x)

print(not True)
print(not False)

print(not "test")

print(True and False)
print(8 and "test")
print("test" and 8)
print("test" and 0)
print(0 and "test")
print("left") and print("right")

print("left") or print("right")