from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://search.bilibili.com/all?keyword=python')
print(browser.page_source)
browser.close()

