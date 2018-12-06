# -*- coding:utf-8 -*-
'''
Created on 2018年11月14日

@author: liyong
'''
from collections import Counter
from numpy import number
from __builtin__ import str
from pword.if_demo import num

shopping_car = []
xiangqing = []
demo = True
product_List = [
    ("Macbook", 12000),
    ("cat", 50000),
    ("Python Book", 500),
    ("bike", 200)
]
saving = raw_input("请输入你有多少钱")
if saving.isdigit():
    saving = int(saving)
while demo:
    for i, v in enumerate(product_List, 1):
        print (i, ">>>", v)
    choice = raw_input("请选择一个商品[q:推出]")
    if choice.isdigit():
        choice = int(choice)
        if choice > 0 and choice <= len(product_List):
            p_item = product_List[choice - 1]

            if p_item[1] <= saving:
                saving -= p_item[1]
                shopping_car.append(p_item)
            else:
                print"余额不足,还剩%s" % saving
        else:
            print "编码不存在"

    elif choice == "q":
        demo = False
        print "你已经购买了"

        for l in shopping_car:
            if l not in xiangqing:
                xiangqing.append(l)

        for d in xiangqing:
            num = shopping_car.count(d)
            name = d[0]
            price = d[1]

            zong = price * num
            print '商品名称:%s  ¥:%d *%d  总计:%d' % (name, price, num, zong)

        # print l + ">>>" + p_item.count()
    else:
        print"输入数值有无 "
