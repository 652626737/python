#-*- coding=utf-8 -*-
'''
Created on 2018年7月10日

@author: liyong
'''
from string import index
for letter in "python":
    print "当前字母：",letter
fruits = ["banana","apple","mango"]
for fruit in fruits:
    print "当前水果是",fruit
# 通过序列索引跌代
fruits = ["banana","apple","mango"]
for index in range(len(fruits)):
    print"当前水果是：",fruits[index]
for num in range(10,20):
    for i in range(2,num):
        if num%2==0:
            j=num/i
            print "%d 等于 %d *%d "%(num,i,j)
            break
    else:
        print num ,"是一个质数"