
import urllib.request
from _csv import writer
from queue import Queue

import requests

from Crawl_Data.link_finder import LinkFinder
from Crawl_Data.detail_page import DetailPage
from Crawl_Data.get_data import GetData
from bs4 import BeautifulSoup

import pandas as pd
from Crawl_Data.domain import *
from Crawl_Data.general import *


def add_link_to_queue(queue, crawled, base_url, page_link):
    for url in page_link:
        if url in queue:
            continue
        if url in crawled:
            continue
        if get_domain_name(base_url) not in url:
            continue
        queue.add(url)

def update_file(queue, crawled, queue_file, crawled_file):
    set_to_file(queue, queue_file)
    set_to_file(crawled, crawled_file)
    #data.to_csv(data_file, encoding='utf-8-sig')








project_name = "DataScience"
url = 'https://alonhadat.com.vn/nha-dat/can-ban/nha-dat/2/ho-chi-minh/trang--2.html'
base_url = 'https://alonhadat.com.vn/'

# Tạo project (nếu chưa có)
create_project_direction(project_name)
create_data_files(project_name, url)

# Đọc lại files để bắt đầu/tiếp tục crawl
queue = file_to_set(project_name+"/queue.txt")
crawled = file_to_set(project_name + '/crawled.txt')
#data = pd.read_csv(project_name+'/data.csv')

col = ['Giá', 'DT', 'Đường', 'Phường-Xã', 'Quận-Huyện', 'Thành Phố', 'Hướng', 'Phòng ăn', 'Loại tin',
               'Đường trước nhà', 'Nhà bếp', 'Loại BDS', 'Pháp lý', 'Sân thượng', 'Chiều ngang', 'Số lầu',
               'Chổ để xe hơi', 'Chiều dài', 'Số phòng ngủ', 'Chính chủ']
data = pd.DataFrame(columns=col)

QUEUE = Queue()
for link in queue:
    QUEUE.put(link)


i = 1
count = 1
while QUEUE.qsize() > 0 and count <= 2:
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
        crawled.add(page_url)
        queue.remove(page_url)
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
                #d.return_data().insert(i, 0);
                with open('data.csv', 'a', encoding='utf-8-sig') as f:
                    w = writer(f)
                    w.writerow(d.return_data())

                    #data.to_csv(f, header=False)

                data.loc[i] = d.return_data()
                i = i + 1

        count = count + 1

        update_file(queue, crawled, project_name+"/queue.txt", project_name+"/crawled.txt" )

new_col = ['Đường', 'Phường-Xã', 'Quận-Huyện', 'Thành Phố', 'Giá', 'Loại tin', 'Loại BDS', 'Chính chủ',
                   'Pháp lý', 'DT', 'Chiều ngang', 'Chiều dài', 'Số lầu', 'Số phòng ngủ', 'Hướng', 'Đường trước nhà',
                   'Phòng ăn', 'Nhà bếp', 'Sân thượng', 'Chổ để xe hơi']
data = data.reindex(columns=new_col)

#data = data.reindex(columns=new_col)
#print(QUEUE.qsize())
print(data)


















