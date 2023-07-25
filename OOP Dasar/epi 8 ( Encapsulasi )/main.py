""" Encapsulasi """


class Hero:
    def __init__(self, name, health, attactPower):
        self.__name = name
        self.__health = health
        self.__attPower = attactPower

    # getter
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    # setter
    def diserang(self, serangPower):
        self.__health -= serangPower

    def setAttPower(self, nilaiBaru):
        self.__attPower = nilaiBaru


# awal game
earhshaker = Hero("earhshaker", 50, 5)


# game berjalan
print(earhshaker.getName())
print(earhshaker.getHealth())
earhshaker.diserang(5)
print(earhshaker.getHealth())
