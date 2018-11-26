#! /usr/bin/env python 
# -*- coding: utf-8 -*- 
#运行环境 : python 3.6.2
#用来统计账单的花钱数,并且排序,算出总金额 

import re
import sys 
import chardet  
from asn1crypto._ffi import null
from _overlapped import NULL

f = open("1212.txt")  # 返回一个文件对象  
line = f.readline()  # 调用文件的 readline()方法  
dict = {}

def string_money_re(string):
    string__ = string.strip('\n')  
    money = re.findall(r'(\d+)\.?(\d+)?', string__)
    if money[-1][1] :
        sreing_money = str(money[-1][0] + '.' + money[-1][1])
        return sreing_money
    else : 
        sreing_money = str(money[-1][0] + '.' + '0')
        return sreing_money

while line:  
    goods_money = string_money_re(line)
    
    goods = line.strip('\n')
    
    dict[goods] = float(goods_money) # 添加信息
    line = f.readline()  
    
    
def dict2list(dic=dict):
    # 将字典转化为列表 
    keys = dic.keys()
    vals = dic.values()
    lst = [(key, val) for key, val in zip(keys, vals)]
    return lst

new_list = sorted(dict2list(dict), key=lambda x:x[1], reverse=False) # 按照第1个元素降序排列

print(dict)
print(new_list)
new_new_dict = {}
for i in new_list:
    new_new_dict[i[0]] = i[1]    
print(new_new_dict)

print('-----------------------------------------------------------------')
money = 0
for Goo,Mon in new_new_dict.items():

    money = Mon + money
    print(Mon,Goo)

print('共计 : ',money,'元人民币')

print('-----')


