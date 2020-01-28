# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 20/1/25 -*-


# item系列，把对象模拟成字典进行增删改查
class Foo(object):
    def __init__(self, name):
        self.name = name

    def __getitem__(self, item):
        return self.__dict__.get(item)

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __delitem__(self, key):
        del self.__dict__[key]


obj = Foo(name='egon')
# 查看属性
print(obj.__dict__)
print(obj['name'])
print(obj['hah'])

# 设置属性
# obj.sex = 'male'
obj['sex'] = 'male'
print(obj.__dict__)
print(obj.sex)

# 删除属性
# del obj.name
del obj['name']
print(obj.__dict__)


# __str__方法会把对象转成字符串输出
class People(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 如何返回有用信息
    def __str__(self):
        print('===>str')
        return '<name: {name}, age: {age}>'.format(name=self.name, age=self.age)


obj = People(name='egon', age=18)
# 这样打印的结果有用信息并不多
print(obj)  # <__main__.People object at 0x000001C35D506C88>


# del 回收操作系统打开的文件
class Open(object):
    def __init__(self, filename):
        print('open file ...')
        self.filename = filename

    def __del__(self):
        print('回收操作系统资源：self.close')


f = Open(filename='settings,py')
print('-----main-----')

"""
打印结果：
    open file ...
    -----main-----
    del...
"""