#!/usr/bin/python
#python字典排序  (虽然最后返回的是一个列表 list)
import string,re

file_object = open('runoob.txt',encoding='utf-8')
txt_data = file_object.read()

listtt=re.split('\W',txt_data)
new_list = []
for var in listtt:
    if var != '':
        new_list.append(var)
print(new_list)

print('--------------------------------')
#单词出现的频率
dict = {}
for word in new_list:
    if dict.get(word) == None:
        dict[word] = 1
    else:
        dict[word] += 1
print(dict)

print('----------------------')

#字典排序第一步  : 字典转化成列表
dict_list = sorted(dict.items(),key = lambda x:x[1],reverse = True)
print(dict_list)
print('最后的排序结果是 : ')
for var in dict_list:
    print(var)

    .
