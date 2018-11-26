import json
import math
import time
import requests


headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Content-Length': '26',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'xxxxxxxxxxxxxxxxx',
    'Host': 'www.lagou.com',
    'Origin': 'https://www.lagou.com',
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'X-Anit-Forge-Code': '0',
    'X-Anit-Forge-Token': 'None',
    'X-Requested-With': 'XMLHttpRequest'
}


def get_page(url, params):
    html = requests.post(url, data=params, headers=headers)
    json_data = json.loads(html.text)
    total_count = json_data['content']['positionResult']['totalCount']
    page_number = math.ceil(total_count / 15) if math.ceil(total_count / 15) < 30 else 30
    get_info(url, page_number)


def get_info(url, page):
    for pn in range(1, page + 1):
        params = {
            'first': 'false',
            'pn': str(pn),
            'kd': 'Python'
        }
        try:
            html = requests.post(url, data=params, headers=headers)
            json_data = json.loads(html.text)
            results = json_data['content']['positionResult']['result']
            for result in results:
                infos = {
                    'businessZones': result['businessZones'],
                    'city': result['city'],
                    'companyFullName': result['companyFullName'],
                    'companyLabelList': result['companyLabelList'],
                    'companySize': result['companySize'],
                    'district': result['district'],
                    'education': result['education'],
                    'explain': result['explain'],
                    'financeStage': result['financeStage'],
                    'firstType': result['firstType'],
                    'formatCreateTime': result['formatCreateTime'],
                    'gradeDescription': result['gradeDescription'],
                    'imState': result['imState'],
                    'industryField': result['industryField'],
                    'jobNature': result['jobNature'],
                    'positionAdvantage': result['positionAdvantage'],
                    'salary': result['salary'],
                    'secondType': result['secondType'],
                    'workYear': result['workYear']
                }
                print('------------------')
                print(infos)
            time.sleep(2)
        except requests.exceptions.ConnectionError:
            pass


if __name__ == "__main__":
    url = 'https://www.lagou.com/jobs/positionAjax.json'
    params = {
        'first': 'true',
        'pn': '1',
        'kd': 'python'
    }
    get_page(url, params)

    
    
