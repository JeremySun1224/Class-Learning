# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 20/1/18 -*-


"""
引子
从封装本身的意思去理解，封装就好像是拿来一个麻袋，把小猫，小狗，小王八，还有alex一起装进麻袋，
然后把麻袋封上口子。照这种逻辑看，封装=‘隐藏’，这种理解是相当片面的。

先看如何隐藏
在Python中用双下划线开头的方式将属性隐藏起来（设置成私有的）
"""


# Python中__去隐藏属性
# 其实这仅仅这是一种变形操作
# 类中所有双下划线开头的名称如__x都会自动变形成：_类名__x的形式
class A(object):
    __x = 1  # __表示隐藏，Python会自动改为_A__x

    def __init__(self, name):
        self.__name = name

    def __foo(self):  # Python会自动改为_A__foo
        print('run foo')

    def bar(self):
        self.__foo()  # 类定义阶段已经发生_A__foo()这种变形
        print('from bar')

print(A.__dict__)

a = A('Egon')
# print(a.__name)  # 这样已经访问不了__name这个属性

a.bar()  # 说明在类内部可以使用object.AttributeName去访问
# 那么我们怎么查看这个隐藏属性呢？
print(a.__dict__)  # {'_A__name': 'Egon'}

"""
实际上是一种变形操作，这种变形的特点：
    1、在类外部无法直接object.__AttributeName去访问
    2、在类内部可以通过object.__AttributeName去访问吗？可以。所以说这种变形并不会真的限制使用
    3、子类无法覆盖父类__开头的属性
So, Why？

"""

class Foo(object):
    def __func(self):  # 加__后实际上是：_Foo__func
        print('from foo')

class Bar(Foo):
    def __func(self):  # 加__后实际上是：_Bar__func
        print('from bar')

# 说明子类是无法覆盖父类的


"""
总结这种变形需要注意的问题：
    1、这种隐藏并不是真正意义的隐藏
    2、这种变形是在类定义阶段就定义的属性，在类定义之后就不会再变形，所以说要隐藏，我们需要在类定义阶段就隐藏属性。
    3、
"""


class B(object):
    __x = 1

    def __init__(self, name):
        self.__name = name

# 验证问题1
print(B._B__x)

# 验证问题2
B.__y = 2
print(B.__dict__)

# 验证问题3
# class A(object):
#     def foo(self):
#         print('A.foo')
#
#     def bar(self):
#         print('A.bar')
#         self.foo()  # 这里的self.foo()实际上就是b.foo()
#
#
# class B(A):
#     def foo(self):
#         print('B.foo')
#
# b = B()
# b.bar()
# 打印结果为：
# A.bar
# B.foo

# 作为对比
# 那如果就是想用A里的foo()呢？那么我们就需要在foo()前加__
class A(object):
    def __foo(self):  # _A__foo
        print('A.foo')

    def bar(self):
        print('A.bar')
        self.__foo()  # self._A__foo()


class B(A):
    def __foo(self):  # _B__foo
        print('B.foo')

b = B()
b.bar()
# 打印结果为：
# A.bar
# B.foo

"""
于是__可以实现只到自己的类里去调函数，不到别的类里去找
"""