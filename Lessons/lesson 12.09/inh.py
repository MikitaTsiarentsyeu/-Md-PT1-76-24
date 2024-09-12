class Animal:

    def __init__(self, name):
        self.name = name

    def make_a_sound(self):
        print("WAAAAAGH")

    # def move(self):
    #     pass




class FlyingAnimal(Animal):

    def __fly(self):
        print("I'm flying")

    def make_a_sound(self):
        print("I'm flying animal!")

    def move(self):
        self.__fly()

class SwimmingAnimal(Animal):

    def __swim(self):
        print("I'm swimming")

    def make_a_sound(self):
        print("I'm swimming animal!")

    def move(self):
        self.__swim()


class RunningAnimal(Animal):

    def __run(self):
        print("I'm running")

    def make_a_sound(self):
        print("I'm running animal!")

    def move(self):
        self.__run()


class Pelican(FlyingAnimal, SwimmingAnimal): pass

p = Pelican("pelican")
# p.swim()
# p.fly()

class Otter(SwimmingAnimal, RunningAnimal): pass

o = Otter("otter")
# o.run()
# o.swim()

class Duck(RunningAnimal, SwimmingAnimal, FlyingAnimal):
    "what a duck?"
    pass

    def __init__(self, name, color):
        super().__init__(name)
        print(self.name)
        self.color = color
    
    # def make_a_sound(self):
    #     print("squak!")

d = Duck("duck", "black")
# d.fly()
# d.swim()
# d.run()

d.make_a_sound()

print(Duck.__mro__)
d.move()
