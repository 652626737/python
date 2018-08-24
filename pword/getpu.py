#coding=utf-8
'''
Created on 2018年8月24日
@author: liyong
'''
import requests

url = 'http://www.mzitu.com'

#设置headers，网站会根据这个判断你的浏览器及操作系统，很多网站没有此信息将拒绝你访问
header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}

#用get方法打开url并发送headers
html = requests.get(url,headers = header)

#打印结果 .text是打印出文本信息即源码
print(html.text)