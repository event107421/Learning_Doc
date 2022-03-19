# time模組是包含各方面對時間操作的函式. 儘管這些常常有效但不是所有方法在任意平臺中有效
import time

# 返回一個時間戳(預設是當時時間)
print(time.time())

# 轉換gmtime()和localtime()返回的元組或struct_time為string.
print(time.asctime(time.gmtime()))

# 在第一次呼叫的時候, 返回程式執行的時間. 第二次之後返回與之前的間隔.
print(time.clock())

# 將時間戳轉換為時間字串, 如沒有提供則返回當前的時間字串,並與asctime(localtime())一樣.
print(time.ctime())

# 執行緒推遲指定時間, 以秒為單位
print(time.sleep(1))

# 將時間戳轉化為, UTC 時區的struct_time.
print(time.gmtime())

# 類似gmtime()但會把他轉換成本地時區.
print(time.localtime())

# struct_time 轉化為時間戳.
print(time.mktime(time.localtime()))

# 根據引數轉換一個sturc_time或元組為字串.
print(time.strftime('%Y-%m-%d', time.localtime()))

# 與strftime相反,返回一個struct_time.
print(time.strptime('2021-04-23', '%Y-%m-%d'))

# time模組中常用的格式化字串
# %y 兩位數的年份 00 ~ 99.
# %Y 四位數的年份 0000 ~ 9999
# %m 月份 01 ~ 12.
# %d day 01 ~ 31.
# %H 時 00 ~ 23.
# %I 時 01 ~ 12.
# %M 分 00 ~ 59.
# %S 秒 00 ~ 61.