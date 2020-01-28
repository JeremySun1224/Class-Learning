# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 20/1/24 -*-

"""
通过字符串访问到对象的属性
"""


class People(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print('{name} is talking'.format(name=self.name))


p = People(name='egon', age=18)
# 访问属性
print(p.name)
print(p.talk)
# 通过字符串映射到对象的属性，判断字典里面有没有属性name，有为True
print(hasattr(p, 'name'))  # 查看p.name，本质上是p.__dict__['name']
# 拿到对象属性
print(getattr(p, 'name'))  # None表示如果没有这个属性不会报错
print(getattr(p, 'sex', None))  # 如果没有这个属性就返回None
# 修改属性
setattr(p, 'sex', 'male') # p.sex='male'
print(p.sex)
# 删除
print(p.__dict__)  # {'name': 'egon', 'age': 18, 'sex': 'male'}
delattr(p, 'age')  # del p.age
print(p.__dict__)  # {'name': 'egon', 'sex': 'male'}

# 对类同样适用
print(getattr(People, 'country', None))


# 反射的应用
class Service(object):
    def run(self):
        while True:
            cmd = input('>>: '.strip())  # cmd = 'get a.txt'
            cmds = cmd.split()
            if hasattr(self, cmds[0]):
                func = getattr(self, cmds[0])  # 这里的getattr拿到是绑定党发
                func(cmds)  # 加括号调用

    def get(self, cmds):
        print('get ...', cmds)

    def put(self, cmds):
        print('put ...', cmds)


obj = Service()
obj.run()