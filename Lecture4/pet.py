class dog:
    def __init__(self, name, color, eye_color, height, weight, length):
        self.name = name
        self.color = color
        self.eye_color = eye_color
        self.height = height
        self.weight = weight
        self.length = length


    def Sit(self):
        print(f"{self.name} is sitting.")

    def Lay_down(self):
        print(f"{self.name} is laying down.")
    
    def Shake(self):
        print(f"{self.name} is shaking hands.")
    
    def Come(self):
        print(f"{self.name} is coming.")
    
    def describe(self):
        print(f"Nom: {self.name}")
        print(f"Couleur: {self.color}")
        print(f"Couleur des yeux: {self.eye_color}")
        print(f"Taille: {self.height} in")
        print(f"Poids: {self.weight} in")
        print(f"Longueur: {self.length} pounds")

Bobby = dog("Bobby", "brown", "black", 50, 20, 30)
Bobby.Sit()
Bobby.Lay_down()
Bobby.Shake()
Bobby.Come()
Bobby.describe()

class cat:
    def __init__(self, name, color, eye_color, height, weight, length):
        self.name = name
        self.color = color
        self.eye_color = eye_color
        self.height = height
        self.weight = weight
        self.length = length


    def Sit(self):
        print(f"{self.name} is sitting.")

    def Lay_down(self):
        print(f"{self.name} is laying down.")
    
    def Shake(self):
        print(f"{self.name} is shaking hands.")
    
    def Come(self):
        print(f"{self.name} is coming.")
    
    def describe(self):
        print(f"Nom: {self.name}")
        print(f"Couleur: {self.color}")
        print(f"Couleur des yeux: {self.eye_color}")
        print(f"Taille: {self.height} in")
        print(f"Poids: {self.weight} in")
        print(f"Longueur: {self.length} pounds")

Mimi = cat("Mimi", "white", "blue", 20, 10, 15)
Mimi.Sit()
Mimi.Lay_down()
Mimi.Shake()
Mimi.Come()
Mimi.describe()
