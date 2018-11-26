#!/usr/bin/env python
# coding=utf-8
import os
import urllib.request

url = 'http://www.jd.com'
dir = os.path.abspath('.')          ## 返回当前文件夹

## 开始下载网页文件
work_path = os.path.join(r'D:\Py\xianyu', 'baiduuuuuuuuuuuuuu.html')   
urllib.request.urlretrieve(url, work_path)


