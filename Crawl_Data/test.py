from _csv import writer

import pandas as pd



d = ['Hồ Chí Minh', 'Hà NỘi', 'đà nẵng 123', '12']
col = ['1', '2', '4', '3']
df = pd.DataFrame(columns=col)

df1 = pd.DataFrame(columns=col)
df1.loc[1] = col
df1.loc[2] = d

#df.to_csv("test.csv", index=True, encoding='utf-8-sig')
#df1.to_csv('test.csv', mode='a', header=False, encoding='utf-8-sig')
with open('test.csv', 'a', encoding='utf-8-sig') as f:
    w = writer(f)
    w.writerow(d)





print(df)













