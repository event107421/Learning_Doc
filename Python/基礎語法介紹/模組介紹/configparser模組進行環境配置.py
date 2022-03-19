import configparser
# 創建一個環境配置檔案config.ini，檔案內容如下：
"""
[user1]
user_ip = 127.0.0.1
user_name = testuser1
user_id = 00

[user2]
user_ip = 127.0.0.2
user_name = testuser2
user_id = 41
"""

# 讀取環境配置檔案 ======================================================================================================
cf = configparser.ConfigParser()
# 讀取配置檔案，如果寫檔案的絕對路徑，就可以不用os模組
cf.read("C:/Users/bill/Downloads/config.ini")
# 獲取檔案中所有的section(一個配置檔案中可以有多個配置，如資料庫相關的配置，郵箱相關的配置， 每個section由[]包裹，即[section])，並以列表的形式返回
secs = cf.sections()
print(secs)

# 獲取某個section名為user1所對應的鍵
options = cf.options("user1")
print(options)

# 獲取section名為user1所對應的全部鍵值對
items = cf.items("user1")
print(items)

# 獲取user1中user_name對應的值
name = cf.get("user1", "user_name")
print(name)

# 改寫配置檔案 ==========================================================================================================
import configparser

conf = configparser.ConfigParser()
filename = "C:/Users/bill/Downloads/config.ini"
conf.read(filename)
#改user1
node = "user1"
key = "user_id"
value = "00"
conf.set(node, key, value)
# 把檔案開啟為寫入模式
fh = open(filename, 'w')
# 把要修改的節點的內容寫到檔案中
conf.write(fh)
# 把檔案關閉
fh.close()

# 刪除section =============================================================================================================
# 刪除user1分組的user_ip
conf.remove_option('user1', 'user_ip')
# 刪除配置檔案中user1分組（會將整個user1下的ip,id,name都刪除）
conf.remove_section('user1')