# json格式(第一頁共25篇)
import requests
from bs4 import BeautifulSoup
import json
from lxml import etree  # 欲使用 Xpath
from random import randint
from time import sleep
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}

url = 'https://www.pixnet.net/mainpage/api/tags/%E5%8F%B0%E5%8C%97/feeds?page=1&per_page=25'

ss = requests.session()
response = ss.get(url, headers=headers)
res = response.json()

# -------------------------
# typee = []
# title = []
# urll = []
# tagss = []
# blogg = []
# jpgg = []
# articlee = []

dict_0 = {}



# --------------------------


total_page = res['data']['total_page']

for i in range(1, total_page):

    #     total_page = str(i)
    each_url = 'https://www.pixnet.net/mainpage/api/tags/%E5%8F%B0%E5%8C%97/feeds?page=' + str(i) + '&per_page=25'
    #     url = 'https://www.pixnet.net/mainpage/api/tags/%E5%8F%B0%E5%8C%97/feeds?page=1&per_page=25'

    ss = requests.session()
    response = ss.get(each_url, headers=headers)
    print(response) #只顯示一次25篇的response
    #     time.sleep(random.randint(2,6))
    res = response.json()

    for each_element in res['data']['feeds']:

        # typee.append(each_element['type'])
        # print('type : ', each_element['type'])

        # title.append(each_element['title'])
        print('title : ', each_element['title'])

        new_url = each_element['link']
        # urll.append(new_url)
        print('網址 : ', new_url)

        #         print('圖檔 : ',each_element['images_url'])  #每篇最多3張圖片

        # tagss.append(each_element['tags'])
        print('tags : ', each_element['tags'])  # 不包含搜尋的關鍵字: 台北

        # 解決請求速度過快導致程序報錯
        #         while 1:

        try:
            # 針對列表的文章進行文字的爬取
            response1 = ss.get(new_url, headers=headers)
            print(response1)

            #         time.sleep(random.randint(3,8))
            response1.encoding = 'utf-8'

            #             except:

            #                 print("Connection refused by the server..")
            #                 print("Let me sleep for 5 seconds")
            #                 print("ZZzzzz...")
            #                 time.sleep(10)
            #                 print("Was a nice sleep, now let me continue...")

            #                 continue

            # 使用xpath解析網頁
            new_res = etree.HTML(response1.text)

            content_01 = new_res.xpath('//*[@id="article-box"]/div/div[2]/ul/li[1]/a//text()')  # 全站分類

            content_00 = new_res.xpath('//*[@id="article-content-inner"]//p//img/@src')  # jpg

            #         //*[@id="article-content-inner"]/p//img//@src
            content = new_res.xpath('//*[@id="article-content-inner"]//p//text()')  # 內文

            # 每篇的: 全站分類
            for j, text22 in enumerate(content_01):
                content_01[j] = text22.strip()

            T = ''.join(content_01)
            # blogg.append(T)
            print(T)

            # 每篇的jpg
            for j, text22 in enumerate(content_00):
                content_00[j] = text22.strip()

            J = content_00
            # jpgg.append(J)
            print(J)

            # 簡單的資料清洗 (print出內文)
            for j, text22 in enumerate(content):
                content[j] = text22.strip()

            article = ''.join(content)
            # articlee.append(article)
            print(article)

            print('================================')




        except:
            print("Connection refused by the server..")
            print("Let me sleep for 5 seconds")
            print("ZZzzzz...")
            time.sleep(5)
            print("Was a nice sleep, now let me continue...")
            continue
