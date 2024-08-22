"""
    3. Write a program that takes a string as input and returns a
    dictionary with the count of each word in the string.
"""

user_string = [i for i in input("write the text: ").split(' ') if len(i) != 0]
print(user_string)

res = {}

for word in user_string:
    res[word] = res.get(word, 0) + 1

print(res)
