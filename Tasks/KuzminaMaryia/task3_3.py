from collections import Counter


text1 = input("Enter text: ")


print(Counter(["".join(filter(str.isalpha, x.lower())) for x in text1.split() if "".join(filter(str.isalpha, x.lower()))]))