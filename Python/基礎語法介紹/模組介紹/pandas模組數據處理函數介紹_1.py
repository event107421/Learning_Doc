# pandas模組介紹 ========================================
"""
在學資料分析的時候都是習慣使用dataframe的資料格式，那在python就需要用pandas這個套件。
將dictionary的格式轉成pandas，在介紹Pandas之前有許多書籍會提到Numpy，主要原因是因為Pandas背後的數值型態都是Numpy，Numpy的資料結構可以幫助Pandas在執行運算上更有效率以及更省記憶體。
舉例來說Python的內建資料結構list可以塞好幾種不同type的資料進去，如下列程式碼所示，這個list裡面的資料有string, int, float
"""
# Pandas 提供的資料結構
# 1.Series：用來處理時間序列相關的資料(如感測器資料等)，主要為建立索引的一維陣列。
# 2.DataFrame：用來處理結構化(Table like)的資料，有列索引與欄標籤的二維資料集，例如關聯式資料庫、CSV 等等。
# 3.Panel：用來處理有資料及索引、列索引與欄標籤的三維資料集。
import pandas as pd # 引用套件並縮寫為 pd

"""
但對於機器來說，要提升效能或是提升記憶體省用效率最好有一致的型別會比較好。
所以可以使用numpy的array資料結構會強迫把裡面的資料都轉成同一型態
"""
list2 = ["1", 2, 3., 4, 5]

np.array(list2)

# 建立 Series ==========================================
"""
Series欄位
利用pd.Series函式參數放入list即可創建一個簡單的series，使用type就可以看到s1是屬於pandas的series，如果不指定index預設會是0,1,2,3,4…
"""
# 資料可以的類型如下：
# array
# dictionary
# 單一資料

s1 = pd.Series([1, 3, np.nan, 5, 7])
print(type(s1))

# 要指定index的話就在參數那邊多輸入一個list給index參數
s2 = pd.Series([1, 3, np.nan, 5, 7], index = ['a', 'b', 'c', 'd', 'e'])
print(type(s2))

select = pd.Series(data, index = idx) #將資料讀入 series 方法中

# 資料為 Array
cars = ["BMW", "BENZ", "Toyota", "Nissan", "Lexus"]
select = pd.Series(cars)  
print(select) 

# 資料為 Dictionary
dict = {  
    "factory": "Taipei",
    "sensor1": "1",
    "sensor2": "2",
    "sensor3": "3",
    "sensor4": "4",
    "sensor5": "5"
}
select = pd.Series(dict, index = dict.keys()) # 排序與原 dict 相同
# 資料選擇與篩選，可以針對 dict 或是 array 資料透過透過索引值或標籤，挑選出你所要的值
print(select[0])  
print("=====")  
print(select['sensor1'])  
print("=====")  
print(select[[0, 2, 4]])  
print("=====")  
print(select[['factory', 'sensor1', 'sensor3']])
# 資料切片
print(select[:2])  
print("=====")  
print(select['sensor2':]) 

# 資料為單一資料
cars = "BENZ"  
select = pd.Series(cars, index = range(3))  
print(select) 

# 建立 DataFrame ==================================
# DataFrame 用來處理結構化(Table like)的資料，有列索引與欄標籤的二維資料集
"""
DataFrame 表格
我們用np.random.randn產生出一個4*4大小數值為標準常態分佈，並命名欄位名稱依序為a, b, c, d，語法就可以這樣寫
"""

df = pd.DataFrame(np.random.randn(6, 4), columns = ['a', 'b', 'c', 'd'])
print(type(df))

# 資料為 Dictionary
groups = ["Movies", "Sports", "Coding", "Fishing", "Dancing", "cooking"]  
num = [46, 8, 12, 12, 6, 58]

dict = {"groups": groups,  
        "num": num
       }

select_df = pd.DataFrame(dict)
print(select_df)

# 資料為 Array
arr = groups = [["Movies", 46],["Sports", 8], ["Coding", 12], ["Fishing",12], ["Dancing",6], ["cooking",8]]

df = pd.DataFrame(arr, columns = ["name", "num"]) # 指定欄標籤名稱  
print(df)

# 資料描述查看
groups = ["Movies", "Sports", "Coding", "Fishing", "Dancing", "cooking"]  
num = [46, 8, 12, 12, 6, 58]

dict = {"groups": groups,  
        "num": num
        }

select_df = pd.DataFrame(dict)

