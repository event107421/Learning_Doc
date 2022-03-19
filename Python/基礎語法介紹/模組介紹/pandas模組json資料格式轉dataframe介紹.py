# -*- coding: UTF-8 -*-
from pandas.io.json import json_normalize
import pandas as pd
import json
import time

# pandas 解析json文件為DataFrame的三種方式以及其靈活度和效率的比較
# 利用pandas自帶的read_json直接解析字符串
# 利用json的loads和pandas的json_normalize進行解析
# 利用json的loads和pandas的DataFrame直接構造(這個過程需要手動修改loads得到的字典格式)
 
# 讀入數據
data_str = open('data.json').read()
print(data_str)
 
# 測試json_normalize
start_time = time.time()
for i in range(0, 300):
    data_list = json.loads(data_str)
    df = json_normalize(data_list)
end_time = time.time()
print(end_time - start_time)
 
# 測試自己構造
start_time = time.time()
for i in range(0, 300):
    data_list = json.loads(data_str)
    data = [[d['timestamp'], d['value']] for d in data_list]
    df = pd.DataFrame(data, columns=['timestamp', 'value'])
end_time = time.time()
print(end_time - start_time)
 
#  測試read_json
start_time = time.time()
for i in range(0, 300):
    df = pd.read_json(data_str, orient='records')
end_time = time.time()
print(end_time - start_time)