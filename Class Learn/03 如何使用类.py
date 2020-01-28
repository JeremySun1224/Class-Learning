# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 19/12/21 -*-

"""
类和函数的区别：
    类在定义阶段内部的代码就会执行，而函数只有在调用阶段才运行。
    一旦执行函数就会产生名称空间。
"""
# 先定义类
class LuffyStudent(object):
    # 相似的特征
    school = 'LuffyCity'  # 数据属性

    # 相似的技能
    def learn(self):  # 函数属性
        print('is learning')

    def eat(self):  # 函数属性
        print('is eating')

    def sleep(self):  # 函数属性
        print('is sleeping')

# 查看类的名称空间
print(LuffyStudent.__dict__)
# 访问变量school的值，也就是访问类的数据属性
print(LuffyStudent.__dict__['school'])
# 访问类的函数属性
print(LuffyStudent.__dict__['learn'])

# 针对属性，Python提供了专门的访问属性的语法
# 由于我们在使用一些模块的属性时并不用__dict__去访问，而是直接用.，这里我们也可以直接用点访问类的属性
# 查看或者说访问
print(LuffyStudent.school)  # 效果等同于print(LuffyStudent.__dict__['school'])
print(LuffyStudent.learn)  # 效果等同于print(LuffyStudent.__dict__['learn'])

# 增，比如增加属性
LuffyStudent.country = 'China'  # 增加属性
print(LuffyStudent.__dict__)

# 删
del LuffyStudent.country
print(LuffyStudent.__dict__)

# 改
LuffyStudent.school = 'Luffycity'
print(LuffyStudent.__dict__)
