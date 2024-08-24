class Dog:

    def __init__(self, name, breed, color):
        self.name = name
        self.breed = breed
        self.__color = color
        self.__age = 0

    def get_color(self):
        return self.__color

    # def set_color(self, color):
    #     pass

    def get_age(self):
        return f"{self.__age} years"

    def set_age(self, age):
        if age > 0 and age < 30:
            self.__age = age

    def bark(self):
        print(f"woof! my name is {self.name}")


Zefirka = Dog("Zefirka", "wss", "white")
print(Zefirka.name)
Zefirka.__color = "black"
print(Zefirka.get_color())

Zefirka.set_age(4)
print(Zefirka.get_age())