class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("Ini adalah showinfo di class Hero")
        print(f"{self.name} helath : {self.health}")


class Hero_intelligent(Hero):
    def __init__(self, name):
        super().__init__(name, 100)

    # override
    def showInfo(self):
        print("Ini adalah showinfo di subclass Hero_intelligent")
        print(f"{self.name} \n\tTipe : intellegint, \n\thealth : {self.health}")


class Hero_strength(Hero):
    def __init__(self, name):
        super().__init__(name, 200)


lina = Hero_intelligent("lina")
axe = Hero_strength("axe")

lina.showInfo()
axe.showInfo()
