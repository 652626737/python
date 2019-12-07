#!/usr/bin/env python
# encoding: utf-8
'''
@author: 李勇
@contact: 13732546017@163.com
@software: garner
@file: json_demo.py
@time: 2018-12-16 13:42
@desc:
'''

with open("省市区", "r", "encode=utf-8") as json_read, open("省市区2", "w", "encode=utf-8") as json_with:
for line in json_read:
    print  line