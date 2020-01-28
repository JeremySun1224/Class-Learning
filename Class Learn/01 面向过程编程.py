# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 19/12/21 -*-

"""
面向过程编程：
核心二字就是过程。过程指的是解决问题的步骤，即设计一条流水线，机械式的思维方式。

优点：
把复杂的问题流程化，进而简单化。

缺点：
扩展性不好，扩展一个函数后之后相关的函数都得改，很繁琐。

由此引出面向对象
"""

# 用户注册流程
# 现在添加邮箱
import json
import re

def interactive():
    name = input('name>>: ').strip()
    pwd = input('passward>>: ').strip()
    email = input('email>>: ').strip()
    user_info = {
        'name': name,
        'pwd': pwd,
        'email': email
    }
    return user_info

def check(user_info):
    is_valid = True

    if len(user_info['name']) == 0:
        print('用户名不能为空')
        is_valid = False

    if len(user_info['pwd']) < 6:
        print('密码不能少于6位')
        is_valid = False

    if not re.search(r'@.*?\.com$', user_info['email']):
        # re.search()功能是如果能匹配到就有结果，匹配不到就返回None，而它为None就是if not
        print('邮箱格式不合法')
        is_valid = False

    check_info = {
        'is_valid': is_valid,
        'user_info': user_info
    }

    return check_info


def register(check_info):
    if check_info['is_valid']:
        with open('db.json', 'a+', encoding='utf-8') as f:
            json.dump(check_info['user_info'], f)  # 序列化
            f.write('\n')


def main():
    user_info = interactive()
    check_info = check(user_info=user_info)
    register(check_info)

if __name__ == '__main__':
    main()