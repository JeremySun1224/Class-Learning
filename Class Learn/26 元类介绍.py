# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 20/1/25 -*-


"""
储备知识exec
参数1：字符串形式的命令
参数2：全局作用域（字典形式），如果不指定，默认使用globals()
参数3：局部作用域（字典形式），如果不指定，默认使用locals()
"""

g = {
    'x': 1,
    'y': 2
}

l = {}

exec("""
global x, m
x = 10
m = 100

z = 3
""", g, l)
print(g)
print(l)

"""
一切皆对象，对象可以怎么用？
    1、都可以被引用，x=obj；
    2、都可以当做函数的参数传入；
    3、都可以当做函数的返回值；
    4、都可以当做容器类(列表、元组等)的元素。

类也是对象，Foo = type(...)
"""


class Foo(object):
    pass


class Bar(object):
    pass


obj = Foo()
print(type(obj))  # <class '__main__.Foo'>
print(type(Foo))  # <class 'type'>
print(type(Bar))  # <class 'type'>
# 可见其元类都是type

"""
元类：产生类的类就是元类。
     默认用class定义的类，它们的元类都是type
"""


# 定义类的两种方式：
# 方式1：class。实际上是class这个类调用了type这个元类产生类，即Chinese=type(...)

class Chinese(object):
    country = 'China'  # 每一个中国人都有国籍

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print('{name} is talking'.format(name=self.name))


# 方式2：type
# 定义类的三要素：类的名字；类的基类；类的名称空间
class_name = 'Chinese'
class_bases = (object,)
class_body = """
country = 'China'  # 每一个中国人都有国籍

def __init__(self, name, age):
    self.name = name
    self.age = age

def talk(self):
    print('{name} is talking'.format(name=self.name))
"""
class_dic = {}  # 初始状态
exec(class_body, globals(), class_dic)
print(class_dic)
# 造类
China = type(class_name, class_bases, class_dic)
print(Chinese)
print(China)
