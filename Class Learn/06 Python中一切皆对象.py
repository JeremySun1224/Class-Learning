# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 20/1/5 -*-

"""
补充说明：
    1、站在不同角度，定义出的类是截然不同的；
    2、现实中的类并不完全等于程序中的类。比如现实中的公司类，在程序中有时需要拆分成部门类，业务类等；
    3、有时为了编程需求，程序中也可能会定义现实中不存在的类。比如策略类，现实中并不存在，但是在程序中却是很常见的类。

Python中一切皆对象，并且在python3中统一了类与类型的概念。
    1、类型即数据类型，如列表，字典等
    2、一切皆对象的意思就是包括我们平时常用的list，dict都是类，我们在使用它们的时候都是先实例化的再使用的。
"""

print(type([1, 2, 3]))  # <class 'list'>，可以看出类型就是类——class
l1 = [1, 2, 3]
l1.append(4)  # 这里的append()就是我们的绑定方法。
print(l1)  # [1, 2, 3, 4]

l1 = [1, 2, 3]
list.append(l1, 4)  # 这就相当于我们对对象l1使用list类里的绑定方法append()，即把l1-->self。
print(l1)  # [1, 2, 3, 4]


# 先定义类
class LuffyStudent(object):
    # 相似的特征
    school = 'LuffyCity'

    def __init__(self, name, sex, age):  # 这里self, name, sex, age是位置参数(positional arguments)
        self.Name = name  # 即stu1.Name = '王二丫'，定制属性。
        self.Sex = sex  # 即stu1.Sex = '女'，定制属性。
        self.Age = age  # 即stu1.Age = 18，定制属性。

    # 相似的技能
    def learn(self):
        print('{Name} is learning'.format(Name=self.Name))

    def eat(self, food):
        print('{Name} is eating {Food}'.format(Name=self.Name, Food=food))

    def sleep(self):
        print('{Name} is sleeping'.format(Name=self.Name))

# print(LuffyStudent)  # <class '__main__.LuffyStudent'>

kone = LuffyStudent(name='kone', sex='male', age=18)
print(kone.eat(food='apple'))
print(list)  # <class 'list'>，可以看出list是一个类，那么类加括号就是一个实例化的过程。