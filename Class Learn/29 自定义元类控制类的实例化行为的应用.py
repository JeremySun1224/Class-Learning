# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 20/1/26 -*-


# 单例模式
# 实现方式1
class MySQL(object):
    __instance = None  # __instance=obj1

    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 3306

    @classmethod
    def singleton(cls):
        if not cls.__instance:
            obj = cls()
            cls.__instance = obj
        return cls.__instance

    def conn(self):
        pass

    def execute(self):
        pass


obj1 = MySQL()
obj2 = MySQL()
obj3 = MySQL()

print(obj1)  # <__main__.MySQL object at 0x0000013F8F43BA20>
print(obj2)  # <__main__.MySQL object at 0x0000013F8F43BAC8>
print(obj3)  # <__main__.MySQL object at 0x0000013F8F43BB00>

# 可以看出相同的对象却占据了不同的内存地址，这需要优化，我们需要用到的就是单例模式

obj4 = MySQL.singleton()
obj5 = MySQL.singleton()
obj6 = MySQL.singleton()

print(obj4)  # <__main__.MySQL object at 0x0000027C4673BC50>
print(obj5)  # <__main__.MySQL object at 0x0000027C4673BC50>
print(obj6)  # <__main__.MySQL object at 0x0000027C4673BC50>


# 可以看出此时对象的内存地址就相同了


# 实例方式2：元类的方式

class Mymeta(type):
    def __init__(self, class_name, class_bases, class_dic):
        if not class_name.istitle():  # istitle()首字母大写
            raise TypeError('类名的首字母必须大写')  # 主动抛出异常
        if '__doc__' not in class_dic or not class_dic['__doc__'].strip():
            raise TypeError('必须有注释，且注释不能为空')
        super(Mymeta, self).__init__(class_name, class_bases, class_dic)  # 在子类中重用父类的功能
        self.__instance = None

    def __call__(self, *args, **kwargs):
        if not self.__instance:
            obj = object.__new__(self)
            self.__init__(obj)  # 给类自动初始化，这里的self相当于Mysql
            self.__instance = obj
        return self.__instance


class Mysql(object, metaclass=Mymeta):
    """
    Mysql 类
    """

    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 3306

    def conn(self):
        pass

    def execute(self):
        pass


obj7 = Mysql()
obj8 = Mysql()
obj9 = Mysql()

print(obj7)  # <__main__.Mysql object at 0x0000024E8567BC88>
print(obj8)  # <__main__.Mysql object at 0x0000024E8567BC88>
print(obj9)  # <__main__.Mysql object at 0x0000024E8567BC88>


# 可以看出三个实例化对象的内存地址相同了
