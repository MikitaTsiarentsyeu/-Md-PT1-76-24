class Food:

    MEAT_TYPE = 'meat'
    PLANT_TYPE = 'plant'
    TYPES = (MEAT_TYPE, PLANT_TYPE)

    def __init__(self, food_name, food_type):
        self.name = food_name
        if food_type in Food.TYPES:
            self.type = food_type
        else:
            self.type = Food.TYPES[-1]

    def __str__(self) -> str:
        return f"{self.name} of type {self.type}"
        

class Animal:

    def eat(self, something):
        print(f"eating {something}")

    def phe(self):
        print("phe...")

    def sleep(self):
        print("I'm sleeping")

    def walk(self):
        print("walking")


class Carnivore(Animal):


    def eat(self, something:Food):
        if something.type == Food.MEAT_TYPE:
            Animal.eat(self, something)
            self.sleep()
            self.walk()
        else:
            super().phe()

class Herbivore(Animal):

    def eat(self, something:Food):
        if something.type == Food.PLANT_TYPE:
            Animal.eat(self, something)
            self.walk()
            self.sleep()
        else:
            super().phe()


class Omnivore(Herbivore, Carnivore):
    
    def eat(self, something):
        if something.type == Food.MEAT_TYPE:
            Carnivore.eat(self, something)
        elif something.type == Food.PLANT_TYPE:
            Herbivore.eat(self, something)
        else:
            super().phe()



stake = Food("stake", Food.MEAT_TYPE)
grass = Food("grass", Food.PLANT_TYPE)

tigger = Carnivore()
rabbit = Herbivore()
piglet = Omnivore()

# for food in stake, grass:
#     print("---")
#     tigger.eat(food)


# for food in stake, grass:
#     print("---")
#     rabbit.eat(food)

print(Omnivore.__mro__)

for food in stake, grass:
    print("---")
    piglet.eat(food)