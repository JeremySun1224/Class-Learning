# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 20/1/4 -*-

# 先定义类
class LuffyStudent(object):
    # 相似的特征
    school = 'LuffyCity'

    def __init__(self, name, sex, age):  # 这里self, name, sex, age是位置参数(positional arguments)
        self.Name = name  # 即stu1.Name = '王二丫'，定制属性。
        self.Sex = sex  # 即stu1.Sex = '女'，定制属性。
        self.Age = age  # 即stu1.Age = 18，定制属性。

    # 相似的技能
    def learn(self):
        print('{Name} is learning'.format(Name=self.Name))

    def eat(self, food):
        print('{Name} is eating {Food}'.format(Name=self.Name, Food=food))

    def sleep(self):
        print('{Name} is sleeping'.format(Name=self.Name))


stu1 = LuffyStudent(name='王二丫', sex='女', age='18')
stu2 = LuffyStudent(name='李三炮', sex='男', age='38')
stu3 = LuffyStudent(name='张铁蛋', sex='男', age='48')

# 查看类给对象定制的私有特征
print(stu1.__dict__)
print(stu2.__dict__)
print(stu3.__dict__)

# 对象：特征与技能的结合体
# 定义对象相似的技能

# 类：类是一系列对象相似的特征与相似的技能的结合体
# 类中的数据属性：是所有对象共有的
print(LuffyStudent.school, id(LuffyStudent.school))
print(stu1.school, id(stu1.school))
print(stu2.school, id(stu2.school))
print(stu3.school, id(stu3.school))
# 可以看出id也是相同的，说明类中的数据属性是类中的对象所公有的

# 类中的函数属性：是绑定给对象使用的，绑定到不同的对象是不同的绑定方法。对象在调用绑定方法时，会把对象名自动传给第一个参数self，其余的参数仍需手动传
print(LuffyStudent.learn)  # <function LuffyStudent.learn at 0x000001DC10795268>表明类在调用自己函数属性时就是普通的函数。
# LuffyStudent.learn()  # TypeError: learn() missing 1 required positional argument: 'self'
LuffyStudent.learn(stu1)
print(stu1.learn)  # bound method LuffyStudent.learn of <__main__.LuffyStudent object at 0x00000219FCAA29E8>>
print(stu2.learn)  # bound method LuffyStudent.learn of <__main__.LuffyStudent object at 0x00000219FCAA2A58>>
print(stu3.learn)  # bound method LuffyStudent.learn of <__main__.LuffyStudent object at 0x00000219FCAA2A90>>
# 可以看出同一技能在绑定给不同对象的时候所对应的内存地址是不同的，但仍是同一个功能。
stu1.learn()  # 触发的是stu1下面的learn()技能，stu1是王二丫。对象调用learn()方法却不用传入参数，这意味着肯定有自动传，即learn(stu1)
stu1.eat(food='apple')  # 这里的参数传递就相当于是eat(self=stu1, food='apple')


"""
总结：
    1、何为bound method？
    我们给不同对象绑定同一技能，当一起调用时，不同对象执行的是不同方法。比如，A绑定了learn()，B绑定了learn()，那么A在执行leaen()技能的时候，
    A learn()到的东西不会给了B，互不影响。
    
    2、类中定义的函数属性实际上是给实例化出的对象使用的。因为类要想直接调用函数属性的话还得传参数，而对象在调用类的时候会自动传参。哪个对象调用
    函数属性就把哪个对象名当做第一参数传入，即对象名-->self。
    
    3、如果类有一个函数属性x，对象也有一个函数属性x，那么在对象调用这个函数属性的时候实际上触发的是对象的那个函数属性x。这与名称空间的概念类似，
    访问时先访问局部的，再访问全局的。如果对象中没有这个属性，函数会在类中找，如果类中也没有的话，会去父类中找，如果一直没有，就报错，不会到全局去找。
"""

stu1.place = 'place from stu1'
LuffyStudent.place = 'place from LuffyCity class'

print(stu1.__dict__)
print(stu1.place)
