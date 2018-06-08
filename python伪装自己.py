# Small_Python_DemoS
自己写的一些零零散散的Python小Demo


**************************************************************************************************************************************
#伪装自己访问知乎  python requests
#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
import requests

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
response = requests.get("https://www.zhihu.com", headers=headers)
print(response.text)
**************************************************************************************************************************************

#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import requests
headers={"User-Agent" : "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
  "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
  "Accept-Language" : "en-us",
  "Connection" : "keep-alive",
  "Accept-Charset" : "GB2312,utf-8;q=0.7,*;q=0.7"}

#百度百科 [可用]
url_baike = 'https://baike.baidu.com/item/java/85979'

#京东网页 [可用]
url_JD = 'https://search.jd.com/Search?keyword=iPhone&enc=utf-8&wq=iPhone&pvid=68ffcb98c26c4ef3a7d9cae3ef65c16f'

#淘宝网页 [不可用]
url_taobao = 'https://s.taobao.com/search?q=iPhone&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180606&ie=utf8'

r=requests.post(url_JD,headers=headers,allow_redirects=False)   #allow_redirects设置为重定向

r.encoding="UTF-8"
print r.url
print r.text
print r.headers #响应头
print r.request.headers #请求头

