import pandas as pd
import numpy as np

"""
接著我們介紹一些在R常用的dplyr套件中資料整理的功能，如何在python內實現
filter() 函數：SQL 查詢中的 where 描述

select() 函數：SQL 查詢中的 select 描述

mutate() 函數：SQL 查詢中的衍生欄位描述

summarise() 函數：SQL 查詢中的聚合函數描述

group_by() 函數：SQL 查詢中的 group by 描述

merge() 函數：SQL查詢中的 join 描述

rbind、cbind()函數：SQL查詢中的 union 描述
"""

"""
首先我們將iris鳶尾花的數據讀進來，作為範例資料
順便介紹下鳶尾花的欄位

1. 花萼長度(Sepal Length)：計算單位是公分。

2. 花萼寬度(Sepal Width)：計算單位是公分。

3. 花瓣長度(Petal Length) ：計算單位是公分。

4. 花瓣寬度(Petal Width)：計算單位是公分。

5. 類別(Class)：可分為Setosa，Versicolor和Virginica三個品種。
"""

from sklearn import datasets
import pandas as pd
import numpy as np

# 首先將dictionary將key印出來發現有data, target, target name, DESCR, feature_names
iris.keys()

# 再將資料一一列印出來看看裡面是什麼，會發現DESCR為該資料的描述文字
print(iris.DESCR)
iris = datasets.load_iris()

# 由於原始資料是將類別的結果分開存放，所以我們分別取出資料
x = pd.DataFrame(iris.data, columns = iris.feature_names)
y = pd.DataFrame(iris.target, columns = ['target_names'])

# 接著我們把x,y進行合併
data = pd.concat([x,y], axis=1)
print(data)
print(data.columns)

"""
實現filter() 函數
在pandas中要實現filter的函數，可以撰寫布林判斷條件將符合條件的觀測值從資料框中篩選出
"""

print(iris.target_names)

# 那我們可能想篩選出target.names是setosa的數據，在原本數據中0、1、2分別代表['setosa' 'versicolor' 'virginica']，所以我們篩選出target_names這個欄位裡面是0的數據
data[data['target_names'] == 0]

"""
如果有多個條件，可以使用 | 或 & 符號連結
例如我們想要篩選出target.names是setosa，且花萼長度(Sepal Length)是5公分以上的數據
"""

data[(data['target_names'] == 0) & (data['sepal length (cm)'] > 5)]

"""
實現select() 函數
用 list 標註變數名稱可以將變數從資料框中選出，實踐 select() 函數的功能
"""

data[['target_names', 'sepal length (cm)']]

# 那這邊要注意一點，如果只選一個變數且沒有以 list 標註，同樣能選出變數，但是型別會變為 Series
sepal_length = data['sepal length (cm)']
print(type(sepal_length ))

"""
實現mutate() 函數
撰寫衍生公式並為變數命名即可實踐 mutate() 函數的功能，搭配 apply() 與 lambda 函數將公式應用到每一個觀測值，例如我們現在衍生一個欄位是將花萼長度(Sepal Length)四捨五入結果
"""

data['sepal length int'] = data['sepal length (cm)'].apply(lambda x: round(x, 0))

# 這邊用到了apply、lambda這兩個新的函數，之後可以到python map apply lambda介紹此篇文章連結看這幾個函數仔細的介紹
"""
實現summarise() 函數
DataFrame 不同的聚合函數針對欄位計算，實踐 summarise() 函數的功能，例如我們計算target.names是setosa種類的平均花萼長度、平均花瓣長度
"""

data[(data['target_names'] == 0)][['sepal length (cm)', 'petal length (cm)']].mean()

"""
實現group_by() 函數
最後是用 DataFrame 的 groupby 方法實踐 group_by() 函數的功能，例如我們分別計算不同分類的平均花萼長度
"""

data.groupby(by='target_names')['sepal length (cm)'].mean()

"""
實現merge() 函數
我們先創造出兩個數據集，range() 函數可以創建一個整數的列表，默認是從0開始
"""

# 以下程式碼等於list(range(0, 3))，但這邊要注意是計數到3結束，不包括3，所以結果是[0, 1, 2]
list(range(3))

# 如果要加入數值間隔，就可以加上list(range(0, 7, 2))，結果就是[0, 2, 4, 6]
df1 = pd.DataFrame({'key':['a','b','b'], 'value1':list(range(3))})
df2 = pd.DataFrame({'key':['a','b','c'], 'value2':list(range(0, 5, 2))})

# 如果沒有指定連接key，merge()函數默認用重疊列名，且默認是用inner連接(取key的交集)
pd.merge(df1,df2)

# 那我們接著看其他連接方式，還有left、right、outer三種連接方式，通過merge()函數內的how參數來指定連接方法
pd.merge(df2,df1,how='left')

