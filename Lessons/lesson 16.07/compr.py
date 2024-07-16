
l = [x for x in range(10)]
print(l)

# tem_list = []
# for x in range(10):
#     tem_list.append(x)
# l = tem_list
# print(tem_list)

l = [x*x for x in range(10)]
print(l)

# tem_list = []
# for x in range(10):
#     tem_list.append(x*x)
# l = tem_list
# print(tem_list)

l = [x*x for x in range(100) if x%2 == 0]
print(l)

# tem_list = []
# for x in range(10):
#   if x%2 == 0:
#     tem_list.append(x*x)
# l = tem_list
# print(tem_list)


l = [x*x for x in range(100) if x%2 == 0 if x%5 == 0]
print(l)

# tem_list = []
# for x in range(10):
#   if x%2 == 0:
#       if x%5 == 0:
#           tem_list.append(x*x)
# l = tem_list
# print(tem_list)

s = {x*x for x in range(100) if x%2 == 0 if x%5 == 0}
print(s, type(s))

d = {str(x):x*x for x in range(100) if x%2 == 0 if x%5 == 0}
print(d, type(d))


l = [str(x)+str(y) for x in range(2) for y in range(3)]
print(l)

# tem_list = []
# for x in range(2):
#     for y in range(3):
#         tem_list.append(str(x)+str(y))
# l = tem_list
# print(tem_list)