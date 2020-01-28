# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 20/1/9 -*-

from abc import ABCMeta, abstractmethod


# 把多个类抽取它们相似的部分得到一个父类，然后让子类继承父类，并让子类在继承父类的时候都必须实现父类规定的方法，这需要借助abc模块
# 抽象类的功能只是用来规范子类，所以只能用来继承，但是不能实例化
# 定义抽象类Animal
class Animal(metaclass=ABCMeta):
    def __init__(self, name):  # __init__方法前不需要加：@abc.abstractmethod
        self.name = name

    @abstractmethod
    def run(self):  # 只定义方法不定义功能
        pass

    @abstractmethod
    def eat(self):
        pass


class People(Animal):
    def run(self):
        print('{name} is working'.format(name=self.name))

    def eat(self):
        print('{name} is eating'.format(name=self.name))


class Pig(Animal):
    def run(self):
        print('{name} is moving'.format(name=self.name))

    def eat(self):
        print('{name} is eating'.format(name=self.name))


class Dog(Animal):
    def run(self):
        print('{name} is running'.format(name=self.name))

    def eat(self):
        print('{name} is eating'.format(name=self.name))


people = People(name='egon')
pig = Pig(name='Peiqi')
dog = Dog(name='Heipi')

people.run()
pig.run()
dog.run()


# 可以看出上述三个对象都有“走”这个技能，但是该功能名字不一样，即调用方法名不一样
# 所以现在我们希望找一个解决方案，统一这些名字，方便使用者使用
