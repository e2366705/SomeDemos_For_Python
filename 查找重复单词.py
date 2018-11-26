#!/usr/bin/python
#python查找一段文本重读次数最多的单词
import string,re

file_object = open('runoob.txt',encoding='utf-8')
txt_data = file_object.read()

listtt=re.split('\W',txt_data)
new_list = []
for var in listtt:
    if var != '':
        new_list.append(var)
print(type(new_list))

print('--------------------------------')
#单词出现的频率
dict = {}
for word in new_list:
    if dict.get(word) == None:
        dict[word] = 1
    else:
        dict[word] += 1
print(type(dict))

print('----------------------')

#字典排序第一步  : 字典转化成列表
dict_list = sorted(dict.items(),key = lambda x:x[1],reverse = True)
print(type(dict_list))
print('重复最多单词前十名是 : ')
num = 0
for var in dict_list:
    num += 1
    print(var)
    if num == 10:
        #列出前10个
        break
        
        
