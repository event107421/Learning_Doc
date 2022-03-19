"""
依據日常的工作需求，對數據的操作可以分為如下幾類：
1、數據查詢：從數據庫中提取數據，如：select * from test_table where col_a ='a'
2、數據導入：將excel 或者其他類的數據，導入數據庫中
3、創建、修改和刪除：create test_table... ，update test_table ...，delete test_table...
"""

import pandas as pd
from sqlalchemy import create_engine

# 創建engine，連接數據庫（此時並沒有真正的連接上數據庫）
# 要輸入的包含：用戶名、密碼、host、port、db_name等參數
engine= create_engine('mysql+pymysql://用戶名:密碼@host:port/db_name?charset=utf8')

# 數據查詢
sql = "select * from test_table;"
data = pd.read_sql(sql, engine)

# 數據導入
data = pd.DataFrame()
table_name = 'test_table'
data.to_sql(table_name, con=engine, index=False, if_exists='append')

# 創建、修改和刪除
sql = "delete from test_table where col_a='a'"
engine.execute(sql)