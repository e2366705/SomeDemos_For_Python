#!/usr/bin/python
# -*- coding: UTF-8 -*-
# -*- utf-8 -*-
# coding = utf-8
#coding:utf-8
import requests
from lxml import html

for i in range(10):
    url = 'https://movie.douban.com/top250?start={}&filter='.format(i*25)
    header = {"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16"}

    con = requests.get(url,headers=header)
    r = con.content
    sel = html.fromstring(r)

    for i in sel.xpath('//div[@class="info"]'):
        title = i.xpath('div[@class="hd"]/a/span[@class="title"]/text()')[0]
        info = i.xpath('div[@class="bd"]/p[1]/text()')
        info_1 = info[0].replace(" ", "").replace("\n", "")
        date = info[1].replace(" ", "").replace("\n", "").split("/")[0]
        country = info[1].replace(" ", "").replace("\n", "").split("/")[1]
        geners = info[1].replace(" ", "").replace("\n", "").split("/")[2]
        rate = i.xpath('//span[@class="rating_num"]/text()')[0]
        comCount = i.xpath('//div[@class="star"]/span[4]/text()')[0]
        print(title,info_1,rate,date,country,geners,comCount)

        
        
        
