# -*- coding:utf-8 -*-
#!/usr/bin/env python

'''
Created on 2018年12月7日

@author: liyong
'''


av_catalog = {
    "河北": {
        "廊坊": ["固安 ", "香河", "三河"],
        "天津": ["塘沽", "河西"],
        "石家庄": ["石家庄", "辛集"],
        "保定": ["涿州", "涞水"]
    },
    "山东": {
        "济南": ["天桥区", "丽城区", "长青区"]
    },
    "北京": {
        "朝阳": ["望京", "大裤衩"]
    }
}
back_flag = False
while not back_flag:
    for key in av_catalog:
        print key
    choice = raw_input("层1").strip()
    if choice in av_catalog:
        while not back_flag:
            for key2 in av_catalog[choice]:
                print key2
            choice2 = raw_input("层2").strip()
            if choice2 == "b":
                back_flag = True
            if choice2 in av_catalog[choice]:
                while not back_flag:
                    for key3 in av_catalog[choice][choice2]:
                        print key3
                    choice3 = raw_input("层3").strip()
                    if choice3 == "b":
                        back_flag = True
                    else:
                        back_flag = False
                else:
                    back_flag = False
            else:
                print"无效输入"
        else:
            back_flag = False
    else:
        print"无效输入"
