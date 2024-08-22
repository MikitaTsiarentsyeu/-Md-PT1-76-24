c, d, f = "cat", "dog", "fish"

pets = "a cat, a dog and a fish"

test_pets = "a " + c + ", a " + d + " and a " + f 

print(test_pets, test_pets == pets)

"a cat"
"a cat, a "
"a cat, a dog"
"a cat, a dog and a "
"a cat, a dog and a fish"

print("a {}, a {} and a {}".format(c, d, f))

print(f"a {c}, a {d} and a {f}")

print(f"high {25/4.9:.2f}")

# print("%s %d" % ("test", 45)) old way