# 假如要指定連接的key時則要將連接的key組成list傳入，通過merge()函數內的on來指定連接的key，這邊我們再建出兩個數據集
df3 = pd.DataFrame({'key1':['foo','foo','bar','bar'], 'key2':['one','one','one','two'], 'value1':[4,5,6,7]})
df4= pd.DataFrame({'key1':['foo','foo','bar'],  'key2':['one','two','one'], 'value2':[1,2,3]})
pd.merge(df3 , df4, on=['key1', 'key2'], how='outer')

"""
如果兩個數據集的欄位名稱不同，可以利用left_on、right_on兩個參數分別指定連接的key，
這邊我們再建出一個欄位名稱不同的數據集
"""

df5 = pd.DataFrame({'key3':['foo','foo','bar','bar'], 'key4':['one','one','one','two'], 'value1':[4,5,6,7]})
pd.merge(df4, df5, left_on = 'key1', right_on = 'key3')

"""
實現rbind()、cbind()函數
可以用pandas的concat來實現，但是這邊要注意一件事情，當把兩個數據集concat在一起時，這個函數並不會自動幫你去重複，就要再利用drop_duplicates()這個函數來達成
這邊我們用上面建好的df1、df2兩個資料集來做示範
"""

pd.concat([df1,df2])

"""
這邊可以注意到的是，當沒有指定合併方式時，concat會執行R內rbind方式，另外也可以觀察當合併的時候資料的index是按照原資料集的index
所以在concat內可以通過axis這個參數來指定合併的方式，默認是 axis = 0，合併的方式就是剛剛提到的rbind()方式，如果是指定 axis = 1就是R內的cbind()方式，剛剛提到的index問題則可以通過concat內的ignore_index重建index，默認是ignore_index = False，改為ignore_index = True
index就會重建
"""

pd.concat([df1,df2], axis = True)
pd.concat([df1,df2], ignore_index=True)

"""
去除重複數據
剛剛有提到，在進行兩個數據集concat的時候，concat這個函數並不會自動刪除重複的數據，這時我們就要利用drop_duplicates()這個函數來幫忙達成
"""

data = pd.DataFrame({'key':['a', 'a', 'b', 'b'], 'value':[1, 1, 2, 2]})
data.drop_duplicates(subset = 'key', keep = 'first', inplace = True)
data

"""
這邊我們簡單介紹下參數

subset : column label or sequence of labels, optional

用來指定特定的列，默認所有列

keep : {‘first’, ‘last’, False}, default ‘first’

刪除重複項並保留第一次出現的項

inplace : boolean, default False

直接在原來資料上修改還是保留一個副本

資料處理的介紹就到這邊，那我們下一個章節就來討論將存在電腦本機的數據檔案讀進python內
"""

# isin()函數及其逆函數使用 ================================================
# 一般在處理資料有可能會想利用模糊比對的方式搜索有包含字串的資料列，此時就可以用到isin這個函數
# DateFrame中布林索引這個東西，可以用滿足布林條件的列值來過濾數據
df = pd.DataFrame(np.random.randn(4,4),columns=['A','B','C','D'])
df
print(df.A > 0)
df[df.A>0]

# 此時添加一欄E
df['E'] = ['a','a','c','b']

# 可以從E欄中篩選出有包含a、ｃ字段的資料列
df[df.E.isin(['a','c'])]

# 也可以使用多條件篩選的方式
df[df.E.isin(['a','d']) & df.D.isin([0,])]

# 或是想篩選沒有包含的資料列則可以在前面加上~符號
df[~df.E.isin(['a','c'])]

# drop_duplicates函數使用 ===============================================
# 一般處理資料時可能會有一些重複的資料列，此時可以透過drop_duplicates函數，刪除DataFrame的某列中的重複項。
drop_duplicates(subset = '列名', keep = 'firsrt', inplace = 'True')

# subset：輸入的列名，形式為subset='列名1'，可輸入多列，形式為subset=['列名1','列名2']
# keep：包括'first'、'last'、False，三個參數，注意first和last帶引號，而False沒有，'first'是保留重複項中第一個，last是保留最後一個，False是都不保留
# inplace：包括TRUE、FALSE，TRUE是直接將重複的列資料做刪除，並覆蓋原本的資料集，FALSE則是不改變原來的dataFrame，而將結果生成在一個新的dataFrame中

df=pd.DataFrame({'x':[1,2,3,6],'y':[1,4,1,1],'z':[1,2,4,1]})
df

df.drop_duplicates(subset = ['y','z'], keep = 'first', inplace = True)
df

# agg函数使用方法 ==============================================
cities = pd.DataFrame(np.random.randn(5, 5),
     index = ['a', 'b', 'c', 'd', 'e'],
     columns = ['shenzhen', 'guangzhou', 'beijing', 'nanjing', 'haerbin'])
cities.iloc[2:4, 2:4] = np.nan
cities

