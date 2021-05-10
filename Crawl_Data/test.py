import pandas as pd

"""""
options = webdriver.ChromeOptions();
options.add_argument("headless");
# 1. Khai báo browser
browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# 2. Mở URL của post
browser.get("https://alonhadat.com.vn/can-ban-nha-ho-chi-minh-t2/trang-47.htm")

sleep(3)

estate_list = browser.find_elements_by_class_name("content-item")

print(estate_list)


for estate in estate_list:
    # hiển thị tên người và nội dung, cách nhau bởi dấu :
    square = estate.find_element_by_class_name("ct_dt")
    KT = estate.find_element_by_class_name("ct_kt")
    price = estate.find_element_by_class_name("price-dis")
    print("*",square.text,",", KT.text,",", price.text)
#
#
# sleep(5)

# 6. Đóng browser
browser.close()
"""

data = {'Name':[],
        'Age':[]}
data1 = {'Name':['jack1'],
        'Age':[11]}
b = [10 , 'hello', 'gấ']
b1  =[10 , 11,10 ]
a1 = pd.DataFrame(columns=b)
a = pd.DataFrame(columns=b)

i = 1
a.loc[i]= b1
a1 = a

#a=a.append(data1,ignore_index=True)
#a=a.append(data1,ignore_index=True)
print(a1)

for i in range(4):
        print("  "+ str(i))
print()












