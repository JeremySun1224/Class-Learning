# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 20/1/8 -*-

"""
类的类型：
1、经典类，查找方式：深度优先
2、新式类，查找方式：广度优先

在Python2中，经典类指的是没有继承object的类，如class Hero:
            新式类指的是继承了object的类，如class Hero(object):

在Python3中，统一都是新式类



继承的实现原理：
    Python到底是如何实现继承的？对于定义的每一个类，Python会计算出一个方法解析顺序。
    这个MRO列表就是一个简单的所有基类的线性顺序列表。为了实现继承，Python会在MRO列表上从左到右开始查找基类，
    直到找到第一个匹配这个属性的类为止。MRO列表是通过C3算法实现的，实际上就是合并所有父类的MRO列表并遵循如下3条原则：
        1、子类会先于父类被检查；
        2、多个父类会根据它们在列表中的顺序被检查；
        3、如果对下一个类存在合法的选择，选择第一个父类。

    Python可以继承多个父类，那么属性的查找方式有两种，分别是：深度优先和广度优先。
"""

# class Foo():
#     pass
#
# print(Foo.__bases__)  # (<class 'object'>,)，默认继承了object类


# 验证多继承情况下的属性查找
class A(object):
    def test(self):
        print('from A')

class B(A):
    def test(self):
        print('from B')

class C(A):
    def test(self):
        print('from C')

class D(B):
    def test(self):
        print('from D')

class E(C):
    def test(self):
        print('from E')

class F(D, E):
    def test(self):
        print('from F')


f1 = F()
f1.test()  # 发现test是一个方法，那么就可以加()运行
# 查找顺序：F->D->B->E->C->A
print(F.mro())  # 新式类里，mro()方法可以直接查看查看方式

