""" Latihan Encapsulasi """

import os


class Hero:
    # private class variable
    __jumlah = 0

    def __init__(self, name, health, attPower, armor) -> None:
        self.__name = name
        self.__healthStandar = health
        self.__attPowerStandar = attPower
        self.__armorStandar = armor
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthStandar * self.__level
        self.__attpower = self.__attPowerStandar * self.__level
        self.__armor = self.__armorStandar * self.__level

        self.__health = self.__healthMax

        Hero.__jumlah += 1

    @property
    def info(self):
        return f"{self.__name} level {self.__level} : \n\thealth = {self.__health}/{self.__healthMax} \n\tattct = {self.__attpower} \n\tarmor = {self.__armor}"

    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self, addExp):
        self.__exp += addExp
        if self.__exp >= 100:
            print(self.__name, "level up")
            self.__level += 1
            self.__exp -= 100

            self.__healthMax = self.__healthStandar * self.__level
            self.__attpower = self.__attPowerStandar * self.__level
            self.__armor = self.__armorStandar * self.__level

    def attact(self, musuh):
        self.gainExp = 50


slardar = Hero("slardar", 100, 5, 10)
axe = Hero("axe", 100, 5, 10)
os.system("cls")
print(slardar.info)

for i in range(1, 4):
    slardar.attact(axe)
print(slardar.info)
