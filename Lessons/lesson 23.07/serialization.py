import json
import pickle

with open("test.json", 'r') as target:
    cars = json.load(target)

print(cars, type(cars))

cars[0]["is_electric"] = True

print(cars)

with open("test_new.json", 'w') as target:
    json.dump(cars, target)

d = {"colours":("red", "blue", "green")}


dumped = json.dumps(d)
print(repr(dumped))
# print(repr(json.dumps(print))) error

new_d = json.loads(dumped)
print(new_d, d == new_d)


with open("test_new.pickle", 'wb') as target:
    pickle.dump(print, target)

with open("test_new.pickle", 'rb') as target:
    my_print = pickle.load(target)

my_print("hello from the new print")