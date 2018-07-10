#-*- coding=utf-8 -*-
'''
Created on 2018年7月10日

@author: liyong
'''
i=2
while (i<100):
    j=2
    while(j<=(i/j)):
        if not (i%j): break
        j+=1
    if(j>i/j):print i,"是素数"
    i+=1
print "good bye"