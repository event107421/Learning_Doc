import pymssql

"""
使用connect建立連線物件
connect.cursor建立遊標物件，SQL語句的執行基本都在遊標上進行
cursor.executeXXX方法執行SQL語句，cursor.fetchXXX獲取查詢結果等
呼叫close方法關閉遊標cursor和資料庫連線
"""

# 創建一個數據庫連接，host是服務器的IP地址，如果是本機可以用"."，user是訪問用戶名，password是密碼，database是資料庫名稱，charset是資料庫的編碼，如果沒設定可能會亂碼
conn = pymssql.connect(host = ".", user = "sa", password = "twinflag", database = "bbs", charset = 'utf8')

""" 
如果和本機資料庫互動,只需修改連結字串 
conn = pymssql.connect(host='.', database='Michael') 
如果出現以下類似的錯誤訊息：
pymssql.OperationalError: (20009, b'DB-Lib error message 20009, severity 9:\nUnable to connect: Adaptive Server is unavailable or does not exist (localhost:1433)\nNet-Lib error during Unknown error (10060)\n')
代表SQL Server中的TCP還沒開啟，此時我們就需要進入SQL Server的組態管理員去進行設定，如下：
1. 從 [Sql Server Configuration Manager] => [SQL Server 網路組態] => [SQLEXPRESS的通訊協定] => [TCP/IP]  中 , 確定 IP位址 127.0.0.1 [已啟用] 且 [使用中] , 然後在 IPAll 的 [TCP通訊埠] 中填入 [1433] .
2. 接著到 [SQL Server 服務] => SQL Server(SQLEXPRESS)點右鍵選重新啟動，讓SQL整個重新啟動後就可以連上了

"""
# 創建遊標對象，相當於ADO的記錄集
cou = conn.cursor()
# 寫SQL查詢語法
sql = "SELECT * FROM table_name"
# 執行命令
cou.execute(sql)

#只有執行了下面的命令，上面的操作才能生效，配合異常處理，可以實現pymssql的事務操作
conn.commit()

"""
如果update/delete/insert記得要conn.commit()，否則會導致資料庫事務無法提交，不能順利的寫入/刪除等等
"""

# 也可以使用for迴圈來迭代查詢結果
# 例子中查詢操作的引數使用的%s而不是'%s'，若引數值是字串，在執行語句時會自動新增單引號
# for row in cou:
#   print("ID=%d, Name=%s" % (row[0], row[1]))
row = cou.fetchone()
while row:
  print("ID = %d, Name = %s" % (row[0], row[1]))
  row = cursor.fetchone()
 
# 插入一條記錄
sql="Insert into user(name) values('admin')"
cou.execute(sql)

# 插入資料操作
cou.executemany(
  "INSERT INTO persons VALUES (%d, %s, %s)",
  [(1, 'John Smith', 'John Doe'),
   (2, 'Jane Doe', 'Joe Dog'),
   (3, 'Mike T.', 'Sarah H.')])

#關閉數據庫的連接
conn.close()

"""
遊標(cursor)使用注意事項
一個連線一次只能有一個遊標的查詢處於活躍狀態，如下：
"""

c1 = conn.cursor()
c1.execute('SELECT * FROM persons')
 
c2 = conn.cursor()
c2.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')
 
print( "all persons" )
print( c1.fetchall() ) # 顯示出的是c2遊標查詢出來的結果
 
print( "John Doe" )
print( c2.fetchall() ) # 不會有任何結果

"""
為了避免上述的問題可以使用以下兩種方式：
建立多個連線來保證多個查詢可以並行執行在不同連線的遊標上
使用fetchall方法獲取到遊標查詢結果之後再執行下一個查詢， 如下：
"""

c1.execute('SELECT ...')
c1_list = c1.fetchall()
 
c2.execute('SELECT ...')
c2_list = c2.fetchall()

"""
使用with語句（上下文管理器）
可以通過使用with語句來省去顯示的呼叫close方法關閉連線和遊標
"""

with pymssql.connect(server, user, password, database) as conn:
 with conn.cursor(as_dict=True) as cursor:
  cursor.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')
  for row in cursor:
   print("ID=%d, Name=%s" % (row['id'], row['name']))
   
# pymssql 2.0.0以上的版本可以通過cursor.callproc方法來呼叫儲存過程
with pymssql.connect(server, user, password, database) as conn:
 with conn.cursor(as_dict=True) as cursor:
  # 建立儲存過程
  cursor.execute("""
  CREATE PROCEDURE FindPerson
   @name VARCHAR(100)
  AS BEGIN
   SELECT * FROM persons WHERE name = @name
  END
  """)
 
  # 呼叫儲存過程
  cursor.callproc('FindPerson', ('Jane Doe',))
  for row in cursor:
   print("ID=%d, Name=%s" % (row['id'], row['name']))
   


# 我們也可以將SQL的數據利用pandas套件來處理
import pandas as pd
# 這裡直接用SQL查詢語法即可
sql = "SELECT * FROM table_name"
# 利用pandas的read_sql函數來做SQL語法的查詢
df0 = pd.read_sql(sql, conn)
df = pd.DataFrame(df0)


