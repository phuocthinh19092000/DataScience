from html.parser import HTMLParser
from urllib import parse


class DetailPage(HTMLParser):

    def __init__(self, base_url):
        super().__init__()
        self.base_url= base_url
        self.data = ''
        self.start_tag = ''
        self.link = ''
        self.links = set()
        self.check = False

    def handle_starttag(self, tag, attrs):
        self.start_tag = tag
        if  tag == 'a' :
            for (attribute, value) in attrs :
                if attribute == 'href':
                    self.link = parse.urljoin(self.base_url, value)
                    self.check = True



    def handle_data(self, data):
        if self.check == True:
            self.data = data
        self.check = False

    def handle_endtag(self, tag):
        if self.data == '<< xem chi tiết >>' and self.start_tag == 'a' and tag == 'a':
            self.links.add(self.link)
        self.data = ''
        self.link = ''



    def detail_links(self):
        return self.links

    def error(self, message):
        pass


''''
options = webdriver.ChromeOptions();
options.add_argument("headless");
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get(
    'https://alonhadat.com.vn/nha-dat/can-ban/nha-dat/2/ho-chi-minh/trang--3.html')
content = driver.page_source
html_string = BeautifulSoup(content, "lxml")
html_string.decode('utf-8')'''

''''
html_content = requests.get('https://alonhadat.com.vn/nha-dat/can-ban/nha-dat/2/ho-chi-minh/trang--32.html').text
soup = BeautifulSoup(html_content, "lxml")
soup.decode('utf-8')

a = DetailPage('https://alonhadat.com.vn/')
a.feed(str(soup))
#print(a.detail_links())
#print(len(a.detail_links()))


col = ['Giá', 'DT','Đường', 'Phường-Xã', 'Quận-Huyện', 'Thành Phố', 'Hướng', 'Phòng ăn', 'Loại tin', 'Đường trước nhà', 'Nhà bếp',  'Loại BDS',  'Pháp lý',  'Sân thượng',  'Chiều ngang',  'Số lầu',  'Chổ để xe hơi',  'Chiều dài', 'Số phòng ngủ', 'Chính chủ']
dataFrame = pd.DataFrame(columns=col)

i = 1
for link in a.detail_links():
    response = urllib.request.urlopen(link)
    html_bytes = response.read()
    html_string = html_bytes.decode('utf-8')
    data = GetData()
    data.feed(str(html_string))
    dataFrame.loc[i] = data.return_data()
    i = i+1


new_col = ['Giá','Đường', 'Phường-Xã', 'Quận-Huyện', 'Thành Phố', 'Loại tin', 'Loại BDS', 'Chính chủ', 'Pháp lý', 'DT', 'Chiều ngang' ,'Chiều dài', 'Số lầu', 'Số phòng ngủ', 'Hướng', 'Đường trước nhà',  'Phòng ăn',  'Nhà bếp',  'Sân thượng', 'Chổ để xe hơi']
dataFrame=dataFrame.reindex(columns = new_col)
print(dataFrame)'''