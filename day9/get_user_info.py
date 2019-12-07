#!/usr/bin/env python
# encoding: utf-8
'''
@author: 李勇
@contact: 13732546017@163.com
@software: garner
@file: get_user_info.py
@time: 2018-12-24 19:20
@desc:
'''
User_Info = []

def get_user_info():
    # 读取京东数据
    User_data_jingdong =open("jingdong","r")
    data_jingdong = User_data_jingdong.readlines()
    for i in data_jingdong:
        User_Info.append(i.strip())
     # 读取微信数据
    User_data_weixin = open("weixin", "r")
    data_weixin = User_data_weixin.readlines()
    for a in data_weixin:
        User_Info.append(a.strip())
    return User_Info



