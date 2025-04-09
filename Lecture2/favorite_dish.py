Pasta = {"types": "Fusilli", "amount": 300}
Creams = {"types": "Liquid", "amount": 3000}
Salmon = {"types": "Smoke", "amount": 4000}
Riz = {"types": "Basmati", "amount": 600}

def favorite_dish(Pasta: dict, Creams: dict, Salmon: dict, Riz: dict):
    if Creams["amount"] > 30 and Salmon["amount"] > 100:
        if Pasta["amount"] > 200:
            return "It's possible to cook pasta with salmon"
        elif Riz["amount"] > 100:
            return "It's possible to cook rice with salmon"
        else:
            return "Impossible to cook with salmon"
    else:
        return "Impossible to cook with salmon"

while favorite_dish(Pasta, Creams, Salmon, Riz) != "Impossible to cook with salmon":
    if favorite_dish(Pasta, Creams, Salmon, Riz) == "It's possible to cook pasta with salmon":
        Pasta["amount"] -= 200
        Creams["amount"] -= 50
        Salmon["amount"] -= 100
        print("Cooking pasta with salmon...")
        print("It's possible to cook pasta with salmon")
        break
    if favorite_dish(Pasta, Creams, Salmon, Riz) == "It's possible to cook rice with salmon":
        Riz["amount"] -= 100
        Creams["amount"] -= 50
        Salmon["amount"] -= 100
        print("Cooking rice with salmon...")
        print("It's possible to cook rice with salmon")
        break
        

