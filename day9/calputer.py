#!/usr/bin/env python
# encoding: utf-8
'''
@author: 李勇
@contact: 13732546017@163.com
@software: garner
@file: compiuter.py
@time: 2018-12-30 21:24
@desc:
'''
import re
Flag=True
s = raw_input("输入一个表达式")
def check(s):
    if re.findall('0-9a-zA_Z',s):
        print "invalid"
        flag = False
        pass
    return flag
def format(s):
    s = s.replace(' ','')
    s = s.replace('++',"+")
    s = s.replace('+-','-')
    s = s.replace('--','+')
    s =  s.replace('-+','-')
    return s

if check(s):
    strs =format(s)
    while re.search('\('):
        re.search('\([^()]+\)',strs)
        pass
    else:
        pass