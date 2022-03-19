"""
我們再上一篇做了pandas實現資料選取、篩選、分組、合併等介紹
接下來我們就該來學習資料載入的部分
pandas 可以支援多種文字、二進位檔案與資料庫的資料載入，常見的 txt、csv、excel 試算表、MySQL 或 PostgreSQL 都難不倒，如果對詳細的內容有興趣，可以參考 pandas 0.21.0 documentation
"""

# 首先我們先將pandas及numpy讀進來，以及等等會用到的glob套件
import pandas as pd
import numpy as np
import glob

# 接著我們嘗試讀取幾個檔案格式
"""
CSV檔
相信大家在做資料分析很常用到csv的檔案格式，且檔案存在自己電腦的某個路徑中就可以用以下方法進行讀取
"""

df=pd.read_csv('路徑\data.csv')
print('用read_csv讀取的csv文檔：', df)

"""
但是這邊須注意一點，如果路徑或是檔案名稱有中文，pandas的read_csv這個函數會跳錯誤，如下列訊息

                        OSError: Initializing from file failed

會出錯主要是因為read_csv內有一個engine參數，默認是C engine，在讀取中文標題可能會出錯，所以將engine轉換成python即可(官方文檔是說C engine速度更快，但python engine功能比較完善)在這邊提供大家兩個方法
"""

# 第一個方法就是像剛剛所說明的將engine改成python即可
df = pd.read_csv('路徑\data.csv', engine='python')
print('用read_csv讀取的csv文檔：', df)

# 第二個方法就是先用open函數，將檔案先打開後讀取
o = open('路徑\data.csv', 'r')
df = pd.read_csv(o)
o.close
print('用read_csv讀取的csv文檔：', df)

# 如果大家的csv檔是還沒下載的，類似存在雲端上或是下載網址，也可以直接進行讀取
csv_file = "網址/檔名.csv"
data = pd.read_csv(csv_file)
print(data)

"""
我們這邊稍微講解一下read_csv較常用到的參數
sep：str, default ‘,’

指定分隔符號，如果不指定參數，則會嘗試使用逗號分隔。
header：int or list of ints, default ‘0’
指定哪一列用來作為欄位名，默認第0列，如果檔案內沒有欄位名則可以改成None。

encoding : str, default None
指定編碼類型，默認是None，通常會指定為'utf-8'

其他的read_csv內詳細參數可以參考以下網址
https://blog.csdn.net/zhangjianjaEE/article/details/78543743
"""

# 相信大家有的時候可能會在本機中有多個csv檔案，總不可能一個一個讀取進來，這個時候我們可以配合剛剛已經import進來的glob這個套件來達成這個目標

# 資料夾名稱
path =r'資料夾路徑'

#用glob套件可以返回所有匹配的文件路徑列表
allFiles = glob.glob(path + "/*.csv")

# 創造一個空的dataframe、一個空的list，之所以創一個空的list是可以先將讀進來的檔案全部先利用append函數加在list內，最後再用pandas的concat進行資料集的合併
frame = pd.DataFrame()
list_ = []
for file_ in allFiles:
    o=open(file_)
    df = pd.read_csv(o, header=0)
    list_.append(df)

#合併所有list
frame = pd.concat(list_)

"""
另外在這邊說明，read_csv、read_table兩個函數的差別在於
pandas.read_csv()

從文件、URL、文件型對像中加載帶分隔符的數據。默認分隔符為'',"
pandas.read_table()

從文件、URL、文件型對像中加載帶分隔符的數據。默認分隔符為"\t"
"""

# excel檔
xlsx_file = "網址/檔名.xlsx"
data = pd.read_excel(xlsx_file)
print(data)

# excel檔從本機讀取檔案與csv檔方法一樣，這邊就不多加贅述

"""
html表格資料
相信有些人都有用過BeautifulSoup進行網站資料的撈取，那pandas也有提供一個函數，讓你可以擷取網頁上表格資料
那我們用StockQ.org 上的股市資料來進行示範
"""

import pandas as pd
url = 'http://www.stockq.org/market/asia.php'
table = pd.read_html(url)

# 這部分可能會出現錯誤，可能是lxml的套件問題
import error lxml not found please install it

# 以防萬一我們安裝以下兩個套件，就可以執行了
pip3 install html5lib
pip3 install beautifulsoup4

# 這個網頁上有多個表格，而我們關注的股市資料放在第五個表格中，因此下指令 拿到第五個表格的資料，再來用 drop 指令把不要的 Row 與 Column 丟掉
import pandas as pd
url = 'http://www.stockq.org/market/asia.php'
table = pd.read_html(url)[4]
table = table.drop(table.columns[[0,1,2,3,4]],axis=0)
table = table.drop(table.columns[9:296],axis=1)
table
