# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 19/12/21 -*-

"""
每个对象还有自己独有的特征，比如名字等，也就是说个性化定制。

__init__方法用来为对象定制对象自己独有的特征。

值得注意的是：凡是在类内部以双下划线定义的函数都有自己独特的意思
"""
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
        print('is learning')

    def eat(self):
        print('is eating')

    def sleep(self):
        print('is sleeping')

# 后产生对象
# 报错：missing 3 required positional arguments。修改：传入位置参数
# 调用类（这里我们并没有调用__init__()，但是Python会自动调用，于是我们需要给类传入另外的位置参数。其实__init__是一种初始化。
# stu1 = LuffyCity()，没有__init__()的时候调用类会实例化出一个普通的对象，没有个性化定制。
# 加入__init__()方法后，我们可以通过传入位置参数的方法实例化出独特的对象，这就是使用__init__()方法的原因。
stu1 = LuffyStudent(name='王二丫', sex='女', age='18')
print(stu1)


"""
有__init__()方法后实例化步骤：
1、先产生一个对象，但是这个对象没有自己独有的属性，即这是一个空对象stu1
2、触发LuffyStudent.__init__()这一函数属性，由于__init__()也是一个普通的函数，那么就得按照参数的规矩传入参数。
实际上当我们调用完__init__()方法后会造出一个空对象stu1，并把这个空对象传给参数self，即stu1-->self，
联合name, sex, age组成4个参数一起传给__init__()，即stu1, name, sex, age --> self, Name, Sex, Age。
由此产生LuffyStudent.__init__(stu1, '王二丫', '女', 18)这一实例化对象。
"""
print(LuffyStudent.__init__)  # <function LuffyStudent.__init__ at 0x000001600E078D08>

# 查
# stu1.Name = '王二丫'给对象stu1设置属性，就会涉及到名称空间，那么我们可以用__dict__查看
print(stu1.__dict__)  # {'Age': '18', 'Sex': '女', 'Name': '王二丫'}于是stu1有了独立特征
print(stu1.Name)  # 直接访问对象的属性

# 改
stu1.Name = '李二丫'
print(stu1.Name)

# 删
del stu1.Name
print(stu1.__dict__)

# 增
stu1.class_name = 'Python开发'
print(stu1.__dict__)
print(stu1.class_name)


# 再实例化一个对象stu2
stu2 = LuffyStudent(name='李三炮', sex='男', age='38')
print(stu2.__dict__)
print(stu2.Name)
print(stu2.Sex)
print(stu2.Age)