windows 中文件的路径!!!!!
folder = r'D:\Py\xianyu\xianyu.txt'
folder = r'D:\Py\xianyu\xianyu.txt'
folder = r'D:\Py\xianyu\xianyu.txt'
folder = r'D:\Py\xianyu\xianyu.txt'
folder = r'D:\Py\xianyu\xianyu.txt'
folder = r'D:\Py\xianyu\xianyu.txt'
folder = r'D:\Py\xianyu\xianyu.txt'
folder = r'D:\Py\xianyu\xianyu.txt'folder = r'D:\Py\xianyu\xianyu.txt'
folder = r'D:\Py\xianyu\xianyu.txt'
folder = r'D:\Py\xianyu\xianyu.txt'folder = r'D:\Py\xianyu\xianyu.txt'
folder = r'D:\Py\xianyu\xianyu.txt'

加 r

加 r

加 r

加 r

加 r

加 r

创建文件夹 : 
os.mkdir("D:\\pythoooooooooooooooooooooon") 

#创建多级目录  
os.makedirs("D:\\python\\oo\\2\\3")

#删除文件夹
os.rmdir("D:\\pythoooooooooooooooooooooon")  

#删除多级目录  
os.removedirs("D:\\python\\oo\\2\\3");  

#返回当前目录绝对路径
os.path.abspath('.')

#获取当前目录位置
path1=os.getcwd()
print(path1)  

#获取目录下文件夹及文件
paths=os.listdir("D:\\pythonnnn")
print(paths)
for path in paths:
    print(path)
    


# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
print(os.path.join('D:\\', 'wwwwwwwwwwwwwwwwwwwwwwwwwwww'))
###输出 : D:\wwwwwwwwwwwwwwwwwwwwwwwwwwww


#遍历所有子目录及文件 (主要是文件!!!!)
for p1,d,filelist in os.walk('D:'+os.sep+'KwDownload'):
    for f1 in filelist:
        fp=os.path.join(p1,f1)
        print(fp)

#获取目录下文件夹  (主要是文件夹)
paths=os.listdir("D:\\KwDownload")
for path in paths:
    print(path)
  
 # r只读，w可写，a追加
with open('D:\\QQQQQQQQQQQ.txt','a',encoding='UTF-8') as fff:
    fff.write('你好啊!!!!\n')
    fff.close()
    
#               读  文件 Read
folder = r'D:\Py\xianyu\xianyu.txt'
with open(folder , 'r', encoding='UTF-8') as fff:        //r   表示只读 
    the_txt_data = fff.read()          // 这就是txt文件的数据
fff.close()
