"""
統計函數
amin() 用於計算陣列中的元素沿指定軸的最小值。
amax() 用於計算陣列中的元素沿指定軸的最大值。
"""

a = np.array([[3,7,5],[8,4,3],[2,4,9]]) 
print (a)
print ('\n')

# 1代表找出每列的最小元素
print (np.amin(a,1))
print ('\n')

# 0代表找出每行的最小元素
print (np.amin(a,0))
print ('\n')
print (np.amax(a))
print ('\n')
print (np.amax(a, axis = 0))

"""
ptp()函數計算陣列中元素最大值與最小值的差（最大值 - 最小值）
"""

a = np.array([[3,7,5],[8,4,3],[2,4,9]]) 
print (a)
print ('\n')
print (np.ptp(a))
print ('\n')

# 1代表計算每列的最大元素-最小元素
print (np.ptp(a, axis =  1))
print ('\n')

# 0代表計算每列的最大元素-最小元素
print (np.ptp(a, axis =  0))

"""
percentile()百分位數是統計中使用的度量
"""

a = np.array([[10, 7, 4], [3, 2, 1]])
print (a)

# 50% 的分位數，就是 a 裡排序之後的中位數
print (np.percentile(a, 50))

# axis為 0，計算每列的百分位數
print (np.percentile(a, 50, axis=0))

# axis 為 1，計算每行的百分位數
print (np.percentile(a, 50, axis=1))

# 可以用keepdims來保持維度不變
print (np.percentile(a, 50, axis=1, keepdims=True))

"""
median()函數用於計算陣列元素的中位數
"""

a = np.array([[30,65,70],[80,95,10],[50,90,60]]) 
print (a)
print ('\n')
print (np.median(a))
print ('\n')

#計算每列的中位數
print (np.median(a, axis =  0))
print ('\n')

#計算每行的中位數
print (np.median(a, axis =  1))

"""
mean() 函數返回陣列中元素的算術平均值
"""

a = np.array([[1,2,3],[3,4,5],[4,5,6]]) 
print (a)
print ('\n')
print (np.mean(a))
print ('\n')

#計算每列的平均數
print (np.mean(a, axis =  0))
print ('\n')

#計算每行的平均數
print (np.mean(a, axis =  1))

"""
average() 根據在另一個陣列中給出的各自的權重計算當前陣列中元素的加權平均值
"""

a = np.array([1,2,3,4]) 
print (a)
print ('\n')

# 不指定權重時相當於 mean 函數
print (np.average(a))
print ('\n')

# 設定wts權重
wts = np.array([4,3,2,1]) 
print (np.average(a,weights = wts))
print ('\n')

# 如果 returned 參數設為 true，則返回權重的和 
print (np.average([1,2,3,  4],weights =  [4,3,2,1], returned =  True))

"""
如果是在多維陣列中也可以指定要計算的列或行
"""

a = np.arange(6).reshape(3,2) 
print (a)
print ('\n')

wt = np.array([3,5]) 
print (np.average(a, axis =  0, weights = wt))
print ('\n')
print (np.average(a, axis =  1, weights = wt, returned =  True))

"""
標準差std = sqrt(mean((x - x.mean())**2))
"""

print (np.std([1,2,3,4]))

"""
變異數mean((x - x.mean())** 2)
"""

print (np.var([1,2,3,4]))


"""
排序、條件篩選函數
sort() 函數返回輸入陣列的排序
"""

a = np.array([[3,7],[9,1]])
print (a)
print ('\n')
print (np.sort(a))
print ('\n')

# 每列排序
print (np.sort(a, axis =  0))
print ('\n')

# 在 sort 函數中排序欄位 
dt = np.dtype([('name',  'S10'),('age',  int)]) 
a = np.array([("raju",21),("anil",25),("ravi",  17),  ("amar",27)], dtype = dt)  
print (a)
print ('\n')
print (np.sort(a, order =  'name'))

