# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 20/1/21 -*-

"""
封装包括数据属性的封装和函数属性的封装

1、封装数据属性意义：
    为了明确的区分内外，在外部不能访问，但在内部可以访问

2、封装方法的意义：
    可以隔离复杂度，让使用者不必接触到复杂的类内部情况
"""


# 封装数据属性
class People(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def tell_info(self):
        print('Name: <{name}> Age: <{age}>'.format(name=self.__name, age=self.__age))  # 在内部可以访问

    def set_info(self, name, age):
        if not isinstance(name, str):
            print('名字必须是字符串类型')
            return
        if not isinstance(age, int):
            print('年龄必须是数字类型')
            return
        self.__name = name
        self.__age = age


p = People(name='egon', age=10)
print(p._People__name)  # 只能间接访问
p.tell_info()
p.set_info(name='EGON', age=11)
print(p._People__name)
p.set_info(name=903, age=11)
print(p._People__name)

"""
取款是功能,而这个功能有很多功能组成:插卡、密码认证、输入金额、打印账单、取钱

对使用者来说,只需要知道取款这个功能即可,其余功能我们都可以隐藏起来,很明显这么做

隔离了复杂度,同时也提升了安全性
"""


# 封装函数属性
class ATM(object):
    def __card(self):
        print('插卡')

    def __auth(self):
        print('用户认证')

    def __input(self):
        print('输入取款金额')

    def __bill(self):
        print('打印账单')

    def __take(self):
        print('取款')

    def withdraw(self):
        self.__card()
        self.__auth()
        self.__input()
        self.__bill()
        self.__take()


a = ATM()

a.withdraw()
