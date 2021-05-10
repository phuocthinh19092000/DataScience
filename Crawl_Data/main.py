import threading
from queue import Queue

from Crawl_Data.crawl_data import CrawlData
from Crawl_Data.domain import *

PROJECT_NAME = 'thenewboston'
HOMEPAGE = 'https://alonhadat.com.vn/nha-dat/can-ban/nha-dat/2/ho-chi-minh/trang--6.html'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
print(DOMAIN_NAME)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()
CrawlData(HOMEPAGE, DOMAIN_NAME)

COUNT = 0
#Create threads
def create_workers():
    for _ in range (NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

# Do the next job in the queue
def work():
    while True:
        url = queue.get()
        CrawlData.crawl_page(url)
        queue.task_done()


# Each queue link is a new job
def create_job():
    for link in CrawlData.queue:
        queue.put(link)
    queue.join()
    crawl()



# Check if there are item in the queue, if so crawl them
def crawl():
    queue_links = CrawlData.queue
    if len(queue_links) > 0:
        print(str(len(queue_links))+ ' links in the queue' )
        create_job()



create_workers()
crawl()










