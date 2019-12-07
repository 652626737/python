#!/usr/bin/env python 
# -*- coding: utf-8 -*-
'''
Created on 2018年7月3日
@author: liyong
'''
#这是第一个注释
from test.pickletester import DATA0
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
print "a左移运算符=",a<<2
print "b=",b
print "b右移运算符=",b>>2
print "-------------------"
a=21
b=10
c=0
c=a+b
print "1-c的值为：",c
c+=a
print"2-c的值为：",c
c*=a
print "3-c的值为：",c
c/=a
print "4-c的值为：",c
c=2 
c%=a
c**=a
print "5-c的值为：",c
c//= a
print "6-c的值为：",c
a=10
b=20
# c=a&b
print "7-c的值为：",c
if ( a and b ):
    print "1-变量a和b都为true"
else:
    print "1-变量a和都为不为true"
if(a or b):
    print "2-变量a和b的值为真，或者其中一个变量为真。"    
else:
    print"2-变量a和b的值不为真"
# 修改a变量的值
a=0
if(a and b):
    print"3-变量a和b都为true"
else:
    print"3-变量a和b有一个不为真"
if(a or b):
    print"4-变量a和b的值都为真，或其中一个为真。"
else:
    print"4-变量a和b的值都不为真"
if not(a and b):
    print "5-变量a和b都为假，或其中一个变量为假"
else:
    print"5-变量a和b的值都为真"

''' 
in    如果在指定的序列中找到值返回 True，
否则返回 False。    x 在 y 序列中 , 如果 x 在 y 序列中返回 True
'''
a=10
b=20
list = range(10)
print "list = ",list
if(a in list):
    print "1-变量a在给的列表list中"
else:
    print"1-变量a不在给与的列表list中"
if(b not in list):
    print "2-b变量不在给与的列表list中"
else:
    print"2-b变量在给与的列表list中"
# 修改a变量的值
a=5
if(a in list):
    print "3-变量a在给与的list列表中"
else:
    print "3-变量a不在给与的list列表中"
if(b not in list ):
    print"4-变量b不在给与的列表list中"
else:
    print"4-变量b在给与的列表中"
    
'''
is    is 是判断两个标识符是不是引用自一个对象   
 x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
'''
a=20
b=20
print "a is id=",id(a)
print "b is id=",id(b)

if(a is b):
    print"1-a and b引用同一个对象"
else:
    print"1-a and b 引用不同对象"
#修改b的值
b=10
if(a is not b):
    print"2-a and b 引用不同的对象"
else:
    print"2-a and b 引用同一对象"

        
        
        
    
    
    
    
    
    