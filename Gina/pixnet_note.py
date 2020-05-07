# json格式(第一頁共25篇)

import requests
from bs4 import BeautifulSoup
import json
from lxml import etree  # 欲使用 Xpath
import random
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
article_type = []
article_title = []
article_url = []
tags = []
blogg = []
jpgg = []
articlee = []

# --------------------------


total_page = res['data']['total_page']

# for i in range(1, total_page):
for i in range(1, 2):

    #     total_page = str(i)
    each_url = 'https://www.pixnet.net/mainpage/api/tags/%E5%8F%B0%E5%8C%97/feeds?page=' + str(i) + '&per_page=25'
    #     url = 'https://www.pixnet.net/mainpage/api/tags/%E5%8F%B0%E5%8C%97/feeds?page=1&per_page=25'
    # print(each_url)


    ss = requests.session()
    response = ss.get(each_url, headers=headers)
    # time.sleep(random.randint(2, 6))
    res = response.json()


    print("=========================")
    for each_element in res['data']['feeds']:

        # print(each_element)
        # {'type': 'blog', 'member_uniqid': '784035b2117bc9e79d', 'display_name': '尋也',
        #  'avatar': 'https://s8.pimg.tw/avatar/cw980374/0/0/zoomcrop/45x45.png?v=1531576328', 'title': '【台北】穗科手打烏龍麵',
        #  'link': 'https://cw980374.pixnet.net/blog/post/321456332-%e3%80%90%e5%8f%b0%e5%8c%97%e3%80%91%e7%a9%97%e7%a7%91%e6%89%8b%e6%89%93%e7%83%8f%e9%be%8d%e9%ba%b5',
        #  'hit': 177, 'created_at': 1581153851,
        #  'images_url': ['https://pic.pimg.tw/cw980374/1581155315-4007497404_n.jpg',
        #                 'https://pic.pimg.tw/cw980374/1581155353-236356311_n.jpg',
        #                 'https://pic.pimg.tw/cw980374/1581155353-3689782169_n.jpg'], 'reply_count': 0,
        #  'tags': ['忠孝敦化', '穗科手打烏龍麵忠孝店', '手打烏龍麵'], 'video': {}}
        article_type.append(each_element['type'])
        print('type : ', each_element['type'])


        article_title.append(each_element['title'])
        print('title : ', each_element['title'])

        each_article_url = each_element['link']
        article_url.append(each_article_url)
        print('網址 : ', each_article_url)

        #         print('圖檔 : ',each_element['images_url'])  #每篇最多3張圖片

        tags.append(each_element['tags'])
        print('tags : ', each_element['tags'])  # 不包含搜尋的關鍵字: 台北


        #         #解決請求速度過快導致程序報錯
        #         while 1:

        #             try:
        #                 # 針對列表的文章進行文字的爬取
        response = ss.get(each_article_url, headers=headers)
        print(response)
        time.sleep(random.randint(3, 8))
        response.encoding = 'utf-8'

        #             except:

        #                 print("Connection refused by the server..")
        #                 print("Let me sleep for 5 seconds")
        #                 print("ZZzzzz...")
        #                 time.sleep(10)
        #                 print("Was a nice sleep, now let me continue...")

        #                 continue

        # 使用xpath解析網頁
        new_res = etree.HTML(response.text)

        classifi_in_each_article_url = new_res.xpath('//*[@id="article-box"]/div/div[2]/ul/li[1]/a//text()')  # 全站分類

        jpg_in_each_article_url = new_res.xpath('//*[@id="article-content-inner"]//p//img/@src')  # jpg
        #         //*[@id="article-content-inner"]/p//img//@src

        content_in_each_article_url = new_res.xpath('//*[@id="article-content-inner"]//p//text()')  # 內文

        # 每篇的: 全站分類
        for j, text22 in enumerate(classifi_in_each_article_url):
            classifi_in_each_article_url[j] = text22.strip()  #.strip() 刪除頭尾空格


        T = ''.join(classifi_in_each_article_url)
        blogg.append(T)
        print(T)

        # 每篇的jpg
        for j, text22 in enumerate(jpg_in_each_article_url):
            jpg_in_each_article_url[j] = text22.strip()

        J = jpg_in_each_article_url
        jpgg.append(J)
        print(J)

        # 簡單的資料清洗 (print出內文)
        for j, text22 in enumerate(content_in_each_article_url):
            # print(text22)
            # 稻荷餐飲集團
            #  的特色為日式、職人手作
            # 其子品牌包括
            # 「
            # 一禾堂麵包本舖
            # 」
            # 、
            # 「元禾食堂」、
            #  
            # 「穗科食堂」
            #  

            content_in_each_article_url[j] = text22.strip() #.strip() 去除每行文字的頭尾空格


        article = ''.join(content_in_each_article_url)  #變成文字緊緊相連的文章

        articlee.append(article)
        print(article)
        #
        print('================================')