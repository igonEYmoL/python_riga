class swiming():
    def __init__(self, below_water , above_water):
        self.__below_water = below_water
        self.__above_water = above_water
    def swim(self):
        print("I can swim")
        return None
    def set_below_water(self, below_water):
        self.__below_water = below_water
    
    def set_above_water(self, above_water):
        self.__above_water = above_water
    
    def get_below_water(self):
        return self.__below_water
    def get_above_water(self):
        return self.__above_water

class eating():
    def eat(self):
        print("I can eat")
        return None

class platypus(swiming, eating):
    def __init__(self, color, name):
        self.name = name
        self.color = color
    def eat(self):
        print (f"{self.name} is eating")
        return None
    
        
Nicolas = platypus("brown", "Nicolas")
Nicolas.set_below_water("2m")
Nicolas.set_above_water("1m")
Nicolas.get_below_water()
Nicolas.get_above_water()

Nicolas.eat()
Nicolas.swim()