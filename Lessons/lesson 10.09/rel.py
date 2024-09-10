#aggregation - has a 'something'
#composition - consists of 'something'

class Engine:

    def __init__(self, power, volume):
        self.__power = power
        self.__volume = volume

    def get_power(self):
        return self.__power
    
    def get_volume(self):
        return self.__volume
    
    power = property(get_power)
    volume = property(get_volume)


#aggregation
class SerialCar:

    def __init__(self, engine, make, model):
        self.engine = engine
        self.__make = make
        self.__model = model

    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    make = property(get_make)
    model = property(get_model)

v2 = Engine(100, 1.2)
vw = SerialCar(v2, "vw", "golf")

print(vw.engine.power)

#aggresive composition
class SuperCar:

    class __Engine:

        def __init__(self, power, volume):
            self.__power = power
            self.__volume = volume

        def get_power(self):
            return self.__power
        
        def get_volume(self):
            return self.__volume
        
        power = property(get_power)
        volume = property(get_volume)


    def __init__(self, make, model, power=300, volume=8):
        self.__engine = SuperCar.__Engine(power, volume)
        self.__make = make
        self.__model = model

    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def get_power(self):
        return self.__engine.power
    
    def get_volume(self):
        return self.__engine.volume
    
    make = property(get_make)
    model = property(get_model)
    power = property(get_power)
    volume = property(get_volume)


#composition
class SuperCar:

    def __init__(self, make, model, power=300, volume=8):
        self.__engine = Engine(power, volume)
        self.__make = make
        self.__model = model

    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def get_power(self):
        return self.__engine.power
    
    def get_volume(self):
        return self.__engine.volume
    
    make = property(get_make)
    model = property(get_model)
    power = property(get_power)
    volume = property(get_volume)
