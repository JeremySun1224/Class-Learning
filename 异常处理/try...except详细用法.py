# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 20/1/27 -*-


"""
使用异常处理的情况：
    1、异常发生的错误异常能明确预知
    2、只有知道错误一定会发生，而且难以避免，可是我又不希望程序因为这个错误就停止，才可以考虑使用Exception
"""

"""
多分支：被检测的代码块抛出的异常有多种可能性，
并且我们需要针对每一种异常类型都定制专门的处理逻辑
"""

try:
    print('===>')
    # name
    print('===>')
    l = [1, 2, 3]
    # l[100]
    print('===>')
    d = {}
    d['name']
    print('===>')

except NameError as e:  # 这里相当于把这个异常记为e，方便详细打印
    print('Error: {error}'.format(error=e))

except IndexError as e:
    print('Error: {error}'.format(error=e))

except KeyError as e:
    print('Error: {error}'.format(error=e))

"""
万能异常：Exception，被检测的代码块抛出的异常有多种可能性，
并且针对所有的异常类型都只用有种处理逻辑就可以，即使用Exception
"""

try:
    print('===>')
    # name
    print('===>')
    l = [1, 2, 3]
    # l[100]
    print('===>')
    d = {}
    d['name']
    print('===>')

except NameError as e:  # 这里相当于把这个异常记为e，方便详细打印
    print('Error: {error}'.format(error=e))

except IndexError as e:
    print('Error: {error}'.format(error=e))

except KeyError as e:
    print('Error: {error}'.format(error=e))

except Exception as e:
    print('统一异常抛出处理', e)

else:  # 不太常用
    print('在被监测的代码块没有发生异常时执行')

finally:
    print('不管被监测的代码块有无发生异常都会执行')

print('after code')

# finally通常在回收资源的时候使用
try:
    f = open(file='a.txt', mode='r', encoding='utf-8')
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))  # 抛出异常

except Exception as e:
    pass

finally:
    f.close()  # 不论出错与否都要回收资源

"""
主动触发异常：raise 异常类型(值)
"""


class People(object):
    def __init__(self, name, age):
        if not isinstance(name, str):
            raise TypeError('名字必须是str类型')
        if not isinstance(age, int):
            raise TypeError('年龄必须是int类型')
        self.name = name
        self.age = age


# 如果用户就要传入整型作为name，我们现在就要限制用户这么做，则用到raise
People(name='egon', age=18)

"""
自定义异常类型
"""


class MyException(BaseException):  # 虽是自定义异常，但仍需继承BaseException
    def __init__(self, msg):
        super(MyException, self).__init__()  # 继承父类的__init__()方法
        self.msg = msg

    def __str__(self):
        return '<{mag}>'.format(mag=self.msg)  # 一定要return一个字符串类型


raise MyException('我自己的异常类型')  # print(obj)


"""
断言：assert
    假设我们的程序是明确分为两大部分：
        部分1：通过执行...执行输出一个明确的结果
        部分2：部分2是要依赖部分1的结果才能执行
"""

info = {}
info['name'] = 'egon'
info['age'] = 18

# if 'name' not in info:  # 断定这个name应该在info
#     raise KeyError('必须有name这个key')
#
# if 'age' not in info:
#     raise KeyError('必须有age这个key')

# 使用断言assert可以减少上述两个if

assert ('name' in info) and ('age' in info)  # 如果断言失败就抛出异常，可以看出减少了代码量

if info['name'] == 'egon' and info['age'] > 10:
    print('Welcome')
