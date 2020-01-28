# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 20/1/8 -*-


class Hero(object):

    def __init__(self, nikename, life_value, aggressivity):
        self.nikename = nikename
        self.life_value = life_value
        self.aggressivity = aggressivity

    def attack(self, enemy):
        enemy.life_value -= self.aggressivity


# 子类也可以拥有自己一些新的属性技能等
class Garen(Hero):
    camp = 'Demacia'

    def attack(self, enemy):
        print('from Garen Class')




class Riven(Hero):
    camp = 'Noxus'





g = Garen(nikename='草丛伦', life_value=100, aggressivity=30)
print(g.camp)

r = Riven(nikename='呆瑞文', life_value=80, aggressivity=50)
print(g.attack(enemy=r))