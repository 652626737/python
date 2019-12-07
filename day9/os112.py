#!/usr/bin/env python
# encoding: utf-8
'''
@author: 李勇
@contact: 13732546017@163.com
@software: garner
@file: os.py
@time: 2018-12-27 20:09
@desc:
'''
import os
import sys
print os.getcwd()

os.chdir("/Users/liyong/PycharmProjects/python/")



print  os.listdir("/Users/liyong/PycharmProjects/python/")


print  os.stat("/Users/liyong/PycharmProjects/python/day9/os112.py").st_atime

print  os.sep

print os.system("dir")
print  os.environ
sys.