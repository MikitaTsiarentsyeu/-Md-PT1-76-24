d = {}
print(d, type(d))

d = {"one":1, "two":2, "three":3}
print(d)

print(d["one"])

# print(d[1]) KeyError

d["one"] = 1.0
print(d)

d[5] = "five"
print(d)

d = {9103976271:[["Reina", "Meinhard"], ["Memphis", "Tennessee"]],
4199392609:[["Stephanie", "Bruce"], ["Greensboro", "North Carolina"]],
9099459979:[["Ermes", "Angela"], ["Dallas", "Texas"]],
6123479367:[["Lorenza", "Takuya"], ["Indianapolis", "Indiana"]],
7548993768:[["Margarete", "Quintin"], ["Raleigh", "North Carolina"]]}

num = int(input("enter phone number:"))

if num in d:
    res = d[num]
    print(f"{res[0]} from {res[1]}")
else:
    print("phone was not found")

# print(d.get(num))