# 連接mysql取數據方法 ========================================================
# 需要先建立sql連接，有兩個模組可以建立連接
# 1.用sqlalchemy構建數據庫鏈接 ================================
import pandas as pd
from sqlalchemy import create_engine

"""
依據日常的工作需求，對數據的操作可以分為如下幾類：
1、數據查詢：從數據庫中提取數據，如：select * from test_table where col_a ='a'
2、數據導入：將excel 或者其他類的數據，導入數據庫中
3、創建、修改和刪除：create test_table... ，update test_table ...，delete test_table...
"""

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


# 2.用DBAPI構建數據庫鏈接 ====================================
import pandas as pd
import pymysql

# sql 命令
sql_cmd = "SELECT * FROM table"

# 用DBAPI構建數據庫鏈接engine
con = pymysql.connect(host=localhost, user=username, password=password, database=dbname, charset='utf8', use_unicode=True)
df = pd.read_sql(sql_cmd, con)

# 用模組創建完連接engine後，會用pandas中的read_sql函數來取數據，以下為各參數說明 ================================
import pandas
pandas.read_sql(sql, con, index_col=None, coerce_float=True, params=None, parse_dates=None, columns=None, chunksize=None)

# sql:SQL命令字符串
# con：連接sql數據庫的engine，一般可以用SQLalchemy或者pymysql之類的包建立
# index_col: 選擇某一列作為index
# coerce_float:非常有用，將數字形式的字符串直接以float型讀入
# parse_dates:將某一列日期型字符串轉換為datetime型數據，與pd.to_datetime函數功能類似。可以直接提供需要轉換的列名以默認的日期形式轉換，也可以用字典的格式提供列名和轉換的日期格式，比如{column_name: format string}（format string："%Y:%m:%H: %M:%S"）。
# columns:要選取的列。一般沒啥用，因為在sql命令裡面一般就指定要選擇的列了
# chunksize：如果提供了一個整數值，那麼就會返回一個generator，每次輸出的行數就是提供的值的大小。
