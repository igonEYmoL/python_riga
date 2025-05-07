class Superhero:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def use_power(self):
        print(f"{self.name} uses {self.power}!")
    
    def set_quality(self, quality):
        self.quality = quality
    
    def use_quality(self):
        print(f"{self.name} is known for their {self.quality}.")
    
    def printname(self):
        print(f"Superhero name: {self.name}")

hero1 = Superhero("Superman", "flight")
hero2 = Superhero("Batman", "stealth")
hero3 = Superhero("WonderWoman", "super strength")

hero1.use_power()
hero2.use_power()
hero3.use_power()

hero1.set_quality("bravery")
hero2.set_quality("intelligence")
hero3.set_quality("wisdom")

hero1.use_quality()
hero2.use_quality()
hero3.use_quality()

hero1.printname()
hero2.printname()
hero3.printname()


