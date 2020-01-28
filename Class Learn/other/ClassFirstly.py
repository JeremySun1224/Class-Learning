# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 19/12/9 -*-

# 引言
"""
记住一句话：类是模板，而实例则是根据类创建的对象。
以圆为例，圆具有圆周率和半径两个相似特征的属性。
于是我们可以根据相似特征抽取出圆类。
每个圆的半径可以不同，那么半径就可以作为圆的实例属性；
而每个圆的圆周率是相同的，那么圆周率可以作为类属性。
这样就定义出了一个圆类。
而我们要知道圆的面积、周长等可以通过类方法计算出来。
"""

# 类的定义与实例创建
"""
在Python中，类通过class关键字定义。类名的首字母通常为大写。
Python3中类基本都会继承于object类，当然也可以不继承object类，
两者区别不大。但没有继承object类使用多继承时可能会出现问题。
"""
# 创建Circle类，Circle为类名
class Circle(object):
    pass


"""
有了Circle类的定义，我们就可以创建出具体的circle1、circle2等实例。
circle1和circle2是两个实际的圆。创建实例使用类名+()的形式，类似函数调用的形式创建。
"""
# 创建两个Circle类的实例
circle1 = Circle()
circle2 = Circle()


"""
Python类中的实例属性和类属性
类属性是用来表明这个类是什么，分为实例属性和类属性
    实例属性用于区分不同的实例，每个实例各自拥有，相互独立；
    类属性是每个实例共有的属性，且类属性有且只能有一份。
    
1、实例属性
    类属性用来指明这个“类”是什么，实例属性是用来区分每个实例不同的基础。
    上面我们创建了两个Circle类。大家都知道所有圆都具备半径这个通用属性。
    下面我们为circle1和circle2实例添加半径r这个属性并赋值。
"""
# r为实例属性
circle1.r = 1
circle2.R = 2
# 使用“实例名.属性名”可以访问我们的属性
print(circle1.r)
print(circle2.R)
"""
如上circle1.r和circle2.R有大小写区分，两个实例的属性名称不统一不利于后面的访问和使用，
而且在每次创建圆后我们要再为实例添加属性就会比较麻烦，所以我们在创建实例时给类初始化属性。

在定义Circle类时，可以为Circle类添加一个特殊的__init__()方法。
当创建实例时，__init__()方法将自动给创建的实例添加实例属性。
"""
class Circle(object):
    # 初始化属性r，不要忘记self参数，它是类下面所有方法必须的参数
    def __init__(self, r):
        self.r = r  # 表示给我们将要创建的实例实例属性r赋值


"""
注意：__init__()方法的第一个参数必须是self(self代表类的实例，可以用别的名字，但建议使用约定俗成的self)。
    后续参数可以自由指定，和定义函数没什么区别。
拓展：__init__()方法的永达类似于Java中的构造方法，但它不是构造方法。Python中创建实例的方法是__new__()，
    这个方法在Python中大多数使用默认方法，不需要重新定义，初学者不用关注__new__()方法。
"""

# 相应的，创建实例时就必须提供出self以外的参数
circle1 = Circle(1)
circle2 = Circle(2)
# "实例名.属性名“访问属性
print(circle1.r)
print(circle2.r)


"""
注意：实例名.属性名 circle.r访问属性，是我们上面Circle类__init__()方法中的self.r中的r这个实例属性名称，
    而不是__init__(self, r)中的r参数名，如下更容易理解：
"""
class Circle(object):
    def __init__(self, R):  # 约定俗成这里应该使用r，它与self.r中的r同名
        self.r = R

circle1 = Circle(1)
print(circle1.r)  # 我们访问的是小写r

"""
面试时喜欢问的问题：创建类时，类方法中的self是什么？
self代表类的实例，是通过类创建的实例（注意，在定义类时这个实例我们还没有创建，
它表示我们使用类时创建的那个实例。
"""

"""
2、类属性
绑定在实例上的属性不会影响其他实例，但类本身也是一个对象。
如果在类上绑定属性，则所有实例都可以访问该类的属性，并且所有实例访问的类属性都是一个！
记住，实例属性每个实例各自拥有，相互独立，而类属性有且仅有一份。
"""
# 圆周率为圆的共有属性，我们可以在Circle类中添加圆周率这个类属性，如下：
class Circle(object):
    pi = 3.14  # 类属性

    def __init__(self, r):
        self.r = r

circle1 = Circle(1)
circle2 = Circle(2)

print('-----未修改前-----')
print('pi = \t', Circle.pi)  # 3.14
print('circle1.pi = \t', circle1.pi)  # 3.14
print('circle2.pi = \t', circle2.pi)  # 3.14

# 通过类名修改类属性，所有实例的类属性都会被改变
print('-----通过类名修改后-----')
Circle.pi = 3.14159
print('pi = \t', Circle.pi)
print('circle1.pi = \t', circle1.pi)  # 3.14159
print('circle2.pi = \t', circle2.pi)  # 3.14159

# 实际上这里是给circle1创建了一个与类属性同名的实例属性
print('-----通过circle1实例名修改后-----')
circle1.pi = 3.14111
print('pi = \t', Circle.pi)  # 3.14159
print('circle1.pi = \t', circle1.pi)  # 实例属性的访问优先级比类属性高，所以有3.14159变为3.14111
print('circle2.pi = \t', circle2.pi)  # 3.14159

"""
仔细观察我们通过类创建的实例修改的类属性后，通过其他实例访问类属性它的值还是没有改变。
其实是因为通过实例修改类属性时是给实例创建了一个与类属性同名的实例属性，
而实例属性访问优先级比类属性高，所以我们访问时优先访问实例属性，它将屏蔽掉对类属性的访问。
"""
# 我们删除circle1实例的属性pi，就能访问该类的类属性了
print('-----删除circle1实例属性pi-----')
del circle1.pi
print('pi = \t', Circle.pi)
print('circle1.pi = \t', circle1.pi)
print('circle2.pi = \t', circle2.pi)


"""
Python类的实例方法

方法是表明这个类是用来做什么的
在类的内部，我们使用def关键字来定义方法。
与一般函数的定义不同，类方法必须第一个参数为self，self代表的是类的实例（即使你还未创建类的实例），
其他参数和普通函数完全一样。
"""
class Circle(object):
    pi = 3.14  # 类属性，每个实例都首先具备了这个类属性。注意：实例属性优先于类属性

    def __init__(self, r):
        self.r = r  # 实例属性

    def get_area(self):  # get_area()为方法名
        '''圆的面积'''
        return self.r**2 * Circle.pi  # 通过实例修改pi的值对面积无影响，这里的pi为类属性
        # return self.r**2 * self.pi  # 通过实例修改pi的值对面积机会有影响

print('-----计算面积-----')
circle1 = Circle(2)  # 类的实例都具备类的特征
print(circle1.get_area())  # 调用方法：self不需要传入参数，不要忘记方法后的括号。输出为3.14


"""
注意：示例中的get_area(self)就是一个方法，它的第一个参数是self。__init__(self, name)其实也可以看做是一个特殊的实例方法。
在方法的内部需要调用实例属性采用’self.属性名‘的方法进行调用。示例中get_area(self)对于pi属性的引用Circle.pi与self.pi存在一定区别。
    Circle.pi使用的是类属性pi，我们通过创建的实例去修改pi的值对它无影响。
    self.pi为实例的pi值，我们通过创建的实例去修改pi的值时，由于使用self.pi调用的是实例属性，
    所以self.pi是修改后的值。
调用实例方法中的实例属性可采用’实例名.方法名(出self的参数)‘使用。
"""