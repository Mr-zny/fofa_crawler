import json
import os


#初始化函数
def config_init():
        global fofa_email,fofa_key,file_path,url,headers,cookie

        headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Cookie': '你的cookie',
                'Host': 'fofa.info',
                'If-None-Match': '7f903-2D+qhFA0HzGH1WQkX+JqPPpUoSM',
                'sec-ch-ua-platform': 'Windows',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
        }
        url = "https://fofa.info/result?qbase64="

        if os.path.exists('./config.json'):
                config_data = json.loads(open('config.json', mode='r', encoding='utf-8', ).read())
                fofa_email = config_data['fofa_email']
                fofa_key = config_data['fofa_key']
                file_path=config_data['file_path_name']
                cookie = config_data['cookie']
                headers['Cookie'] = cookie


config_init()


