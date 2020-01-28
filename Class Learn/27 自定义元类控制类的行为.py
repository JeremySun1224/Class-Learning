# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 20/1/26 -*-


# 自定义元类仍可以继承type类
class Mymeta(type):
    # 重写的这个__init__()会覆盖了父类的__init__，所以是需要用到super()
    def __init__(self, class_name, class_bases, class_dic):
        if not class_name.istitle():  # istitle()首字母大写
            raise TypeError('类名的首字母必须大写')  # 主动抛出异常
        # print(class_name)
        # print(class_bases)
        print(class_dic)
        if '__doc__' not in class_dic or not class_dic['__doc__'].strip():
            raise TypeError('必须有注释，且注释不能为空')
        super(Mymeta, self).__init__(class_name, class_bases, class_dic)  # 在子类中重用父类的功能


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

print(Chinese.__dict__)