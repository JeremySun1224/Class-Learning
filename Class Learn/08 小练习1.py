# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 20/1/8 -*-

"""
练习1：编写一个学生类，产生一堆学生对象，
要求：有一个计数器（属性），统计总共实例了多少个对象。（调用类会触发__init__()方法，可以用这个进行实例化）
"""

class Student(object):
    # 公有的特征
    school = 'LuffyCity'  # 定义一个变量则称之为类的数据属性，它是所有对象共有的属性
    count = 0
    # 定制独有的特征
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        # self.count = count
        # count += 1  # 如果__init__()里没有定义count，那么它会到上一层找，在数据属性里有count
        Student.count += 1  # __init__()自己的名称空间里没有count属性，它会去类的属性里寻找

    def learn(self):  # 定义一个函数称之为类的函数属性，self就是当某个对象调用该方法的时候自动将对象名传参给self，这个self可以随便改，但是吧这是约定俗成的
        print('{name} is learning'.format(name=self.name))

p1 = Student(name='egon', age=38, sex='male')
p2 = Student(name='alex', age=38, sex='female')
p3 = Student(name='kim', age=38, sex='male')

print(Student.count)
print(Student.__dict__)
print(p1.count)
print(p1.__dict__)
print(p2.count)
print(p2.__dict__)
print(p3.count)
print(p3.__dict__)

"""
print(p1.count)  # p1.count()报错not callable，去掉()
print(p2.count)
print(p3.count)

加都为0，也就是说我们不能在对象的属性里进行加减，而是要从整个类出发，改类的属性才行
"""
