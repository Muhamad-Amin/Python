class Hero:  # templet
    pass


hero1 = Hero()  # object / intance
hero2 = Hero()
hero3 = Hero()


hero1.name = "snipper"
hero1.health = 300

hero2.name = "sven"
hero2.health = 200

hero3.name = "ucup"
hero3.health = 1000

print(hero1)  # cek object atau tidak
print(hero1.__dict__)  # cek apa saja atributnya
print(hero1.name)  # akses nama
