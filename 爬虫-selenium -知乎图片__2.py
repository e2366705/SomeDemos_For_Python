from selenium import webdriver
import time
import urllib.request
from bs4 import BeautifulSoup
import html.parser

def main():
    driver = webdriver.Chrome()  # 打开浏览器
    driver.get("https://www.zhihu.com/question/40273344") # 打开想要爬取的知乎页面

    # 模拟用户操作
    def execute_times(times):

        for i in range(times):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            try:
                driver.find_element_by_css_selector('button.QuestionMainAction').click()
                print("page" + str(i))
                time.sleep(1)
            except:
                break

    execute_times(2)

    result_raw = driver.page_source  # 这是原网页 HTML 信息
    result_soup = BeautifulSoup(result_raw, 'html.parser')# 然后将其解析
    result_bf = result_soup.prettify()  # 结构化原 HTML 文件
    with open("111.txt", 'w',encoding="utf-8") as girls:  # 存储路径里的文件夹需要事先创建。
        girls.write(result_bf)
    girls.close()
    print("爬取回答页面成功!!!")


    with open("222.txt", 'wb') as noscript_meta:
        noscript_nodes = result_soup.find_all('noscript')  # 找到所有<noscript>node
        noscript_inner_all = ""
        for noscript in noscript_nodes:
            noscript_inner = noscript.get_text()  # 获取<noscript>node内部内容
            noscript_inner_all += noscript_inner + "\n"

        noscript_all = html.parser.unescape(noscript_inner_all).encode('utf-8')  # 将内部内容转码并存储
        noscript_meta.write(noscript_all)

    noscript_meta.close()
    print("爬取noscript标签成功!!!")

    img_soup = BeautifulSoup(noscript_all, 'html.parser')
    img_nodes = img_soup.find_all('img')
    with open("333.txt", 'w') as img_meta:
        count = 0
        for img in img_nodes:
            if img.get('src') is not None:
                img_url = img.get('src')

                line = str(count) + "\t" + img_url + "\n"
                img_meta.write(line)
                urllib.request.urlretrieve(img_url, "./image/" + str(count) + ".jpg")  # 一个一个下载图片
                count += 1

    img_meta.close()
    print("图片下载成功")
if __name__ == '__main__':
    main()
    
    
