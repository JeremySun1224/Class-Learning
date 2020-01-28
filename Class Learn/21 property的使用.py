# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 20/1/21 -*-

import math

"""
特性(property)

什么是特性property

property是一种特殊的属性，访问它时会执行一段功能（函数）然后返回值

例1：BMI指数（bmi是计算而来的，但很明显它听起来像是一个属性而非方法，如果我们将其做成一个属性，更便于理解）

成人的BMI数值：

过轻：低于18.5

正常：18.5-23.9

过重：24-27

肥胖：28-32

非常肥胖, 高于32

体质指数（BMI）=体重（kg）÷身高^2（m）

EX：70kg÷（1.75×1.75）=22.86
"""


class People(object):
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height

    @property  # 使用property方法必须有返回值作为其结果
    def bmi(self):
        return self.weight / self.height ** 2


p = People(name='egon', weight=75, height=1.81)
# p.bmi = p.weight / (p.height ** 2)
# print(p.bmi)
# 按照上述方法每次计算BMI都要手动计算一下，所以我们可以定义一下这个功能，则可以如下修改
# print(p.bmi())  # 只能p.bmi()这么调，不能像p.bmi这么调。那怎么改呢？只要在前面加property装饰器
print(p.bmi)
p.height = 1.9
print(p.bmi)


# 例2
class People1(object):
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


p1 = People1(name='egon')
print(p1.get_name())


# 我现在只想正常的访问p1.name就能得到name，不想用get_name()，我们就可以使用property装饰器


class People2(object):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name


p2 = People2(name='egon')
print(p2.name)


# 例3

class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius


c = Circle(radius=10)
# 返回面积
print(c.area)
# 返回周长
print(c.perimeter)
