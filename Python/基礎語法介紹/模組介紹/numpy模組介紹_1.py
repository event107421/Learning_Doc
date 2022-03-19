"""
一開始我們介紹下Numpy是甚麼，Numpy是Numeric Python的縮寫，提供了我們豐富的數學函數、強大的多維數組對像以及優異的運算性能
更重要的是，Numpy與Scipy、Matplotlib、Scikits等眾多Python科學計算庫很好結合在一起，是使用Python進行數據分析的一個核心工具
Numpy的重點在於陣列的操作，其所有功能特色都建築在同質且多重維度的 ndarray(N-dimensional array)上，一般我們稱一維陣列為 vector 而二維陣列為 matrix
一開始我們會引入 numpy 模組，透過傳入 list 到 numpy.array() 創建陣列。
"""

"""
array函數
numpy.array ( object , dtype = None , copy = True , order = None , subok = False , ndmin = 0 )
object：數組或嵌套的數列
dtype：數組元素的數據類型
copy：對像是否需要復制
order：創建數組的樣式，C為行方向，F為列方向，A為任意方向(默認)
subok：默認返回一個與基類類型一致的數組
ndmin：指定生成數組的最小維度
array與list差別
python中的list是python的內置數據類型，list中的數據類不必相同的，而array的中的類型必須全部相同
"""

import numpy as

list1 = [1,2,3,'a']
print(list1)

a = np.array([1, 2, 3, 4, 5])
b = np.array([[1, 2, 3], [4, 5, 6]])
c = list(a)
print(a,np.shape(a))
print(b, np.shape(b))
print(c,np.shape(c))


"""
這邊說一下數據有哪些類型：
bool：邏輯值數據類型(True 或者False)

int：默認的整數類型(類似於C 語言中的long，int32 或int64)

intc：與C 的int 類型一樣，一般是int32 或int 64

intp：用於索引的整數類型(類似於C 的ssize_t，一般情況下仍然是int32 或int64)

int8：字節(-128 to 127)

int16：整數(-32768 to 32767)

int32：整數(-2147483648 to 2147483647)

int64：整數(-9223372036854775808 to 9223372036854775807)

uint8：無符號整數(0 to 255)

uint16：無符號整數(0 to 65535)

uint32：無符號整數(0 to 4294967295)

uint64：無符號整數(0 to 18446744073709551615)

float：float64 類型的簡寫

float16：半精度浮點數，包括：1 個符號位，5 個指數位，10 個尾數位

float32：單精度浮點數，包括：1 個符號位，8 個指數位，23 個尾數位

float64：雙精度浮點數，包括：1 個符號位，11 個指數位，52 個尾數位

complex：complex128 類型的簡寫，即128 位複數

complex64：複數，表示雙32 位浮點數(實數部分和虛數部分)

complex128：複數，表示雙64 位浮點數(實數部分和虛數部分)

我們可以利用dtype來定義數據的類型
另外，數據類型可以使用字符串來代替，例如：int8, int16, int32, int64四種數據類型可以使用字符串'i1', 'i2','i4','i8'代替
"""

student = np . dtype ( [ ( ' name ' , ' S20 ' ) , ( ' age ' , ' i1 ' ) , ( ' marks ' , ' f4 ' ) ] )
a = np . array ( [ ( ' abc ' , 21 , 50) , ( ' xyz ' , 18 , 75 ) ] , dtype = student )
print( a )

"""
每個內建類型都有一個唯一定義它的字符代碼
b：邏輯值

i：(有符號) 整型

u：無符號整型integer

f：浮點型

c：複數浮點型

m：timedelta（時間間隔）

M：datetime（日期時間）

O：(Python) 對象

S, a：(byte-)字符串

U：Unicode

V：原始數據(void)
"""

# numpy屬性
np1 = np.array([1, 2, 3])
np2 = np.array([3, 4, 5])

# 陣列相加
print(np1 + np2)

# list列表轉array陣列
array = np.aaray([1, 2, 3], [4, 5, 6])

"""
ndim：維度
"""

print('number of dim:',array.ndim)

"""
shape：行數和列數
"""

print('shape :',array.shape)

"""
size：元素個數
"""

print('size:',array.size)


"""
array：創建陣列
創造一個2列3行的矩陣
"""

a = np.array([[2, 3, 4],[2, 3, 4]])

"""
dtype：指定數據類型
"""

a = np.array([2, 3, 4], dtype = np.int)
a = np.array([2, 3, 4], dtype = np.float)

"""
這邊我們也可以利用布林值來取出陣列中的值，我們取出np3中大於3的數字
"""

np3 = np.array([1, 2, 3, 4, 5, 6])
print(np3 > 3)
print(np3[np3 > 3])

"""
zeros：創建全為0數據
創建3列4行全為0的矩陣
"""

a = np.zeros((3, 4))

"""
ones：創建全為1數據
創建3列4行全為1的矩陣，指定數據類型為整數
"""

a = np.ones((3, 4), dtype = np.int)

"""
empty：創建接近0數據
"""

a = np.empty((3, 4))

"""
arrange：按指定範圍創建數據
創建一個10至20的數列，間隔為2
"""

a = np.arange(10, 20, 2)

"""
可以使用reshape來指定此數列的列行數，例如我們創建一個0至11的數列，分成3列4行的矩陣
"""

a = np.arange(12).reshape((3,4))

"""
如果想對這個矩陣進行加總，可以指定要列加總還是行加總，最後會回傳一維陣列，以下就是對列加總
"""

print(np3.sum(axis=1))

"""
linspace：創建線段
創建一個1至10的數列，分割為20個數值
"""

a = np.linspace(1,10,20)

"""
logspace：創建一個於等比數列
"""

np.logspace(start, stop, num = 50, endpoint = True, base = 10.0, dtype = None)

"""
start：序列的起始值為：base ** start

stop：序列的終止值為：base ** stop。如果endpoint為true，該值包含於數列中

num：要生成的等步長的樣本數量，默認為50

endpoint：該值為ture時，數列中中包含stop值，反之不包含，默認是True。

base：對數log 的底數，取對數的時候log 的下標

dtype：ndarray 的數據類型
"""

a = np.logspace(0, 9, num = 10, base=2)
print(a)

"""
切片和索引
ndarray 數組可以基於0 - n 的下標進行索引，切片對象可以通過內置的slice 函數，並設置start, stop 及step 參數進行，從原數組中切割出一個新數組
"""

# 從索引 2開始到索引 7 停止，間隔為2
a = np.arange(10)
s = slice(2, 7, 2) 
print(a[s])

"""
我們也可以用冒號分割參數start:stop:step 來進行操作
這邊稍微解釋下冒號的用法，如果只放置一個參數，如[2]，將返回與該索引相對應的單個元素。如果為[2:]，表示從該索引開始以後的所有項都將被提取。如果使用了兩個參數，如[2:7]，那麼則提取兩個索引(不包括停止索引)之間的項
"""

a = np.arange(10) 
b = a[2:7:2]
print(b)

"""
切片還可以包括省略號…，可以用在多個陣列組成的矩陣上。如果在行位置使用省略號，它將返回包含行中元素的ndarray
"""

a = np.array([[1,2,3], [3,4,5], [4,5,6]]) 
print(a[...,1])   # 第2列元素
print(a[1,...])   # 第2行元素
print(a[...,1:])  # 第2列及剩下的所有元素
