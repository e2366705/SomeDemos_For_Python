from selenium import webdriver
import os
#selenium--chromedriver
#引入chromedriver.exe
chromedriver = "C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)

#设置浏览器需要打开的url
url = "http://www.baidu.com"
browser.get(url)

#在百度搜索框中输入关键字"python"
browser.find_element_by_id("kw").send_keys("Python3的安装")
#单击搜索按钮
browser.find_element_by_id("su").click()

#关闭浏览器
#browser.quit()