"""
argsort() 函數返回的是陣列值從小到大的索引值
"""

x = np.array([3,  1,  2])  
print (x)
print ('\n')

y = np.argsort(x)
print (y)
print ('\n')

# 以排序後的順序重構原陣列
print (x[y])
print ('\n')

# 使用迴圈重構原陣列：')
for i in y:  
    print (x[i], end=" ")

"""
lexsort() 用於對多個序列進行排序，例如我們有學生成績以及成績對應的學生姓名兩個陣列，我們可以用lexsort這個函數，他會先對成績做排序，接下來會把成績的順序也對照到姓名那個陣列上做排序
"""

nm =  ('raju','anil','ravi','amar') 
dv =  ('f.y.',  's.y.',  's.y.',  'f.y.') 
ind = np.lexsort((dv,nm))  
print (ind) 
print ('\n') 

# 使用這個索引來獲取排序後的資料
print ([nm[i]  +  ", "  + dv[i]  for i in ind])

"""
nonzero() 函數返回輸入陣列中非零元素的索引
"""

a = np.array([[30,40,0],[0,20,10],[50,0,60]])  
print (a)
print ('\n')
print (np.nonzero (a))

"""
where() 函數返回輸入陣列中滿足給定條件的元素的索引
"""

x = np.arange(9.).reshape(3,  3)  
print (x)

# 大於 3 的元素的索引
y = np.where(x >  3)  
print (y)

# 使用這些索引來獲取滿足條件的元素
print (x[y])

"""
extract() 函數根據某個條件從陣列中抽取元素，返回滿條件的元素
"""

x = np.arange(9.).reshape(3,  3)  
print (x)

# 定義條件, 選擇偶數元素
condition = np.mod(x,2)  ==  0  
print (condition)

# 使用條件提取元素
print (np.extract(condition, x))

"""
partition()用於指定一個數，對陣列進行分區
"""

a = np.array([3, 4, 2, 1])

# 將陣列 a 中所有元素（包括重複元素）從小到大排列，比第3小的放在前面，大的放在後面
np.partition(a, 3)  

# 小於 1 的在前面，大於 3 的在後面，1和3之間的在中間
np.partition(a, (1, 3))


"""
矩陣(Matrix) 
該模組中的函數返回的是一個矩陣，而不是 ndarray 物件
matlib.empty(shape, dtype, order) 函數返回一個新的矩陣

shape: 定義新矩陣形狀的整數或整數元組

Dtype: 可選，資料類型

order: C（行優先） 或者 F（列優先）
"""

import numpy.matlib 
import numpy as np

# 填充隨機數值
print (np.matlib.empty((2,2)))

"""
matlib.zeros() 函數創建一個以 0 填充的矩陣
"""

print (np.matlib.zeros((2,2)))

"""
matlib.ones()函數創建一個以 1 填充的矩陣
"""

print (np.matlib.ones((2,2)))

"""
matlib.eye() 函數返回一個矩陣，對角線元素為 1，其他位置為零
"""

print (np.matlib.eye(n =  3, M =  4, k =  0, dtype =  float))

"""
n: 返回矩陣的列數
M: 返回矩陣的行數，默認為 n
k: 對角線的索引
dtype: 資料類型
"""

"""
matlib.identity() 函數返回給定大小的單位矩陣，單位矩陣是個方陣，從左上角到右下角的對角線（稱為主對角線）上的元素均為 1，除此以外全都為 0
"""

print (np.matlib.identity(5, dtype =  float))

"""
matlib.rand() 函數創建一個給定大小的矩陣，資料是隨機填充的
"""

print (np.matlib.rand(3,3))

"""
矩陣總是二維的，而 ndarray 是一個 n 維陣列。 兩個可互換的
"""

i = np.matrix('1,2;3,4')  
print (i)

j = np.asarray(i)  
print (j)

k = np.asmatrix (j)  
print (k)



