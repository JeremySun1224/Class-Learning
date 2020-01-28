# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 20/1/21 -*-

class Room(object):
    def __init__(self, name, owner, weight, length):
        self.name = name
        self.owner = owner

        self.__weight = weight
        self.__length = length

    def tell_area(self):
        area = self.__weight * self.__length
        return '{owner}的{name}面积是：{area}平米'.format(owner=self.owner, name=self.name, area=area)


r = Room(name='卫生间', owner='Alex', weight=10, length=10)

# 对于使用者来说，只需要记住这一行代码，具体的面积怎么算，或者是增加体积，这些都不用使用者担心，一定程度上提高了程序的可扩展性
print(r.tell_area())