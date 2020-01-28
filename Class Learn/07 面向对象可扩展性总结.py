# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 20/1/5 -*-

# 从代码级别看面向对象

# 可扩展性高

class Chinese(object):
    # 假设现在要扩展一个属性country
    country = 'China'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    # 假设现在要扩展一个功能
    def eat(self, food):
        self.food = food
        return print('{name} is eating {food}'.format(name=self.name, food=self.food))


# 实例化
p1 = Chinese(name='egon', age=38, sex='male')
p2 = Chinese(name='alex', age=38, sex='female')
p3 = Chinese(name='kim', age=38, sex='male')
# p1.country = 'China'

print(p1.country)
print(p1.eat('apple'))
print(p2.eat('orange'))
print(p3.eat('banana'))