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
rikimaru = Hero("rikimaru", 100, 5, 10)

input_user = int(
    input(
        "pilih salah satu yang ingin anda serang sebanyak 10x \n1. sniper \n2. rikimaru \n:"
    )
)

while True:
    for i in range(0, 10):
        if input_user == 1:
            rikimaru.serang(sniper)
        elif input_user == 2:
            sniper.serang(rikimaru)
        else:
            print(f"{input_user} tidak ada dalam pilihan")
    akhir = input("apakah anda ingin menyerangnya lagi (y/n)?: ")
    if akhir == "y" or akhir == "Y":
        pass
    else:
        break
