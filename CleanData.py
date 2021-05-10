# -*- coding: utf-8 -*-
import pandas as pd
import null

# đọc data set vô ở đây
df_dataset = pd.read_csv('Data/Data.csv', encoding='utf-8-sig')
# Clean data

# xu li dien tich

Square = df_dataset['DT']
Square1 = []
for square in Square:
    Square1.append(float(square[0]))


# xu li gia tien
Price = df_dataset['Giá']
Price1= []
i = 0
price = Price[i]
area = Square[i]
if 'tỷ' in price:
    replacePrice = price.replace(",", ".")
    changeToMoney = float(replacePrice[:replacePrice.find('t') - 1]) * 1000000000
    Price1.append(changeToMoney)
elif '/ m2' in price:
    replacePrice = price.replace(",", ".")
    changeToMoney = float(
        replacePrice[:replacePrice.find('t') - 1]) * 1000000 * int(Square[:area.find('m') - 1])
    Price1.append(changeToMoney)
else:
    changeToMoney = float(price[:price.find('t') - 1]) * 1000000
    Price1.append(changeToMoney)



# xu li huong
Direction = df_dataset['Hướng']
Direction1 = []
for direction in Direction:
    if direction == '_':
        Direction1.append("")
    else:
        Direction1.append(direction)




# xu li phong an
phongan = df_dataset['Phòng ăn']
phongan1 = []

for pa in phongan:
    if pa == '---':
        phongan1.append("")
    else:
        phongan1.append(pa)



# xu li loai tin
loaitin = df_dataset['Loại tin']
duongtruocnha = df_dataset['Đường trước nhà']
duongtruocnha1 = []
for duong in duongtruocnha:
    if duong == '---':
        duongtruocnha1.append("")
    else:
        duongtruocnha1.append(duong[:len(duong)-1])



# xu li nha bep
nhabep = df_dataset['Nhà bếp']
nhabep1 = []
for nb in nhabep:
    if nb=='---':
        nhabep1.append("")
    else:
        nhabep1.append(nb)



# xu li loai bds
loaibds = df_dataset['Loại BDS']



# xu li phap ly
phaply = df_dataset['Pháp lý']
phaply1 = []
for pl in phaply:
    if pl =='---':
        phaply1.append("")
    else:
        phaply1.append(pl)



# xu li san thuong
santhuong = df_dataset['Sân thượng']
santhuong1 = []
for st in santhuong:
    if st =='---':
        santhuong1.append("")
    else:
        santhuong1.append(st)



# xu li chieu ngang
chieungang = df_dataset['Chiều ngang']
chieungang1 = []
for cn in chieungang:
    if cn == '---':
        chieungang1.append("")
    else:
        chieungang1.append(cn[:len(cn)-1])

# xu li so lau

solau = df_dataset['Số lầu']
solau1 = []
for cn in solau:
    if cn == '---':
        solau1.append("")
    else:
        solau1.append(cn)


# xu li cho de xe hoi
parking = df_dataset['Chổ để xe hơi']
parking1 = []
for cn in parking:
    if cn == '---':
        parking1.append("")
    else:
        parking1.append(cn)

# xu li chieu dai
chieudai = df_dataset['Chiều dài']
chieudai1 = []
for cn in chieudai:
    if cn == '---':
        chieudai1.append("")
    else:
        chieudai1.append(cn[:len(cn)-1])

# xu li so phong ngu

sophongngu = df_dataset['Số phòng ngủ']
sophongngu1 = []
for cn in sophongngu:
    if cn == '---':
        sophongngu1.append("")
    else:
        sophongngu1.append(cn)


# xu li chinh chu

chinhchu = df_dataset['Chính chủ']
chinhchu1 = []
for cn in chinhchu:
    if cn == '---':
        chinhchu1.append("")
    else:
        chinhchu1.append(cn)

# xu li duong

duong = df_dataset['Đường']
phuongxa = df_dataset['Phường-Xã']
quanhuyen = df_dataset['Quận-Huyện']
thanhpho = df_dataset['Thành Phố']

# doc vao csv
#
df = pd.DataFrame({'Square': Square1, 'Length': chieudai1, 'Width': chieungang1, 'Road': duongtruocnha1, 'Floor': solau1, 'Bedroom':sophongngu1 ,'Price': Price,'Direction': Direction,'DiningRoom' : phongan1,'Kitchen':nhabep1, 'Legal': phaply1, 'Terrace':santhuong1, 'Garage': parking1, 'Owned':chinhchu1, 'Route':duong, 'Ward':phuongxa, 'District': quanhuyen, 'City' :thanhpho, 'Type Of New': loaitin, 'Type Of Estate':loaibds })
df.to_csv('Data/data1.csv', index=True, encoding='utf-8-sig')
