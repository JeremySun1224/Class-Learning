# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 20/1/8 -*-


"""
如果我们希望新建一个和父类相同方法的类，这样我们就会覆盖原先父类的方法，但是我们还是希望在别的地方重新调用父类的方法，
那么，这就涉及到一个新的知识点：在子类中重用父类的方法或属性。有两种方式：
    1、指名道姓的方法，Hero.attack()，这需要我们手动传值，这种方法是不依赖继承的。因为只有绑定方法才能自动传值
    2、super()会得到一个特殊的对象，专门用来继承父类的属性的。该方法依赖于继承。
"""

# 方式一：指明道姓
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

    def __init__(self, nikename, life_value, aggressivity, weapon):
        self.nikename = nikename
        self.life_value = life_value
        self.aggressivity = aggressivity
        # Hero.__init__(self, nikename, life_value, aggressivity)  # 还可以用指名道姓的方法，不依赖继承
        self.weapon = weapon

    def attack(self, enemy):
        Hero.attack(self, enemy=enemy)  # 方式1：指名道姓
        print('from Garen Class')


# 这时候调用触发的就是Garen类自己的__init__()方法，那么就需要多传一个参数weapon
g = Garen(nikename='草丛伦', life_value=100, aggressivity=30, weapon='金箍棒')
print(g.__dict__)

# 那么问题来了，我们虽然派生出了新的方法，但是可以看出代码又重复了。因为在实例化对象的时候，Garen()也有自己的__init__()方法


# 方式二：super()
class Hero(object):

    def __init__(self, nikename, life_value, aggressivity):
        self.nikename = nikename
        self.life_value = life_value
        self.aggressivity = aggressivity

    def attack(self, enemy):
        enemy.life_value -= self.aggressivity


class Garen(Hero):
    camp = 'Demacia'

    def attack(self, enemy):
        # 依赖于继承
        """
        super(自己的类名, self)，这样就能得到一个特殊的对象，相当于得到父类，它用的东西都是父类的。
        由于super(Garen, self)是一个对象，那么它调用的attack()就是一个绑定方法，
        第一个参数就不用传了，但是self还是要传的。
        """
        super(Garen, self).attack(enemy)
        print('from Garen Class')


class Riven(Hero):
    camp = 'Noxus'


g = Garen(nikename='草丛伦', life_value=100, aggressivity=30)
r = Riven(nikename='呆瑞文', life_value=80, aggressivity=50)
print(g.attack(enemy=r))
print(r.life_value)



class Hero(object):

    def __init__(self, nikename, life_value, aggressivity):
        self.nikename = nikename
        self.life_value = life_value
        self.aggressivity = aggressivity

    def attack(self, enemy):

        enemy.life_value -= self.aggressivity


# Garen可以有自己独特的属性，比如weapon为金箍棒
class Garen(Hero):
    camp = 'Demacia'

    def __init__(self, nikename, life_value, aggressivity, weapon):
        # self.nikename = nikename
        # self.life_value = life_value
        # self.aggressivity = aggressivity
        '''
        在Python2中的super()需要指定Garen和self
        super(Garen, self).__init__(nikename, life_value, aggressivity)  # 这是一种绑定方法，所以不用传self
        在Python3中，可以不用传入类名，但为了Python的版本兼容，最好写上
        '''
        super().__init__(nikename, life_value, aggressivity)
        self.weapon = weapon

    def attack(self, enemy):
        Hero.attack(self, enemy=enemy)  # 方式1：指名道姓
        print('from Garen Class')


g = Garen(nikename='草丛伦', life_value=100, aggressivity=30, weapon='金箍棒')
print(g.__dict__)



class A(object):
    def f1(self):
        print('from A')
        super().f1()  # super()不会管参照什么父类，它只会按照自己的MRO列表去找

class B(object):
    def f1(self):
        print('from B')

class C(A, B):
    pass

print(C.mro())  # [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]

c = C()  #
c.f1()

"""
打印结果：
    from A
    from B
"""