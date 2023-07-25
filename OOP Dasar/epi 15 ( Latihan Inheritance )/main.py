# import hero

from hero import HeroIntelligent, HeroStrength


# lina = hero.HeroIntelligent("lina")
# slardar = hero.HeroStrength("slardar")

lina = HeroIntelligent("lina")
slardar = HeroStrength("slardar")

lina.show_info()
slardar.show_info()

lina.gainExp = 200
slardar.gainExp = 250

lina.show_info()
slardar.show_info()
