#!/usr/bin/env python
# encoding: utf-8
'''
@author: 李勇
@contact: 13732546017@163.com
@software: garner
@file: lesson_file.py
@time: 2018-12-14 20:26
@desc:
'''

# 能调用方法的一定是对象
f=open("小重山","r")
f=f.readlines()
f[5]=''.join((f[5].strip(),"iiiiii"))
for i in f:
    print i.strip()
