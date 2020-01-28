# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 20/1/8 -*-


"""
指定选课系统
"""


# 人类
class People(object):
    school = 'LuffyCity'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


# 教师类
class Teacher(People):
    def __init__(self, name, age, sex, level, salary):
        super(Teacher, self).__init__(name, age, sex)
        self.level = level
        self.salary = salary

    def teach(self):
        print('{name} is teaching'.format(name=self.name))


# 学生类
class Student(People):
    def __init__(self, name, age, sex, class_time):
        super(Student, self).__init__(name, age, sex)
        self.level = class_time

    def learn(self):
        print('{name} is learning'.format(name=self.name))


# 课程类
class Course(object):
    def __init__(self, name, price, period):
        self.name = name
        self.price = price
        self.period = period

    def tell_info(self):
        print('课程名{name} 课程价钱{price} 课程周期{period}'.format(name=self.name, price=self.price, period=self.period))


class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def tell_info(self):
        print('{year}-{month}-{day}'.format(year=self.year, month=self.month, day=self.day))


teacher = Teacher(name='alex', age=18, sex='male', level=10, salary=3000)
student = Student(name='egon', age=18, sex='female', class_time='08:30:00')
python = Course(name='python', price=3000, period='3月')
linux = Course(name='linux', price=2000, period='3月')
date = Date(year=1988, month=5, day=3)

"""
老师要教课，学生要学课，于是想到了类的继承
继承必须是类之间存在从属关系，即什么是什么的关系
可以抽象为老师有课程，学生有课程，于是可以给老师/学生增加一个课程属性
对象是可以进行赋值操作的
"""

# 用对象给老师增加一个课程属性
teacher.course = python
student.course = linux
print(teacher.__dict__)
print(python.name)
print(teacher.course.name)  # 实际上teacher.course的course属性指向的是course对象
teacher.course.tell_info()
student.course.tell_info()
student.birth = date
student.birth.tell_info()

# 这些都是通过组合的方式实现的，并不是继承，同样可以实现代码重用。
# 组合即什么有什么
