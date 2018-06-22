# -*- coding: utf-8 -*-
import os
from PIL import Image, ImageDraw, ImageFont
import PIL


#计算文本文件的行数
txt_lines = 0
file = open("ppp.txt", encoding='utf-8') 
while 1:
    txt_lines += 1
    line = file.readline()
    if not line:
        break
    pass # do something
file.close()
print('这个文本文件有 : ' , txt_lines-1 , '行')

#读取文本的数据
f = open('ppp.txt', encoding='utf-8')
txt_data = f.read()
f.close()
print(txt_data)

text = txt_data

#图片文件的一行相当于文本文件的19行
row = txt_lines * 19
im = Image.new("RGB", (1000,row), (255, 255, 255))
dr = ImageDraw.Draw(im)
font = ImageFont.truetype(os.path.join("fonts", "msyh.ttf"), 14)
 
 # 0,0是打印到图片时的偏移量 [左偏移多少,上偏移多少]
dr.text((0, 0), text, font=font, fill="#000000")
 
#生成图片后立即打开
im.show()

#生成图片后保存
#im.save("t.png")
