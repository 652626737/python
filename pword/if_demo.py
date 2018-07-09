#-*-coding=utf-8 -*-
#!/usr/bin/env python 
'''
Created on 2018年7月9日

@author: liyong
'''
#if基本语法
from pword.helloword import name
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