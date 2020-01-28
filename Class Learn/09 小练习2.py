# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 20/1/8 -*-

"""
练习2：模仿LoL定义两个英雄类
要求：
    英雄需要有昵称、攻击值、生命值等属性；
    实例化出两个英雄对象；
    英雄之间可以互殴，被殴打的一方掉血，血量小于0则判定为死亡。
"""

class Garen(object):
    camp = 'Demacia'

    def __init__(self, nikename, life_value, aggressivity):
        self.nikename = nikename
        self.life_value = life_value
        self.aggressivity = aggressivity

    def attack(self, enemy):
        enemy.life_value -= self.aggressivity

        if enemy.life_value <= 0:
            print('{name} is loss'.format(name=self.nikename))


class Riven(object):
    camp = 'Noxus'

    def __init__(self, nikename, life_value, aggressivity):
        self.nikename = nikename
        self.life_value = life_value
        self.aggressivity = aggressivity

    def attack(self, enemy):
        enemy.life_value -= self.aggressivity

        if enemy.life_value <= 0:
            print('{name} is loss'.format(name=Garen.camp))



g1 = Garen(nikename='草丛伦', life_value=50, aggressivity=30)
r1 = Riven(nikename='呆瑞文', life_value=80, aggressivity=50)


# 对象之间交互运行
print('生命值为：{value}'.format(value=r1.life_value))
r1.attack(enemy=g1)
print('生命值为：{value}'.format(value=r1.life_value))

# 上述代码有冗余