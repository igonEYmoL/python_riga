def hell_nom(name,age=30):
    result = f"Hello {name}, you are {age} years old"
    return result

print(hell_nom("John",10))
print(hell_nom("Mike"))

flour = {"type": "all-purpose","amount": 500}
eggs = {"type": "large","amount": 2}
butter = {"type": "unsalted","amount": 250}




def bake_croissant(flour: dict, eggs: dict, butter: dict):
    if flour["amount"] > 30 and eggs["amount"] > 1 and butter["amount"] > 100:
        return "It's possible to bake croissant"
    else:
        return "Impossible to bake croissant"    

print(bake_croissant(flour,eggs,butter))