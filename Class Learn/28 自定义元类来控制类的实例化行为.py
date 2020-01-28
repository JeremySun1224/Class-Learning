# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 20/1/26 -*-


# 知识储备：__call__()方法
class Foo(object):
    def __call__(self, *args, **kwargs):  # *args和**kwargs均是非固定参数，其中args是元组，kwargs是字典
        print(self)
        print(args)
        print(kwargs)


obj = Foo()
# 默认情况下实例化后的对象是不可调用的，但一切皆对象的道理来说obj应该通过某种手段也能调用，这种手段就是__call__()
obj(1, 2, 3, a=1, b=2, c=3)  # 这里相当于self=obj, args=(1,2,3), kwargs={'a'=1, 'b'=2, 'c'=3}

"""
元类内部也应该有一个__call__()方法，会在调用Foo时触发执行。
即Foo(1, 2, x=1)，即Foo.__call__(Foo, 1, 2, x=1)
"""


class Mymeta(type):
    def __init__(self, class_name, class_bases, class_dic):
        if not class_name.istitle():  # istitle()首字母大写
            raise TypeError('类名的首字母必须大写')  # 主动抛出异常
        if '__doc__' not in class_dic or not class_dic['__doc__'].strip():
            raise TypeError('必须有注释，且注释不能为空')
        super(Mymeta, self).__init__(class_name, class_bases, class_dic)  # 在子类中重用父类的功能

    def __call__(self, *args, **kwargs):
        print(self)  # self=Chinese
        print(args)  # args=元组()
        print(kwargs)  # kwargs=字典{'age': 19, 'name': 'egon'}
        """
        类实例化的行为包括三步：
            1、先造一个空对象obj
            2、初始化obj
            3、返回obj
        """
        # 造空对象obj
        obj = object.__new__(self)  # self=Chinese
        # 初始化
        self.__init__(obj, *args, **kwargs)
        # 返回obj
        return obj


class Chinese(object, metaclass=Mymeta):
    """
    注释（在类的名称空间__doc__中）
    """
    country = 'China'  # 每一个中国人都有国籍

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print('{name} is talking'.format(name=self.name))


obj = Chinese(name='egon', age=19)  # Chinese.__call__(Chinese, 'egon', 19)
print(obj.__dict__)