import random

# while True:
#     print("HeLlO!", random.randint(1, 10))

x = 0

while x < 5:
    x += 2
    print(x)
else:
    print("the end of the loop")

print("the end")

s = "test str"
# i = 0
# while i < len(s):
#     print(s[i])
#     i += 1

for symbol in s:
    print(symbol)
else:
    print("the end")


x = 0
while True:
    x += 1
    print(x)
    if x == 5:
        break
else:
    print("the end of the loop")

for s in "test str":
    if " " in s:
        continue
    if s == " ":
        break
    print(s)
else:
    print("the end of the loop")


x = -1

while x < 11:
    x += 1
    if x % 2 == 1:
        continue
    print(x)


print("the end")

