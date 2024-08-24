def bark():
    print("woof!")

dog = {"breed":"", "name":"", "color":"", "bark":bark}

Zefirka = {"breed":"wss", "name":"Zefirka", "color":"white", "bark":bark}


x = 10
print(id(x), type(x))
print(id(int), type(int))
# print(id(type), type(type))
print(id(object), type(object))

# print(object.__dict__)
print(dir(object))

class Dog:

    breed = ""
    color = ""
    name = ""

    def bark(self):
        print(f"woof! my name is {self.name}")

print(id(Dog), type(Dog))

Zefirka = Dog()
Zefirka.breed = "wss"
Zefirka.color = "white"
Zefirka.name = "Zefirka"

print(Dog.name, Zefirka.name)

Max = Dog()
Max.breed = "shepherd"
Max.color = "black"
Max.name = "Max"

print(Dog.name, Zefirka.name, Max.name)

Max.bark()
Zefirka.bark()

# monkey patching

Max.profession = "shepherd"
print(Max.profession)
print(Zefirka.profession)


Max.breed = "homo sapiense"