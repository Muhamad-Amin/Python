""" Membuat game saling serang """


class Hero:
    def __init__(self, name, health, attactPower, arrmorNumber) -> None:
        self.name = name
        self.health = health
        self.attactPower = attactPower
        self.arrmorNumber = arrmorNumber

    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}")
        lawan.diserang(self, self.attactPower)

    def diserang(self, lawan, attactPower_lawan):
        print(f"{self.name} diserang {lawan.name}")
        attact_diterima = attactPower_lawan / self.arrmorNumber
        print(f'serangan terasa adalah {str(attact_diterima)}")')
        self.health -= attact_diterima
        print(f"darah {self.name} tersisa {str(self.health)}")


sniper = Hero("sniper", 100, 10, 5)
rikimaru = Hero("rikimaru", 100, 20, 10)


rikimaru.serang(sniper)
sniper.serang(rikimaru)
