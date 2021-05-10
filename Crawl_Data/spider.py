
import urllib.request

from Crawl_Data.link_finder import LinkFinder
from Crawl_Data.general import *
from Crawl_Data.detail_page import DetailPage
from Crawl_Data.get_data import GetData
from bs4 import BeautifulSoup

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import pandas as pd
class Spider:

    #Class variables (share among all instances)
    project_name = ''
    base_url = ''
    domain_name = ''
    data_file = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()
    data = pd.DataFrame()
    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name +'/queue.txt'
        Spider.crawled_file = Spider.project_name+'/crawled.txt'
        Spider.data_file = Spider.project_name+'/data.csv'
        self.boot()
        self.crawl_page('First spider', Spider.base_url)


    @staticmethod
    def boot():
        create_project_direction(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)
        col = ['Giá', 'DT', 'Đường', 'Phường-Xã', 'Quận-Huyện', 'Thành Phố', 'Hướng', 'Phòng ăn', 'Loại tin',
               'Đường trước nhà', 'Nhà bếp', 'Loại BDS', 'Pháp lý', 'Sân thượng', 'Chiều ngang', 'Số lầu',
               'Chổ để xe hơi', 'Chiều dài', 'Số phòng ngủ', 'Chính chủ']
        Spider.data = pd.read_csv(Spider.data_file)
        Spider.data = pd.DataFrame(columns=col)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print('\n'+thread_name + ' now crawling '+ page_url)
            Spider.gather_link(page_url)
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            print('Queue '+ str(len(Spider.queue))+ ' | Crawled ' + str(len(Spider.crawled)))
            Spider.update_file()




    @staticmethod
    def gather_link(page_url):
            html_string  = ''

            #html_content = requests.get(page_url).text
            #soup = BeautifulSoup(html_content, "lxml")
            #soup.decode('utf-8')

            ##############################################

            #response = urllib.request.urlopen(page_url)
            #print("Result code: " +str(response.getcode()))
            #html_bytes = response.read()
            #html_string = html_bytes.decode('utf-8')

            ################################################

            options = webdriver.ChromeOptions();
            options.add_argument("headless");
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
            driver.get(page_url)
            content = driver.page_source
            html_string = BeautifulSoup(content, "lxml")
            html_string.decode('utf-8')

            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(str(html_string))

            detail = DetailPage(page_url)
            detail.feed(str(html_string))
            #print(detail.detail_links())





            Spider.add_data(detail.detail_links())
            Spider.add_link_to_queue(finder.page_link())


    @staticmethod
    def add_data(detail_pages):
        i = 1
        for page in detail_pages:
            response = urllib.request.urlopen(page)
            html_bytes = response.read()
            html_string = html_bytes.decode('utf-8')
            d = GetData()
            d.feed(str(html_string))
            Spider.data.loc[i] = d.return_data()
            i = i + 1
        new_col = ['Đường', 'Phường-Xã', 'Quận-Huyện', 'Thành Phố', 'Giá', 'Loại tin', 'Loại BDS', 'Chính chủ',
                   'Pháp lý', 'DT', 'Chiều ngang', 'Chiều dài', 'Số lầu', 'Số phòng ngủ', 'Hướng', 'Đường trước nhà',
                   'Phòng ăn', 'Nhà bếp', 'Sân thượng', 'Chổ để xe hơi']
        Spider.data = Spider.data.reindex(columns=new_col)



    @staticmethod
    def add_link_to_queue(links):
        for url in links:
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue
            if Spider.domain_name not in url:
                continue
            Spider.queue.add(url)


    @staticmethod
    def update_file():
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)
        Spider.data.to_csv(Spider.data_file, encoding='utf-8-sig')


#p = Spider('thinh', 'https://alonhadat.com.vn/nha-dat/can-ban/nha-dat/2/ho-chi-minh/trang--12.html','alonhadat.com.vn/')
#queue = Queue()

