#-*-coding=utf-8 -*-
#!/usr/bin/env python 
'''
Created on 2018年7月9日

@author: liyong
'''
#if基本语法
from StdSuites.Type_Names_Suite import null
from test.test_getargs2 import Int
from __builtin__ import int
flag = False
name = 'luren'
if name == "python":
    flag = True
    print "welcome boss"
else:
    print name
num = 5

if num ==3:
    print "boss"
elif num ==2:
    print "user"
elif num==1:
    print "worker"
elif num<0:
    print "erro"
else:
    print "roadman"
num = 9
if num>=0 and num<=10:
    print"hello"
num = 10
if num<0 or num>10:
    print "hello"
else:
    print"undefine"
num = 8
#判断一个值是否在0-5或者是10-15之间
if (num<=0and num<=5) or (num>=10 and num <=15):
    print"hello"
else:
    print"undefine"
var = 100
if ( var == 100):print "变量var的值为100"
print "good bye"
    
num = range(100)
even = []
odd =[]
while len(num)>0:
    number = num.pop()
    if(number%2==0):
            even.append(number)
    else:
            odd.append(number)
print even
print odd
count=0
while count<10:
    print "the count is ",count
    count+=1
            
i=1
while i<10:
    i+=1

    if i%2>0:
        continue
    print i
             
i=1
while 1:
    print i
    i+=1
    if i>100:
        break        
var = 1
# while var ==1:
#     num =int(raw_input("输入一个数？\n"))
#     print type(num)
#     if(isinstance(num, int)):
#         print "你输入的是",num
#         print "good bye!"
count = 0
while count<5:
    print count ,"is less than 5"
    count+=1
else:
    print count,"is not less than 5"


        














