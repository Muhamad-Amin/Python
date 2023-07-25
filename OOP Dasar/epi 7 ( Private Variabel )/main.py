""" private variable """


class Hero:
    # class variable
    jumlah = 0

    def __init__(self, name, health):
        self.name = name
        self.health = health

        # variable instance private
        self.__private = "private"

        # variable instace protected
        self._protected = "protected"


lina = Hero("lina", 100)

print(lina.__dict__)
lina._protected = "testing"
print(lina.__dict__)
print(lina._protected)
