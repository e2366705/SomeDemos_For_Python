#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
'''
url  = 'http://tieba.baidu.com/p/2256306796'
page = urllib.urlopen(url)
print page.read()
'''

'''
这个项目  是手动把网页源码保存在text.py中的,然后下载图片

'''

import os
import re
import urllib

def read_html_code():
    #网页的源码保存在text.py中 , 只需要用正则表达式筛选一下就可以把图片的链接提取出来了
    file_object = open('test.py') 
    try:
        #file_context是网页的源码
        file_context = file_object.read() 
        print 'file_context----网页的源码是 : ',file_context
        print '-----------------------------------------------------------------------------------------------'
        
        #正则表达式筛选链接
                #re.compile(r'<img.+?src="(.+?\.jpg)" width')  
        jpgReg = re.compile(r'<img.+?src="(.+?\.jpg)" width')

        #筛选的结果是一个集合 list []
        jpgs = re.findall(jpgReg, file_context)
        print    '筛选的结果是一个集合 list [] ---- ' ,jpgs
        return jpgs
    
    finally:
        file_object.close()
        
        
# 用图片url下载图片并保存成制定文件名
def downloadJPG(imgUrl,fileName):
    urllib.urlretrieve(imgUrl,fileName)
    
        
# 批量下载图片，默认保存到当前目录下
def batchDownloadJPGs(jpgs_url_list,path = './'):
    # 用于给图片命名
    count = 1
    for url in jpgs_url_list:
        downloadJPG(url,''.join([path,'{0}.jpg'.format(count)]))
        count = count + 2

               
if __name__ == '__main__':
     HTML__Code = read_html_code()
     batchDownloadJPGs(HTML__Code)
