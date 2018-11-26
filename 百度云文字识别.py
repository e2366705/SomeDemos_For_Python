首先 ： pip install baidu-aip
pip install baidu-aip
pip install baidu-aip
pip install baidu-aip
pip install baidu-aip

重要的事说三遍！！！！！

pip install baidu-aip
pip install baidu-aip
pip install baidu-aip


---------------------------------------------------------------------

from aip import AipOcr

config = {
    'appId': '11664034',
    'apiKey': 'BL4jDkgBqW6qYxImabEZ8Pji',
    'secretKey': 'TuFAnKcSYD9xDwnvLeImBR8LpEOhmQD3'
}

client = AipOcr(**config)

def get_file_content(file):
    with open(file, 'rb') as fp:
        return fp.read()

def img_to_str(image_path):
    image = get_file_content(image_path)
    result = client.basicGeneral(image)
    print(result)
    if 'words_result' in result:
        return '\n'.join([w['words'] for w in result['words_result']])


if __name__ == '__main__' :
    img_to_str(r'C:\Users\QAQ\Desktop\1.jpg')
    
    
