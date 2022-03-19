# python 取出 Mongdb 中的數據 轉化成DataFrame 然後用pandas處理數據
# 剛開始是用的一個比較麻煩的轉化================================
import pandas as pd
from pymongo import MongoClient

client = MongoClient('192.168.1.XXX', 10070)

db = client.dbtest

collection=db.data_table
items = collection.find()

dateId = []
ai_type = []
ai_name = []
quorum = []
priceUSD = []
ai_disageform = []
country = []
continent  = []
company = []
ai_cap_tr = []
n = 0
for i in items:
     n= n+1
     print("正在輸出 %s 條"%n)
     keys = i.keys()
     if 'ai_disageform' in keys:
         ai_disageform.append(i['ai_disageform'])
     else:
         ai_disageform.append('')
     if 'date' in keys:
         t = str(i['date'])
         dateId.append(t[:10])
     else:
         dateId.append('')
     if 'ai_type' in keys:
         ai_type.append(i['ai_type'])
     else:
         ai_type.append('')
     if 'continent' in keys:
         continent.append(i['continent'])
     else:
         continent.append('')
     if 'quorum' in keys:
         quorum.append(i['quorum'])
     else:
         quorum.append('')
     if 'priceUSD' in keys:
         priceUSD.append(i['priceUSD'])
     else:
         priceUSD.append('')
     if 'country' in keys:
         country.append(i['country'])
     else:
         country.append('')
     if 'ai_name' in keys:
         ai_name.append(i['ai_name'])
     else:
         ai_name.append('')
     if 'company' in keys:
         company.append(i['company'])
     else:
         company.append('')
     if 'ai_cap_tr' in keys:
         ai_cap_tr.append(i['ai_cap_tr'])
     else:
         ai_cap_tr.append('')

df = pd.DataFrame({'dateId':dateId,
                   'ai_type':ai_type,
                   'ai_name':ai_name,
                   'quorum':quorum,
                   'priceUSD':priceUSD,
                   'ai_disageform':ai_disageform,
                   'country':country,
                   'continent':continent,
                   'ai_cap_tr':ai_cap_tr,
                   'company':company})

df.to_csv('../ncbdata/b.csv', encoding = "utf-8",index=None)

# 將每一個字典放到一個數組裡，然後通過read_json() 方法轉化為df對象 ======================
import pandas as pd
import numpy as np
import pymongo
from pymongo import MongoClient
import json

# 連接mongodb
def connectMongdb():

    client = MongoClient('192.168.1.XXX',10070)

    db = client.dbtest

    collection = db.data_table
    items = collection.find()
    return items

# 轉化為df
def tran_df():
    items = connectMongdb()
    temp = []
    for dict in items:
        del dict['_id']
        dict['date'] = dict['date'].strftime("%Y-%m-%d")
        temp.append(dict)
    data_employee = pd.read_json(json.dumps(temp))
    data_employee_ri = data_employee.reindex(columns=['date', 'ai_type', 'ai_name'])
    data_employee_ri.to_csv('data/a.csv')


def main():
    tran_df()

if __name__ == "__main__":
    main()


import pandas as pd
from pymongo import MongoClient

#1. get data from mongodb
class extra_yunnan_hotel(object):
    def get_yunnan_hotel(self):
        client = MongoClient('192.168.1.XXX', 27017)
        db=client.gaode_pois
        data2=db.gaode_pois_hotel_yunnan_extra_mid01.find({},{"_id":0,'name':1,'lng':1,'lat':1}).limit(10)
        # 創建一個空的dataframe
        df = pd.DataFrame(columns = ["_id", "name", "lng", "lat"])
        for x in data2:
            # dict轉成dataframe,注意.T的運用
            pd_data=pd.DataFrame.from_dict(x,orient='index').T
            # 插入df，忽略索引
            df=df.append(pd_data, ignore_index=True)
df.to_csv('_id_name_lng_lat2.csv',sep='\t',encoding='utf-8')

# 執行
start=extra_yunnan_hotel()
start.get_yunnan_hotel()

from pymongo import MongoClient
from bson.objectid import ObjectId

# 以下需分別輸入用戶名、密碼、host、port等參數
client = MongoClient("mongodb://用戶名:密碼@host:port")

db = client.hwtwlog
collection = db.hw_gamelog_Chat
collection.stats
post2 = collection.find_one({'_id': ObjectId("輸入ObjectId")})

for m in collection.find():
    print(m)