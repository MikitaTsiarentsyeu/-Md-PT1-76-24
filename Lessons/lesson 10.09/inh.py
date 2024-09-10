class Parent:

    attr = "parent value"

    def method(self):
        print("parent method")

class Child(Parent):

    attr = "child value"

c = Child()
print(c.attr)
c.method()