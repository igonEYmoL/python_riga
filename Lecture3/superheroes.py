class Superhero:
    def __init__(self, name, power, origin, frends, action_power):
        self.name = name
        self.power = power
        self.frends = frends
        self.origin = origin
        self.action_power = action_power
        self.energy = 100

    def use_power(self):
        print (f"{self.name} uses {self.action_power} to activate their {self.power}.")
    
    def set_quality(self, quality):
        self.quality = quality
    
    def use_quality(self):
        print(f"{self.name} is known for their {self.quality}.")
    
    def printname(self):
        print(f"Superhero name: {self.name}")

    def printpower(self):
        print(f"Superhero power: {self.power}")
    
    def printorigin(self):
        print(f"Superhero origin: {self.origin}")
    
    def printfrends(self):
        print(f"Superhero frends: {self.frends}")


hero1 = Superhero("Superman", "flight", "Krypton", "SuperWoman", "heart")
hero2 = Superhero("Batman", "stealth" , "Earth", "Superman", "hand")
hero3 = Superhero("WonderWoman", "super strength" , "Themyscira", "Batman", "brain")

hero1.use_power()
hero2.use_power()
hero3.use_power()



