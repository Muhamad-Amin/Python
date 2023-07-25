class Hero:
    def __init__(self, name, helath):
        self.name = name
        self.helath = helath


class Hero_intelligent(Hero):
    pass


class Hero_strength(Hero):
    pass


lina = Hero("lina", 100)
techies = Hero_intelligent("techies", 50)
axe = Hero_strength("axe", 200)

print(lina.name)
print(lina.__dict__)
print(techies.__dict__)
print(axe.__dict__)
