 ----------------------------------------------------------------------------------
    需要安装以下依赖库 : 
PyMouse      版本号 : 1.0         1.0
PyUserInput  版本号 : 0.1.10      0.1.11
pywin32      版本号 : 223         223    
 ----------------------------------------------------------------------------------

import pymouse, pykeyboard, os, sys
from pymouse import *
from pykeyboard import PyKeyboard

## 键盘 + 鼠标操作
#完成点击屏幕中央并键入“Hello, World!”的功能：!

m = PyMouse()
k = PyKeyboard()

xxxx, yyyy = m.screen_size()    ## 获取屏幕的尺寸  分别是X 和 Y
print(xxxx , yyyy)
m.click(822,133)
k.type_string('wwwwwwwwwwwwww!')

#鼠标操作：
'''
m.click(x, y, button, n) –鼠标点击
x, y –是坐标位置
buttong –1
表示左键，2
表示点击右键
n –点击次数，默认是1次，2表示双击
m.move(x, y) –鼠标移动到坐标(x, y)
x_dim, y_dim = m.screen_size() –获得屏幕尺寸
'''

wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww



'''
键盘操作:
k.type_string(‘Hello, World!’) –模拟键盘输入字符串
k.press_key(‘H’) –模拟键盘按H键
k.release_key(‘H’) –模拟键盘松开H键
k.tap_key(“H”) –模拟点击H键
k.tap_key(‘H’, n = 2, interval = 5) –模拟点击H键，2
次，每次间隔5秒
k.tap_key(k.function_keys[5]) –点击功能键F5
k.tap_key(k.numpad_keys[5], 3) –点击小键盘5, 3次

联合按键模拟
例如同时按alt + tab键盘
k.press_key(k.alt_key) –按住alt键
k.tap_key(k.tab_key) –点击tab键
k.release_key(k.alt_key) –松开alt键

'''




from selenium import webdriver
import time
import urllib.request
from bs4 import BeautifulSoup
import html.parser
import win32api
import win32con
import pymouse, pykeyboard, os, sys
from pymouse import *
from pykeyboard import PyKeyboard

###                  python 模拟键盘鼠标的操作

# m = PyMouse()
# k = PyKeyboard()

def main():
    driver = webdriver.Chrome()  # 打开浏览器
    driver.get('https://www.jd.com') # 打开想要爬取的知乎页面

    for iii in range(0,11):
        time.sleep(1.5)
        win32api.keybd_event(35, 0, 0, 0)           ### 这是模拟键盘操作 ----> End 键

    time.sleep(2)
    driver.quit()


if __name__ == '__main__':
    main()


'''
可根据键盘模拟指令,结合上一篇远程控制电脑使用

 A   65  
 B   66  
 C   67  
 D   68  
 E   69  
 F   70  
 G   71  
 H   72  
 I   73  
 J   74  
 K   75  
 L   76  
 M   77   
 N   78   
 O   79   
 P   80   
 Q   81   	
 R   82   	
 S   83   	
 T   84     	
 U   85   	    
 V   86   	    
 W   87 
 X   88 
 Y   89 
 Z   90  
   ----------------------------------
 *   106  
 +   107  
 -   109   
 .   110   
 /   111   
  ---------------------------------- 
 Backspace    8 
 Tab  9 
 Clear 12 
 Enter 13 
 Shift 16 
 Control 17 
 Alt  18 
 Caps Lock    20 
 Esc  27 
 Spacebar    32 
 Page Up 33 
 Page Down    34 
  ----------------------------------
 End  35 
 Home 36 
 Left Arrow   37 
 Up Arrow    38 
 Right Arrow   39 
 Down Arrow    40 
 Insert 45 
 Delete 46 
 Help  47 
 Num Lock 144 
 Enter 108 
  ---------------------------------- 
 F1   112 
 F2   113 
 F3   114 
 F4   115 
 F5   116 
 F6   117 
 F7   118 
 F8   119 
 F9   120 
 F10  121 
 F11  122 
 F12  123 
  ----------------------------------
 0   96   
 1   97   
 2   98   
 3   99   
 4   100  
 5   101  
 6   102  
 7   103  
 8   104  
 9   105  
  ----------------------------------
 0   48  
 1   49  
 2   50  
 3   51  
 4   52  
 5   53  
 6   54  
 7   55  
 8   56  
 9   57

'''