# 如果這個時候，我們想看一下按城市分組，然後查看一下各個城市下數據的平均值(mean)和總和(sum)
# 一般可以分開計算，如下：
cities[['shenzhen', 'guangzhou', 'beijing', 'nanjing', 'haerbin']].sum()
cities[['shenzhen', 'guangzhou', 'beijing', 'nanjing', 'haerbin']].mean()

# 但如果是個別統計，如果還要統計其他的數值，這樣一個一個打就顯得特別麻煩，此時我們就可以使用agg函數
cities[['shenzhen','guangzhou','beijing','nanjing','haerbin']].agg(['sum','mean'])

# 我們還可以針對不同的城市，使用不同的聚合函數，只需指定一下
cities.agg({'shenzhen':['sum'],'beijing':['mean'],'nanjing':['sum','mean']})

# 實際上，在使用agg函數，很常也搭配group by函數
df = pd.DataFrame({'Country': ['China', 'China', 'India', 'India', 'America', 'Japan', 'China', 'India'],
                   'Income': [10000, 10000, 5000, 5002, 40000, 50000, 8000, 5000],
                   'Age': [50, 43, 34, 40, 25, 25, 45, 32]})
df

# 同時使用groupby和agg函數對該數據表進行分組聚合操作
df_inc = df.groupby('Country').agg(['min', 'max', 'mean'])
df_inc

# 有些時候只需對部分數據進行不同的聚合操作，此時就可以通過字典的方式來實現
df.groupby('Country').agg({'Age':['max', 'min', 'mean']})

# groupby分組運算後把返回的列重新命名 =================================================
# 有時我們會用groupby配上agg做統計，但系統返回的欄位名稱是預設值，此時想重新設定名稱如下：
# 例如我們對data做group by
import pandas as pd
import numpy as np

df = data.groupby('Seed').agg({'age': ['sum'], 'height': ['mean', 'std']})
print(df.head())

# 回傳結果如下：
#       age     height
#       sum        std       mean
# Seed
# 301    78  22.638417  33.246667
# 303    78  23.499706  34.106667
# 305    78  23.927090  35.115000
# 307    78  22.222266  31.328333
# 309    78  23.132574  33.781667

# 此時我們只要第二層的欄位名稱，就可以利用droplevel這個函數
df.columns = df.columns.droplevel(0)
print(df.head())

# 刪除後回傳結果如下：
#       sum        std       mean
# Seed
# 301    78  22.638417  33.246667
# 303    78  23.499706  34.106667
# 305    78  23.927090  35.115000
# 307    78  22.222266  31.328333
# 309    78  23.132574  33.781667

# 或者，要保留第一層的名稱，就可以跟第二層的名稱做合併:
df.columns = ["_".join(x) for x in df.columns.ravel()]
print(df.head())

#       age_sum   height_std  height_mean
# Seed
# 301        78    22.638417    33.246667
# 303        78    23.499706    34.106667
# 305        78    23.927090    35.115000
# 307        78    22.222266    31.328333
# 309        78    23.132574    33.781667

# 或者，也可以直接利用MultiIndex對多索引直接重新命名，需要重新命名的就需輸入要更改的字串，不需更改名稱的可以利用columns.levels直接選取
df_t = df.reindex(columns=pd.MultiIndex.from_product(
    [['age_stat', 'height_stat'], df.columns.levels[1], df.columns.levels[2]]))

# 解釋下MultiIndex原理 ==============================================
"""
MultiIndex表示多級索引，它是從Index繼承過來的，其中多級標籤用元組對象來表示。
"""
import pandas as pd
from pandas import DataFrame
import numpy as np

# 可以使用from_arrays()函數來建立多級索引
class1=["A", "A", "B", "B"]
class2=["x1", "x2", "y1", "y2"]
m_index1 = pd.MultiIndex.from_arrays([class1, class2], names=["class1", "class2"])
m_index1

df1 = DataFrame(np.random.randint(1, 10, (4, 3)), index = m_index1)
df1

# 也可以使用from_product()從多個集合的笛卡爾積創建MultiIndex對象
m_index2 = pd.MultiIndex.from_product([["A", "B"], ['x1', 'y1']], names = ["class1", "class2"])
m_index2

df2 = DataFrame(np.random.randint(1, 10, (2, 4)), columns = m_index2)
df2

# MultiIndex對象屬性
m_index4 = df1.index
print(m_index4[0])

# 調用.get_loc()和.get_indexer()獲取標籤的下標
print(m_index4.get_loc(("A","x2")))
print(m_index4.get_indexer([("A","x2"),("B","y1"),"nothing"]))

# MultiIndex對象使用多個Index對象保存索引中每一級的標籤
print(m_index4.levels[0])
print(m_index4.levels[1])

# MultiIndex對像還有屬性labels保存標籤的下標
print(m_index4.codes[0])
print(m_index4.codes[1])