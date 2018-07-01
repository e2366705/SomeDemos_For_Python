import requests
from lxml import etree
from urllib import parse

url = 'https://www.zhihu.com/explore'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
html = requests.get(url, headers=headers).text
# 响应返回的是字符串，解析为HTML DOM模式 text = etree.HTML(html)
text = etree.HTML(html)
# 返回所有内容的结点位置
node_list = text.xpath('//div[@class="explore-feed feed-item"]')

for node in node_list:
    # xpath返回的列表，这个列表就这一个参数，用索引方式取出来
    #问题
    question = node.xpath('.//h2/a')[0].text.replace("\n","")
    # 作者
    author = node.xpath('.//*[@class="author-link-line"]/*')[0].text
    #author = "".join(node.xpath('.//*[@class="author-link-line"]//text()')).replace("\n","")
    # 回答
    answer = node.xpath('.//*[@class="content"]')[0].text
    #answer = "".join(node.xpath('.//*[@class="content"]/text()')).strip()
    #answer = str(node.xpath('.//*[@class="content"]/text()'))[1:-1]

    with open('explore.txt', 'a', encoding='utf-8') as file:
        file.write('\n'.join([question, author, answer]))
        file.write('\n' + '=' * 50 + '\n')