print(select_df.shape) # 回傳列數與欄數  
print("---")  
print(select_df.describe()) # 回傳描述性統計  
print("---")  
print(select_df.head(3)) # 回傳前三筆觀測值  
print("---")  
print(select_df.tail(3)) # 回傳後三筆觀測值  
print("---")  
print(select_df.columns) # 回傳欄位名稱  
print("---")  
print(select_df.index) # 回傳 index  
print("---")  
print(select_df.info) # 回傳資料內容

# 資料選擇與篩選
groups = ["Movies", "Sports", "Coding", "Fishing", "Dancing", "cooking"]  
num = [46, 8, 12, 12, 6, 58]

dict = {"groups": groups,  
        "num": num
       }

select_df = pd.DataFrame(dict)

print(select_df.iloc[0, 1]) # 第一列第二欄：組的人數  
print("---")  
print(select_df.iloc[0:1,:]) # 第一列：組的組名與人數  
print("---")  
print(select_df.iloc[:,1]) # 第二欄：各組的人數  
print("---")  
print(select_df["num"]) # 各組的人數  
print("---")  
print(select_df.num) # 各組的人數 

# 使用布林值來做篩選
select_df = pd.DataFrame(dict)
out_df = select_df[select_df.loc[:,"num"] > 10] # 選出人數超過 10 的群組  
print(out_df)

# 資料排序
groups = ["Movies", "Sports", "Coding", "Fishing", "Dancing", "cooking"]  
num = [46, 8, 12, 12, 6, 58]

dict = {"groups": groups,  
        "num": num
        }

select_df = pd.DataFrame(dict)

select_df.sort_index(axis = 0, ascending = True) # 透過索引值做排序，axis 可以指定第幾欄，ascending 用於設定升冪或降密
select_df.sort_values(by = 'num') #透過指定欄位的數值排序

# 處理遺漏值 ==============================
#判斷是否為空值
df = pd.read_csv('shop_list2.csv')  
print(df)

# 讀取後放入 DataFrame
select_df = pd.DataFrame(df)

print(select_df.ix[:, "shop name"].isnull()) # 判斷哪些店名是遺失值  
print("---")  
print(select_df.ix[:, "maket size"].notnull()) # 判斷哪些市場規模不是遺失值

# 處理空值
drop_value = select_df.dropna() # 有遺失值的觀測值都刪除  
print(drop_value)  
print("---")  
filled_value = select_df.fillna(0) # 有遺失值的觀測值填補 0  
print(filled_value)  
print("---")  
filled_value_column = select_df.fillna({"shop name": "NULL", "maket size": 0}) # 依欄位填補遺失值  
print(filled_value_column)

# 可以用np.nan創造出NA
height = pd.Series([150, 175, 143, 174, 158])
weight = pd.Series([56, 70, 42, 58, np.nan])

# 那我們接下來使用資料分析內最常用到的範例資料iris，因為iris數據集在sklearn模組內，將他讀出來後，因為她回傳資料格式為dictionary，所以我們再把他轉成dataframe
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

"""
我們可以透過info以及describe來觀看表格的資訊
info主要可以看有幾筆資料、每個欄位的資料型別是什麼(int, float..)、有無空值(null)的存在、佔據多少記憶體
"""

df.info()

# describe主要是看資料的平均值、分佈情況、是否有資料傾斜Skew的問題，描述性統計的呈現
df.describe()

# 若是想取得資料集的欄位名稱直接用columns即可
df.columns

"""
那我們整理一下 pandas 一些好用的屬性與方法可以快速暸解一個 DataFrame 的外觀與內容
df.shape：這個 DataFrame 有幾列有幾欄
df.columns：這個 DataFrame 的變數資訊
df.index：這個 DataFrame 的列索引資訊
df.info()：關於 DataFrame 的詳細資訊
df.describe()：關於 DataFrame 各數值變數的描述統計

這邊我們來說明一下，有些在使用函數時都會看到有些加小括號有些沒有加，這邊說明一下
1.不帶括號時，調用的是這個函數本身
2.帶括號時(可以帶參數也可以不帶參數)，調用的是執行函數後return的結果
"""


# 接下來也可以用sort_values來做資料排序，我們只取排序後前五筆來看
df.sort_values(by = 'sepal length (cm)').head(5)

"""
資料選取
要選取某個欄位可以使用中括號[]，這邊我們一樣只取前五筆
"""

df['sepal length (cm)'].head(5)

# 如果一次要選取多個欄位，就把這些欄位名稱放進list
df[['sepal length (cm)', 'sepal width (cm)']].head(5)

