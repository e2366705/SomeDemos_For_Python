
#根据url生成二维码
#根据文本数据生成二维码
import qrcode
def qrcodeWithUrl(url):
    img=qrcode.make(url)
    #保存图片
    savePath=r'D:\1.png'
    img.save(savePath)
    print(img)

#根据输入内容生成二维码

def qrcodeWithText(text):
    img=qrcode.make(text)
    #保存图片
    savePath=r'D:\\2.png'
    img.save(savePath)
    print(img)

### test 就是你输入的需要转化的文字二维码!!!!!!
test = r'https://www.pornhub.com/view_video.php?viewkey=ph5b06c9cc6ae00'
qrcodeWithText(test)
print('二维码已生成！')
