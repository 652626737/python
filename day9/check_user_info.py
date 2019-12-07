#!/usr/bin/env python
# encoding: utf-8
'''
@author: 李勇
@contact: 13732546017@163.com
@software: garner
@file: check_user_info.py
@time: 2018-12-24 20:28
@desc:
'''
def check_user_status (User_data,in_user):
    user_date_status = False
    if in_user in User_data:
        return True
    else:
        return "用户不存在"

def check_pass_status(User_data,in_pass):
    pass_date_status = False
    if in_pass in User_data:
        return True
    else:
        return "密码错误"