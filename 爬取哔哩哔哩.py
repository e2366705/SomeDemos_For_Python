#!/usr/bin/python
# -*- coding: UTF-8 -*-
from lxml import etree
from selenium import webdriver
import time
import re
import os

#     01 - 25 页数据的爬取

# ----------------------------------------------返回链接集合--正则表达式提取每一页搜索结果的链接  ----------------------------------------------#
def re_href(URL):
    URLstring  =  search_webs(URL)
    pattern = re.compile(r'//(.*?)\'')  # 匹配模式
    url = re.findall(pattern, URLstring)
    for URLLLL in url:
        URLllll = 'https://'+URLLLL
        print(URLllll)
        tutorial_details(URLllll)

# ---------------------------------------------- search的结果___ (格式 [教程名 : 教程链接]) ----------------------------------------------#
search_webs_data = []
search_webs_data_2 = ''

def  search_webs(URL , page_num):
    browser = webdriver.Chrome()
    browser.get(URL)

    time.sleep(1)

    html_code = browser.page_source                #获得网页源码数据
    html_etree = etree.HTML(html_code)            #结构化网页源码

    #课程名字
    name = html_etree.xpath('//*[@id="server-search-app"]/div[2]/div[2]/div/div[2]/ul/li/div/div[1]/a/@title')         ## XPath寻找网页节点

    #课程链接
    link    = html_etree.xpath('//*[@id="server-search-app"]/div[2]/div[2]/div/div[2]/ul/li/div/div[1]/a/@href')

    for name_link in zip(name,link):
        search_webs_data.append(name_link)

    search_webs_data_2 = '------------------ 这是第:' + str(page_num)+ '页 ------------------\n'
    line_num = 1
    for aaa in search_webs_data:
        aaaaaa = str(aaa)
        search_webs_data_2 =str(line_num) + aaaaaa + '\n' + search_webs_data_2
        line_num += 1

    time.sleep(1)
    browser.close()
    time.sleep(2)
    return str(search_webs_data_2)

# ---------------------------------------------- 将获取到的数据写入txt文件----------------------------------------------#
def write_data_txt(data,page_num,URL):
    folder = 'D:\\Py\\bilibili\\' + folder_name + '\\1000_results.txt'
    with open(folder , 'a', encoding='UTF-8') as fff:
        fff.write(URL + '\n\n' + data + '\n\n\n')
        fff.close()



if __name__ == '__main__' :
    search_string = input('请输入你要在B站搜索的关键词-(比如python) : ')
    folder_name = 'bilibili_search_by_' + search_string
    os.mkdir('D:\\Py\\bilibili\\' + folder_name)


    # ---------------------------------------------- 循环获取几页的数据----------------------------------------------#
    for page_num in range(1, 51):
        print('------------------------------------正在爬取第_' + str(page_num) + '_页------------------------------------')
        search_webs_data.clear()
        URL = 'https://search.bilibili.com/all?keyword=' + search_string + '&page=' + str(page_num)
        write_data_txt(search_webs(URL, page_num), page_num, URL)
        time.sleep(1)


----------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------


#!/usr/bin/python
# -*- coding: UTF-8 -*-
from lxml import etree
from selenium import webdriver
import re
import threading
import time
import os
countTTT = 308

###   ----------------------------------线程_1 ----------------------------------
def jie_xi(forder):
    with open(forder, 'r', encoding='UTF-8') as fff:
        txt_data = fff.read()
        pattern = re.compile(r'//(.*?)\'')
        urls = re.findall(pattern, txt_data)

        for url in urls:
            url = 'https://' + url
            Handle_urls(url)
        print('the end.............')
        time.sleep(5)
        os.system("shutdown -s -t 0")
        fff.close()

def Handle_urls(url):
    browser = webdriver.Chrome()
    browser.get(url)
    time.sleep(2)

    ### 课程 - 标题
    video_title = browser.find_element_by_xpath('//*[@id="viewbox_report"]/h1')

    try:
        browser.find_element_by_css_selector('#v_multipage > ul > a.item.v-part-toggle').click()
        time.sleep(1)
        data = ''
        data = video_title.text + '\n-------------------------------------------------------\n'
        AAA = browser.find_elements_by_xpath('//*[@id="v_multipage"]/ul/a')
        for name in AAA:
            data = data + '\n' + name.text
        save_data(data)
        time.sleep(3)
        browser.close()
    except Exception as e:
        print('哎呀......只有标题啊............')
        save_data('\n' + video_title.text + '\n\n')
        time.sleep(1)
        browser.close()
    else:
        print('emmmmmmmmmm...')


def save_data(data):
    global countTTT
    forder = 'D:\\Py\\bilibili\\bilibili_search_by_python\\result_pages_1000_pages.txt'
    with open(forder , 'a' , encoding='UTF-8') as fff:
        fff.write('\n-------------------------No.' + str(countTTT) + '条-------------------------\n' + data)
        fff.close()
    print('已经执行了:' + str(countTTT) + '次操作')
    countTTT += 1

if __name__ == '__main__':
    forder = 'D:\\Py\\bilibili\\bilibili_search_by_python\\1000_results2.txt'
    jie_xi(forder)


