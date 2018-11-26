from selenium import webdriver
import time
import urllib.request
from bs4 import BeautifulSoup
import html.parser

## python 的  selenium + Chrome_web driver
####        此代码演示将web网页下拉到最底端   比如知乎问答 :    https://www.zhihu.com/question/20167901    #####

def main():
    driver = webdriver.Chrome()  # 打开浏览器
    driver.get("https://www.zhihu.com/question/20167901") # 打开想要爬取的知乎页面

    # 模拟用户操作
    def execute_times(times):
        for i in range(times):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
    execute_times(10000)

if __name__ == '__main__':
    main()

    
