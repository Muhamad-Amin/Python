""" Magic Method """


class Mangga:
    # magic method
    def __init__(self, name, jumlah):
        self.name = name
        self.jumlah = jumlah

    def __repr__(self) -> str:
        return f"Debug - Mangga : {self.name} dengan jumlah : {self.jumlah}"

    def __str__(self) -> str:
        return f"Mangga : {self.name} dengan jumlah : {self.jumlah}"

    def __add__(self, object):
        return self.jumlah + object.jumlah

    @property
    def __dict__(self):
        return "object ini mempunya nama dan jumlah"


belanja1 = Mangga("arumanis", 10)
belanja2 = Mangga("mana lagi", 5)
print(repr(belanja1))
print(belanja2)
print(belanja1 + belanja2)
print(belanja1.__dict__)
