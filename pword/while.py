#-*- coding=utf-8 -*-
'''
Created on 2018年7月10日

@author: liyong
'''
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
    a=1
while 1:
    print "given flag is really true!"
    print a
    a+=1
    
        














