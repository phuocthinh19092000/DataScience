import urllib
import urllib.request
from html.parser import HTMLParser
from urllib import parse

import null as null
import numpy as np
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import lxml
import pandas as pd


class GetData(HTMLParser):

    def __init__(self):
        super().__init__()
        self.temp = []
        self.check = ''
        self.data = ''
        self.start_tag = ''

    def handle_starttag(self, tag, attrs):
        self.start_tag = tag
        if tag == 'td':
           #for (attribute,value) in attrs:
               #if attribute == 'class':
                     #if value == 'infor':
            self.check = True
        if tag == 'span':
            for (attribute, value) in attrs:
                if attribute == 'class' and value == 'value':
                    self.check = True




    def handle_data(self, data):
        self.data = data
        if self.check == True:
            #if  self.data == '':
                #self.temp.append('OK')
            #else:
             self.temp.append(str(data).strip())
             #print(data)
        self.check = False



    def handle_endtag(self, tag):
        if tag == 'td' and self.data == '':
                self.temp.append('Y')
        self.data = ''


    def return_data(self):
        data = []
        index = [0,1,2,6,8,10,12,14,16,18,20,22,24,26,28,30,32]
        for i in index:


            if i == 2:
                addr = str(self.temp[i]).split(',')
                for j in range(len(addr)):
                    data.append(addr[j])
            else:
                data.append(self.temp[i])
            '''
            if i == 2:
                addr = str(self.temp[2]).split(',')
                if len(addr) == 3:
                    for j in range(len(addr)):
                        data.append(addr[j])
                    data.insert(3,'No Data')
                elif len(addr) == 2:
                    for _ in range(2):
                        data.append('NoData')
                    for j in range(len(addr)):
                        data.append(addr[j])
                else:
                    for j in range(len(addr)):
                        data.append(addr[j])

            else:
                
                data.append(self.temp[i])
                '''

        return data


    def error(self, message):
        pass


'''
options = webdriver.ChromeOptions();
options.add_argument("headless");
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get(
    'https://alonhadat.com.vn/nha-khu-vip-ngay-tan-son-nhi-64m2-2-tang-2-ty-180-trieu-8347206.html')
content = driver.page_source
html_string = BeautifulSoup(content, "lxml")
html_string.decode('utf-8')

a = GetData()
a.feed(str(html_string))
print(a.return_data())
print(len(a.return_data()))

'''

