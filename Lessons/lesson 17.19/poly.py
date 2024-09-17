class Animal:

    def say_something(self):
        print("WAAAAGH")

class Cat:

    def say_something(self):
        print("meaw")

class Dog:

    def say_something(self):
        print("bork!")

class Human:

    def say_something(self):
        print("Hello, my name is Arcadiy")


for a in Animal(), Cat(), Dog(), Human(), object():
    a.say_something()