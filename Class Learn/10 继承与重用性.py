# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 20/1/8 -*-

"""
什么事继承呢？
    继承指的是类与类之间的关系，是一种什么’是‘什么的关系，如果人类是动物；猪类是动物，他们同属于一个父类：人。
    继承的功能就是用来解决代码重用问题。
    继承是一种创建新类的方式。
    在Python中，新建的类可以继承一个或多个父类，父类又可以称为基类或超类，新建的类称为派生类或子类。
"""

# Python中类的继承分为单继承和多继承
# 创建父类
class ParentClass1(object):
    pass

class ParentClass2(object):
    pass

# 通过继承创建出子类SubClass1和SubClass2
# 创建子类
class SubClass1(ParentClass1):  # 继承一个父类
    pass

class SubClass2(ParentClass1, ParentClass2):  # 继承多个父类
    pass


# 查看继承
# 查看SubClass1都继承了哪些父类
print(SubClass1.__bases__)  # (<class '__main__.ParentClass1'>,)
# 查看SubClass2都继承了哪些父类
print(SubClass2.__bases__)  # (<class '__main__.ParentClass1'>, <class '__main__.ParentClass2'>)


# 总结对象之间相似的特征与技能得到类，那么我们可以通过总结对象之间相似的特征与技能得到父类

# Garen和Riven都是英雄，由此可先定义英雄类Hero
class Hero(object):
    def __init__(self, nikename, life_value, aggressivity):
        self.nikename = nikename
        self.life_value = life_value
        self.aggressivity = aggressivity

    def attack(self, enemy):
        enemy.life_value -= self.aggressivity


# 子类可以重用父类的所有属性与功能
class Garen(Hero):
    pass


g1 = Garen(nikename='钢门', life_value=100, aggressivity=80)
print(g1)


"""
查找属性顺序:
    1、对象本身；
    2、对象所在的类；
    3、对象所在的类的父类去找。
"""

# 属性查找
class Foo(object):

    def f1(self):
        print('from Foo.f1')

    def f2(self):
        print('from Foo.f2')
        self.f1()


class Bar(Foo):

    def f1(self):
        print('from Bar.f1')


b = Bar()
print(b.__dict__)  # 打印为{}，因为Bar()没有对b进行__init__()
b.f2()

"""
查找属性顺序:
    1、对象本身；由于没有给对象定制__init__()方法，所以对象没有自己的属性，于是只能去对象所在的类中找
    2、对象所在的类；
    3、对象所在的类的父类去找。找到后先打印’from Foo.f2‘，之后调用了self.f1()，谁调用了self，谁就是self。
        只要是开始了属性查找，就继续按照对象-->所属类-->父类，这样的顺序进行查找。
        这里Bar.f1()，于是打印’from Bar.f1‘
"""