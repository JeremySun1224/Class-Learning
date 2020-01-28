# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 20/1/23 -*-

# 将上一层文件夹的Mark Directory as 选为 Source Root即可调动自己写的模块
import settings
import hashlib
import time


class People(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.id = self.create_id()

    # 绑定到对象，就由对象来调用
    def tell_info(self):
        print('Name: {name} Age: {age} Sex: {sex}'.format(name=self.name, age=self.age, sex=self.sex))

    # 通过读取配置文件进行实例化。由于类名可能会改变，所以这里需要绑定类的方法
    @classmethod
    def from_conf(cls):
        obj = cls(
            name=settings.name,
            age=settings.age,
            sex=settings.sex
        )
        return obj

    # 该方法不依赖于类也不依赖对象，这就是一个普通的方法
    @staticmethod
    def create_id():
        md5 = hashlib.md5(str(time.time()).encode('utf-8')).hexdigest()  # 16进制格式hash
        # md5.update()
        return md5


p = People(name='egon', age=18, sex='male')
# 绑定给对象就应该由对象来调用，自动将对象本身当做第一参数传入
p.tell_info()  # tell_info(p)

# 绑定给类就应该由类来调用，自动将类本身当做第一参数传入
p1 = People.from_conf()  # from_conf(People)，这里是通过配置文件settings直接实例化出对象p
p1.tell_info()

# 非绑定方法，不与类或对象绑定，没有自动传值一说，谁都可以调用
p2 = People(name='egon2', age=18, sex='male')
p3 = People(name='hah', age=38, sex='female')
print(p2.id)
print(p2.__dict__)
print(p3.id)
print(p3.__dict__)
