#-*- coding=utf-8 -*-
'''
Created on 2018年7月10日

@author: liyong
'''
nums = range(100)
even = []
odd = []
while len(nums)>0:
    num = nums.pop()
    if (num % 2 == 0 ) :
        even.append(num)
        even.reverse()
    else:
        odd.append(num)

nums2 = range(200)
even2 = []
odd2 = []
while len(nums2)>0:
    num2 = nums2.pop()
    if (num2 % 2 ==0 ) :
        even2.append(num2)
    else:
        odd2.append(num2)
# 获取前10个元素
print even[:10]
# 获取倒数10个原素
print even[-10:]
# 获取前10个元素隔1个打印一个
print even[:10:2]
print odd
print even2
print odd2
# break结束循环
a=1
while a<20:
    a+=1
    if a%2>0:
        break
    print a
# continue结束本兮循环集训下次循环
a=1
while a<20:
    a+=1
    if a%2>0:
        continue
    print a
