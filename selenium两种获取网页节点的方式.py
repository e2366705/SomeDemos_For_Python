
##第一种 : 用时 : 0.4090232849121094 秒

#!/usr/bin/python
# -*- coding: UTF-8 -*-
from lxml import etree
from selenium import webdriver
import time
import re

# ---------------------------------------------- search的结果___ (格式 [教程名 : 教程链接]) ----------------------------------------------#
search_webs_data = []


def search_webs(URL):

    browser = webdriver.Chrome()
    browser.get(URL)
    time.sleep(5)

    time_start = time.time();  # time.time()为1970.1.1到当前时间的毫秒数
    name2 = browser.find_elements_by_xpath('//*[@id="server-search-app"]/div[2]/div[2]/div/div[2]/ul[4]/li/div/div[1]/a')
    for name in name2:
        print(name.text)
    time_end = time.time();  # time.time()为1970.1.1到当前时间的毫秒数    0.3330190181732178
    print(time_end - time_start)
    print('-----^^^^^^^^--------')

    ## 用时 : 0.4090232849121094 秒

    time.sleep(1)
    browser.quit()


if __name__ == '__main__':
    search_webs('https://search.bilibili.com/all?keyword=python&from_source=banner_search&page=1')
    
    #####################################################################################################
    #####################################################################################################
    #####################################################################################################
        
    
    # 第二种 :  用时 0.03000187873840332 秒
    
    #!/usr/bin/python
# -*- coding: UTF-8 -*-
from lxml import etree
from selenium import webdriver
import time
import re

# ---------------------------------------------- search的结果___ (格式 [教程名 : 教程链接]) ----------------------------------------------#
search_webs_data = []

def  search_webs(URL):
    browser = webdriver.Chrome()
    browser.get(URL)
    time.sleep(5)

    time_start = time.time();  # time.time()为1970.1.1到当前时间的毫秒数
    html_code = browser.page_source                #获得网页源码数据
    html_etree = etree.HTML(html_code)            #结构化网页源码

    #课程名字
    name1 = html_etree.xpath('//*[@id="server-search-app"]/div[2]/div[2]/div/div[2]/ul[4]/li/div/div[1]/a/@title')
    for name in name1:
        print(name)
    time_end = time.time();  # time.time()为1970.1.1到当前时间的毫秒数    0.002000093460083008
    print(time_end - time_start)
    print('-----^^^^^^^^--------')

    ##    用时 :0.03000187873840332 秒



if __name__ == '__main__' :
    search_webs('https://search.bilibili.com/all?keyword=python&from_source=banner_search&page=1')
    .
    
