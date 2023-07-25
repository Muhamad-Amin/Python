""" Staticmethod dan Classmethod """


class Hero:
    # private class variabel
    __jumlah = 0

    def __init__(self, name) -> None:
        self.name = name
        Hero.__jumlah += 1

    # method ini hanya berlaku untuk object
    def getJumlah(self):
        return Hero.__jumlah

    # method ini tidak berlaku untuk object karena tidak ada selfnya
    # tapi berlaku untuk class
    def getJumlah1():
        return Hero.__jumlah

    # method static ( decorator ) menempel ke object dan class
    # ( agar bisa berlaku kedua method di atas )
    # kita menggunakan ini untuk menandakan kalau ini adalah method static
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah

    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah


sniper = Hero("sniper")
print(Hero.getJumlah1())
rikimaru = Hero("rikimaru")
print(sniper.getJumlah2())
drowranger = Hero("droranger")
print(Hero.getJumlah3())
