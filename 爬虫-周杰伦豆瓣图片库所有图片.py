#!/usr/bin/python
# -*- coding: UTF-8 -*-
# -*- utf-8 -*-

import os
import requests
from bs4 import BeautifulSoup

def GetHtmlText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""

def main(pages):
    # 创建本地存储图片文件夹
    FilePath = os.getcwd() + '\pictureJay\\'
    if not os.path.exists(FilePath):
        os.makedirs(FilePath)
    # 图片页数
    TempPage = pages
    # 命名序号
    FileNum = 1
    for page in range(pages):
        url = 'https://movie.douban.com/celebrity/1048000/photos/?type=C&start=' + str(page * 30) + '&sortby=like&size=a&subtype=a'
        html = GetHtmlText(url)
        soup = BeautifulSoup(html, 'html.parser')
        uls = soup.find_all('ul', {"class": "poster-col3 clearfix"})
        for ul in uls:
            imgs = ul.find_all('img')
            for img in imgs:
                imgurl = img['src']
                imgcontent = requests.get(imgurl).content
                filename = str(FileNum) + '.jpg'
                with open(os.getcwd() + '/pictureJay/' + filename, 'wb') as wf:
                    wf.write(imgcontent)
                FileNum += 1

if __name__ == '__main__':
    main(9)

    
    