"""
如果是要選第幾筆資料的某些欄位，有兩種方法
第一種是用兩次中括號進行篩選，先篩選出第1筆到第5筆，再篩選出所要的欄位
"""

df[0:5][['sepal length (cm)', 'sepal width (cm)']]

"""
這邊要注意一件事情是python的index都是從0開始，所以index為1是這個資料集的第二筆，這點要注意
另外，有些函數若是你最大選取的打5他不會取到index = 5的這筆資料，只會取到index = 4
第二種是利用loc(location的意思)這個函數，中括號裡面第一個放index的範圍，第二個放column的名稱
"""

df.loc[0:5, ['sepal length (cm)', 'sepal width (cm)']]

"""
資料篩選
在中括號裡面方入篩選條件即可
"""

df[df['sepal length (cm)'] > 7 ]

"""
資料分組
使用groupby的方式，後面加入要運算的函式，例如sum 或是 mean
"""

df.groupby(by = 'target_names').sum()

# List vs Series  ===================================================
import numpy as np
import pandas as pd

sample_series = pd.Series(np.random.sample(1000000))
sample_list = list(np.random.sample(1000000))

%timeit sample_series+sample_series
%timeit [i+i for i in sample_list]

# 可以用fillna補值
careCenter['行政區域'] = careCenter['行政區域'].fillna(method='ffill')

import os # 獲取目前工作路徑
os.getcwd() #获取当前工作路径

single_fund_data.to_csv('Result.csv') #相对位置，保存在getwcd()获得的路径下
single_fund_data.to_csv('C:/Users/think/Desktop/Result.csv') #绝对位置

single_fund_data.to_csv('C:/Users/think/Desktop/Result.csv', sep='?')#使用?分隔需要保存的数据，如果不写，默认是,
single_fund_data.to_csv('C:/Users/think/Desktop/Result1.csv', na_rep='NA') #确实值保存为NA，如果不写，默认是空
single_fund_data.to_csv('C:/Users/think/Desktop/Result1.csv', float_format='%.2f') #保留两位小数
single_fund_data.to_csv('C:/Users/think/Desktop/Result.csv', columns=['name']) #保存索引列和name列
single_fund_data.to_csv('C:/Users/think/Desktop/Result.csv', header=0) #不保存列名
single_fund_data.to_csv('C:/Users/think/Desktop/Result1.csv', index=0) #不保存行索引

# 編碼設置UTF8但因為在windows是big5，打開會亂碼，而且有時big5會處理不了一些較複雜的字會出現錯誤，所以加上sig，編碼一樣是utf8，但是可以正常在windows顯示
fund_data.to_csv('C:/Users/Bill/Desktop/fund_data_' + thetime + '.csv', encoding='utf-8-sig')

import pandas as pd
import numpy as np
import glob
#讀取單個csv檔=====================================================
#讀取中文路徑要先轉換
#通過open操作中轉一下（應該是轉換成python內置的文件流了)
o = open('C:/Users/bill/Desktop/新增資料夾/展示的平台/金融相關/基金介紹資料/fund_data.csv', 'r')
#如果csv文件是gbk格式的話就要修改成這個格式
#o=open(path,'rb')
df = pd.read_csv(o, header = None)
o.close
print('用read_csv讀取的csv文檔：', df)

#另外一個方法，加上engine
df = pd.read_csv('F:/展示的平台/金融相關/基金介紹資料/fund_data.csv', engine='python')
print('用read_csv讀取的csv文檔：', df)

#讀取多個csv檔====================================================
path =r'C:\Users\bill\Desktop\新增資料夾\展示的平台\金融相關\基金介紹資料' # 資料夾名稱
#用glob套件可以返回所有匹配的文件路徑列表
allFiles = glob.glob(path + "/*.csv")
#創造一個空的dataframe，跟讀進來的資料進行合併
frame = pd.DataFrame()
list_ = []
for file_ in allFiles:
    o = open(file_)
    df = pd.read_csv(o, header = 0)
    list_.append(df)
o.close
#合併所有list
frame = pd.concat(list_)

# 函數內如果不填，則回傳頭5行
df.head(10)

# 查看有多少筆資料有NA，看nonnull總數是不是跟資料列數一樣數量，如果不一樣代表有NA值
df.info()

#取基金組別這個欄位的第一筆
A = df['基金組別'][0]

#查看總長度
len(df)

# 讀取 Html 檔案
dfs = pd.read_html('http://rate.bot.com.tw/xrt?Lang=zh-TW')
dfs[0]