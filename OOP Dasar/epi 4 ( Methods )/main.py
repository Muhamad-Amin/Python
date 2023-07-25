class Hero:  # templet
    # class variabel
    jumlah_hero = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variables
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah_hero += 1
        print(f"membuat hero dengan nama {inputName}")

    # void function ( method tanpa return )
    def siapa(self):
        print(f"Namaku adalah {self.name}")

    # method dengan argument
    def healthUp(self, up):
        self.health += up

    # method dengan return
    def getHealth(self):
        return self.health


hero1 = Hero("snipper", 100, 10, 5)
hero2 = Hero("mario bros", 90, 5, 10)

print(hero1.__dict__)
print(hero2.__dict__)

hero1.siapa()
hero1.healthUp(10)

print(hero1.getHealth())
