
import urllib.request
from queue import Queue

import requests

from Crawl_Data.link_finder import LinkFinder
from Crawl_Data.detail_page import DetailPage
from Crawl_Data.get_data import GetData
from bs4 import BeautifulSoup

import pandas as pd
from Crawl_Data.domain import *





def crawl_page(data, queue, crawled , base_url, page_url):
    if page_url not in crawled:
        print('\n'  'Now crawling ' + page_url)
        gather_link(data, queue, crawled ,base_url,page_url)
        queue.remove(page_url)
        crawled.add(page_url)
        print('Queue ' + str(len(queue)) + ' | Crawled ' + str(len(crawled)))

def gather_link(data, queue, crawled, base_url,page_url):

    #options = webdriver.ChromeOptions();
    #options.add_argument("headless");
    #driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    #driver.get(page_url)
    #content = driver.page_source
    #html_string = BeautifulSoup(content, "lxml")
    #html_string.decode('utf-8')

    html_content = requests.get(page_url).text
    html_string = BeautifulSoup(html_content, "lxml")
    html_string.decode('utf-8')

    finder = LinkFinder(base_url, page_url)
    finder.feed(str(html_string))

    detail = DetailPage(base_url)
    detail.feed(str(html_string))
    print(detail.detail_links())
    print(len(detail.detail_links()))


    add_link_to_queue(queue,crawled,base_url,finder.page_link())
    add_data(data, detail.detail_links())



def add_link_to_queue(queue, crawled, base_url, links):
    for url in links:
        if url in queue:
            continue
        if url in crawled:
            continue
        if get_domain_name(base_url) not in url:
            continue
        queue.add(url)

def add_data(data, detail_pages):

    global i
    i = 1
    for link in detail_pages:
        response = urllib.request.urlopen(link)
        html_bytes = response.read()
        html_string = html_bytes.decode('utf-8')
        d = GetData()
        d.feed(str(html_string))
        data.loc[i] = d.return_data()
        i = i+1


i =1
queue = set()
crawled = set()
QUEUE = Queue()
col = ['Giá', 'DT', 'Đường', 'Phường-Xã', 'Quận-Huyện', 'Thành Phố', 'Hướng', 'Phòng ăn', 'Loại tin',
               'Đường trước nhà', 'Nhà bếp', 'Loại BDS', 'Pháp lý', 'Sân thượng', 'Chiều ngang', 'Số lầu',
               'Chổ để xe hơi', 'Chiều dài', 'Số phòng ngủ', 'Chính chủ']
data = pd.DataFrame(columns=col)

'''
crawl_page(data, queue, crawled , 'https://alonhadat.com.vn/', 'https://alonhadat.com.vn/nha-dat/can-ban/nha-dat/2/ho-chi-minh/trang--15.html')

print(data)
print(queue)
print(crawled)
'''
#######

url = 'https://alonhadat.com.vn/nha-dat/can-ban/nha-dat/2/ho-chi-minh/trang--2.html'
base_url = 'https://alonhadat.com.vn/'
QUEUE.put(url)
i =1
count = 1
while QUEUE.qsize() > 0 and count <= 300:
    page_url = QUEUE.get()
    if page_url not in crawled:
        print('Now crawling '+ page_url)

        #options = webdriver.ChromeOptions();
        #options.add_argument("headless");
        #driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        #driver.get(page_url)
        #content = driver.page_source
        #html_string = BeautifulSoup(content, "lxml")
        #html_string.decode('utf-8')

        html_content = requests.get(page_url).text
        html_string = BeautifulSoup(html_content, "lxml")
        html_string.decode('utf-8')

        finder = LinkFinder(base_url, page_url)
        finder.feed(str(html_string))
        page_link = finder.page_link()


        detail = DetailPage(base_url)
        detail.feed(str(html_string))
        detail_link = detail.detail_links()

        add_link_to_queue(queue, crawled, base_url, page_link)
        #queue.remove(page_url)
        crawled.add(page_url)
        print('Queue ' + str(len(queue)) + ' | Crawled ' + str(len(crawled)))

        for link in queue:
            QUEUE.put(link)

        #print(detail_link)
        #print(len(detail_link))


        for link in detail_link:
            response = urllib.request.urlopen(link)
            html_bytes = response.read()
            html_string = html_bytes.decode('utf-8')
            d = GetData()
            d.feed(str(html_string))
            if len(d.return_data()) == data.shape[1]:
                data.loc[i] = d.return_data()
                i = i + 1

        count = count + 1

new_col = ['Đường', 'Phường-Xã', 'Quận-Huyện', 'Thành Phố', 'Giá', 'Loại tin', 'Loại BDS', 'Chính chủ',
                   'Pháp lý', 'DT', 'Chiều ngang', 'Chiều dài', 'Số lầu', 'Số phòng ngủ', 'Hướng', 'Đường trước nhà',
                   'Phòng ăn', 'Nhà bếp', 'Sân thượng', 'Chổ để xe hơi']
data = data.reindex(columns=new_col)

#data = data.reindex(columns=new_col)
#print(QUEUE.qsize())
print(data)
data.to_csv('Data.csv', encoding='utf-8-sig')

















