# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 20/1/27 -*-


"""
异常就是程序运行时发生错误的信号（程序出现错误则会产生异常，若程序没有处理它则会抛出异常，程序的运行也会随之终止）
    错误分为两种：
        语法错误
        逻辑错误：
            ValueError
            NameError
            IndexError
            KeyError
            AttributeError
            ZeroDivisionError
            ......
"""

# 异常处理
# 强调1：对于错误发生的条件是可以预知的，此时应该用if判断去预防异常
AGE = 10
age = input('>>:').strip()
if age.isdigit():
    age = int(age)  # 如果输入的是非数字，则会报错，通过isdigit()进行判断
    if age > AGE:
        print('您猜大了')

# 强调2：对于错误发生的条件是不可预知的，此时应该用异常处理机制，try...except
try:  # try这里是监测的意思，监测try...except之间的代码
    f = open('a.txt', 'r', encoding='utf-8')
    print(next(f), end='')
    print(next(f), end='')
    print(next(f), end='')
    print(next(f), end='')
    print(next(f), end='')
    f.close()
except StopIteration:  # 一旦捕捉到某种异常，就会报错，只有当写对异常程序才能完全运行
    print('\n出错啦')

print('继续执行')