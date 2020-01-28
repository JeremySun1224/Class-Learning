# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 20/1/18 -*-


"""
鸭子类型：不继承类但是可以造一个和类相似的

Python中崇尚鸭子类型，即‘如果看起来像、叫声像而且走起路来像鸭子，那么它就是鸭子’;
Python程序员通常根据这种行为来编写程序。例如，如果想编写现有对象的自定义版本，可以继承该对象;
也可以创建一个外观和行为像，但与它无任何关系的全新对象，后者通常用于保存程序组件的松耦合度。
"""


class File(object):
    def read(self):
        pass

    def write(self):
        pass


# 可以说现在Disk看起来像File类，不用继承File类
class Disk(object):
    def read(self):
        print('Disk read')

    def write(self):
        print('Disk write')


# 可以说现在Text看起来像File类，不用继承File类
class Text(object):
    def read(self):
        print('Text read')

    def write(self):
        print('Text write')


# 实例化对象
disk = Disk()
text = Text()

disk.read()
disk.write()

text.read()
text.write()

"""
序列类型：
列表list，元祖tuple，字符串str
这三个之间没有直接的继承关系，由于它们都是序列类型，那么就都有雨__len__()
"""
l = list([1, 2, 3])
t = tuple(('a', 'b'))
s = str('hello')

# 这里就使用了鸭子类型。对于列表，元祖和字符串三个类，并没有考虑具体的类型，只要是序列类型，我们都可以使用__len__()，这样就方便了使用者
print(l.__len__())
print(t.__len__())
print(s.__len__())


# 由于Python中独特的继承，我们可以直接写成
print(len(l))
print(len(t))
print(len(s))


