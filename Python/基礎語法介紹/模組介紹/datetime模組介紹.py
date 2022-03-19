# datetime模組提供對於日期和時間進行簡單或複雜的操作
import datetime

# datetime模組中datetime類 ======================================================
# 返回當前本地datetime.隨著 tzinfo None
print(datetime.datetime.today())

# 返回當前本地日期和時間
print(datetime.datetime.now())

# 也可以指定時間，如2008/12/5 23:59:59
today = datetime.datetime(2008, 12, 5, 23, 59, 59)

# 根據時間戳返回本地的日期和時間，可指定時區
t = datetime.time()
print(t)
print(datetime.datetime.fromtimestamp(t))

# 根據date和time返回一個新的datetime
a = datetime.date(2015, 4, 21)
b = datetime.time(14, 13, 34)
print(datetime.datetime.combine(a, b))

# timedelta表達兩個date,time和datetime持續時間內的差異.
a = datetime.timedelta(days=7)
b = datetime.datetime.now()

print(a)
print(b - a)

# datetime 也可以這樣做加減，一次加一秒
x = datetime.timedelta(seconds=1)
y = datetime.date(2008, 12, 5, 23, 59, 59)
w = x + y

# 一次加 23小時 59分 59秒
x = datetime.timedelta(hours=23, minutes=59, seconds=59)
w = w + x

# 獲取當前時間
theTime = datetime.datetime.now()

# 定義獲取時間格式，格式為：年-月-日 時：分：秒，毫秒
ISOTIMEFORMAT = '%Y-%m-%d %H:%M:%S,f'
theTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)

# 毫秒的取位问题
ISOTIMEFORMAT_F = '%f'
f_time1 = datetime.datetime.now().strftime(ISOTIMEFORMAT_F)
f_time2 = f_time1[:3]

# datetime模組中date類 ======================================================
# 返回當前的本地日期
print(datetime.date.today())

# 根據提供的時間戳返回local date. 時間戳常用於對時間型別的儲存
print(datetime.date.fromtimestamp(1619145489))

d = datetime.date(2021, 4, 21)
# 根據提供的日期，返回所需日期部分
# date.min: 返回 date(MINYEAR, 1, 1).
# date.max: 返回 date(MAXYEAR, 12, 31).
# date.year: 返回 年, MINYEAR和MAXYEAR之間
# date.month: 返回 月, 1到12月之間
# date.day: 返回 1到 n 之間.
print(d.min, d.max, d.year, d.month, d.day)

# 返回一個相同值的data物件, 除了這些引數給關鍵字指定新的值
print(d.replace())
print(d.replace(day=22))

# 返回一個time.struct_time物件
print(d.timetuple())

# 返回一個Gregoian Calendar物件
print(d.toordinal())

# 返回day of the week. 星期一為0,星期日為6.
print(d.weekday())

# 返回day of the week. 星期一為1,星期日為7
print(d.isoweekday())

# 返回 一個’YYYY-MM-DD’的字串格式
print(d.isoformat())

# 返回一個三元組, (ISO year, ISO week number, ISO weekday)
print(d.isocalendar())

# 返回一個字串日期, d.ctime() 等同於 time.ctime(time.mktime(d.timetuple()))
print(d.ctime())

# 返回一個字串日期, 格式自定義
print(d.strftime('%d/%m/%Y'))

# 獲取某月的日曆
import calendar

cal = calendar.month(2016, 1)
print("以下輸出2016年1月份的日曆:")
print(cal)