import datetime


class Dog:

    __colors = ["white", "black", "red", "mixed"]

    def __init__(self, name, breed, color, dob):
        self.name = name

        self.set_color(color)

        self.__dob = dob
        self.__breed = breed

    def get_dob(self):
        return self.__dob
    
    def get_age(self):
        return f"{datetime.datetime.now().year - self.__dob} years"
    
    def set_color(self, color):
        if color in Dog.__colors:
            self.__color = color
        else:
            self.__color = Dog.__colors[-1]
        
    def get_color(self):
        return self.__color

    def get_breed(self):
        return self.__breed
    
    color = property(get_color, set_color)
    breed = property(get_breed)

d = Dog("Zefirka", "wss", "pink", 2020)
# print(d.__dob)
print(d.get_dob(), d.get_age())

print(d.get_color())
d.set_color("black")
print(d.get_color())
d.set_color("pink")
print(d.get_color())

d.color = "white"
print(d.color)
print(d.breed)
d.breed = "test"