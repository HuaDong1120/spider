import requests

from urllib import parse
from uuid import uuid4
import os
import time
s = input("请输入要爬取的图片：")
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
    'Cookie': 'your Cookie'
    'Referer': 'http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E4%B8%89%E4%B8%8A%E6%82%A0%E4%BA%9A'
}
session = requests.session()
session.headers = headers


def getHTMLText(url):
    html = session.get(url)

    if html.status_code == 200:
        parse_html(html.json())
    else:
        print("访问网页错误")


def parse_html(html):
    data = html['data']
    for i in data:
        try:
            img = i['middleURL']
            print(img)
            download(img)
        except:
            pass


def download(img_url):
    time.sleep(3);
    html = session.get(img_url)
    print(html.status_code)
    filename = s
    if not os.path.exists(filename):
        os.makedirs(filename)
    with open('./{}/{}.jpg'.format(filename,uuid4()),'wb') as f:
        f.write(html.content)


if __name__ == "__main__":

    name = parse.quote(s)
    for i in range(30, 60, 30):
        url = 'http://image.baidu.com/search/acjson?tn=resultjson_com' \
              '&ipn=rj&ct=201326592&is=&fp=result&queryWord={}' \
              '&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=' \
              '&hd=&latest=&copyright=&word={}&s=&se=&tab=&width=' \
              '&height=&face=&istype=&qc=&nc=1&fr=&expermode=' \
              '&force=&pn={}&rn=30'.format(name, name, i)

        getHTMLText(url)
