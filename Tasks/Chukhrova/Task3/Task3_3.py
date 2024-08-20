"""
3. Write a program that takes a string as input and returns a dictionary 
with the count of each word in the string.
"""

user_str = input("Please enter a string:")
word_dic = {}
for word in user_str.split(" "):
    if word in word_dic:
        word_dic[word] += 1
    else:
        word_dic[word] = 1
print(word_dic)