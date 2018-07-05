#!/usr/bin/env python 
# -*- coding: utf-8 -*-
'''
Created on 2018年7月3日
@author: liyong
'''
#这是第一个注释
print "hello word"

# 这是第二个注释
name="liyong"
#这是一个注释

# 等待用户输入

# raw_input("请输入一个数...\n")

# 同一行显示多条语句
import sys
x="liyong123"
sys.stdout.write(x + "\n")
x="a"
y="b"
# 换行输出
print x


print y
print"_________"
# 不换行输出
# 变量后只要加小逗号就会不换行，否则就换行
print x,y,
print x,
print y,
print sys.argv


# 变量的赋值
counter=100
miles=1000.0
name="liyong"
print counter
print miles
print name


# 多变量赋值
a=b=c=d=1
print a
print b
print c
print d


print"-----------------"
a=30
b=40
c= 50

c=a+b
print"1-c的值为:",c
c=a-b
print '2-c的值为：',c
c=a*b
print "3-c的值为：",c
c=a/b
print "4-c的值为：",c
c=b%a
print "5-c的值为：",c
# 修改变量a,b,c
a=2
b=3
c=a**b
print "6-c的值为：",c
print "7-c的值为：",c

a=10
b=5
c=a//b
print "8-c的值为：",c

a=21
b=10
c=0
if(a == b):
    print"1-a=b"
else:
    print"1-a不等于b"
if(a!=b):
    print"2-a不等于b"
else:
    print "2-a等于b" 
if(a<b):
    print "3-a小于b"
else:
    print "3-a不小于b"
if(a>b):
    print "4-a大于b"
else:
    print"4-a不大于b"
print"---------------------"
#修改变量a和b的值
a=5
b=20
if(a<=b):
    print "5-a小于等于b"
else:
    print "a大于b"
if(b>=a):
    print "b大于等于a"
    
print "---------------------"
a=60
b = 13
print "---------------------"
c = a & b
print "a & b=",c
print "---------------------"
c=a|b
print "a|b=",c
print "---------------------"
c=a^b
print "a^b=",c
print "---------------------"

print "a按位取反为:",~a
print "a左移运算符",a<<2
print "b"
    
