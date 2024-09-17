class FreightTrain:

    def __init__(self, count) -> None:
        self.cart_count = count

    def __str__(self):
        # return f"I'm a train of {self.cart_count} carts, choo-choo!"
        return f"{self.__class__.__name__}({self.cart_count})"
    
    def __len__(self):
        return self.cart_count
    
    def __int__(self):
        return self.cart_count
    

    def __eq__(self, other):
        if not isinstance(other, FreightTrain):
            return False
        
        return self.cart_count == other.cart_count
        

    # def __add__(self, other):
    #     try:
    #         return FreightTrain(self.cart_count + other.cart_count)
    #     except:
    #         raise TypeError("cannot add non-train objects")

    def __add__(self, other):
        if not isinstance(other, FreightTrain):
            raise TypeError("cannot add non-train objects")

        return FreightTrain(self.cart_count + other.cart_count)




print(FreightTrain(10))
# print(set())
t = FreightTrain(7)
print(len(t), int(t))

print(t == FreightTrain(10))
print(t == FreightTrain(7))
print(t == t)

tt = FreightTrain(10)

print(t+tt)