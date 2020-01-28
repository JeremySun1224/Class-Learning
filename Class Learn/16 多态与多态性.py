# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 20/1/9 -*-


from abc import ABCMeta, abstractmethod

# 多态是指同一种事物的多种形态，比如动物有多种形态：人、狗和猪等
class Animal(metaclass=ABCMeta):  # 抽象类
    def __init__(self, name):  # __init__方法前不需要加：@abc.abstractmethod
        self.name = name

    @abstractmethod
    def talk(self):  # 只定义方法不定义功能，功能由具体的对象重新定制
        pass


class People(Animal):
    def talk(self):
        print('{name} say hello'.format(name=self.name))


class Pig(Animal):
    def talk(self):
        print('{name} say aoao'.format(name=self.name))


class Dog(Animal):
    def talk(self):
        print('{name} say wangwang'.format(name=self.name))


class Cat(Animal):
    def talk(self):
        print('{name} say miaomiao'.format(name=self.name))

# 多态性
# 多态性是指在不考虑对象类型的情况下使用对象，多态性分为静态多态性和动态多态性
# 静态多态性：如任何类型都可以用运算符+进行运算，我们在应用静态多态性的时候就是不用考虑具体要加减的类型，直接加减

people = People(name='Egon')
pig = Pig(name='Peiqi')
dog = Dog(name='Heipi')
cat = Cat(name='Coffe')

# 动态多态性
# 可以看出，这里我们并没有考虑它是动物里的人，动物里的猪还是动物里的狗，我们都把它当做动物看，是动物具有talk()这个技能，我们直接用就行。
# people.talk()
# pig.talk()
# dog.talk()

def func(animal):  # 只要是animal就一定有talk()这个功能，在增加了Cat这个类的时候，使用者并不用改这段代码就能统一给cat分配功能
    animal.talk()


func(people)  # 所以我们只要传入的是animal，而且这个animal有talk()这个功能就行，比如People类等
func(pig)
func(dog)
func(cat)  # 在定义新的类的时候，不需要对接口func()进行改动，直接就可以实例化对象cat



"""
多态性的好处(需要建立在同一种事物的多种形态上)：
    1、增加程序的灵活性。Python本身就是指出多态性的。以不变应万变，不论对象怎么变，使用者都是用同一种形式去调用，如func(animal)
    2、增加程序的课拓展性。通过继承Animal类创建了一个新的类，使用者无需更改自己的代码，还是用func(animal)去调用
"""


