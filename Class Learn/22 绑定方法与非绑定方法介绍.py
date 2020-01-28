# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 20/1/21 -*-

"""
在类内部定义的函数，分为两大类：
    1、绑定方法
        绑定到对象的方法：
            在类内部定义的没有被任何装饰器修饰
            绑定给谁就应该由谁来调用，谁来调用就会把调用者当做第一个参数自动传入

        绑定到类的方法：
            在类内部定义的被装饰器@classmethod修饰方法
            绑定给谁就由谁来调用

    2、非绑定方法：
        不与类或者对象绑定，谁都可以使用，它就是一个普通的函数。
        它没有自动传值这么一说，利用装饰器@staticmethod进行装饰，此时该方法既不是函数属性也不是类属性
"""


class Foo(object):
    def __init__(self, name):
        self.name = name

    def tell(self):
        print('名字是{name}'.format(name=self.name))

    @classmethod
    def func(cls):  # cls表示现在默认自动传的参数是类本身
        print(cls)

    @staticmethod
    def func1(x, y):
        return print(x + y)


f = Foo(name='egon')


# 定义一个普通函数作为对比
def function():
    pass


# 绑定到对象
print(Foo.tell)  # <function Foo.tell at 0x00000133172B8D90>，说明类访问自己的函数时就是普通函数，于是也就没有自动传参等说法
print(f.tell)  # <bound method Foo.tell of <__main__.Foo object at 0x000001CF1EF2C710>>
print(function)  # <function func at 0x0000017449BF7F28>

# 绑定到类，这里实际上是func(cls=Foo)
print(Foo.func)  # <bound method Foo.func of <class '__main__.Foo'>>

# 非绑定方法
print(Foo.func1)
print(f.func1)
Foo.func1(x=1, y=2)
f.func1(x=1, y=2)
