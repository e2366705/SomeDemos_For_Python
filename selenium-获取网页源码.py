from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://search.bilibili.com/all?keyword=python')
print(browser.page_source)
browser.close()

通过page_source属性可以获取网页的源代码


###  这份教程很不错   
https://cuiqingcai.com/5630.html

  
