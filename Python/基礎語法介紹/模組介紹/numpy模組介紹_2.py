"""
接下來介紹Numpy中一些比較沒上一篇那麼常用的函數及用法
"""

"""
高級索引
"""

import numpy as np


# 整數組索引
x = np.array([[1,  2],  [3,  4],  [5,  6]])

"""
獲取x矩陣中(0,0)，(1,1)和(2,0)位置處的元素
前面陣列代表列數，後面陣列代表行數
"""

y = x[[0, 1, 2],  [0, 1, 0]]
print(y)

# 接下來我們嘗試找出x矩陣中四個角的元素
x = np.array([[  0,  1,  2], [  3,  4,  5], [  6,  7,  8], [  9,  10,  11]])
print(x)
print('\n')

# 四個角的元素位置分別是(0, 0)、(0, 2)、(3, 0)、(3, 2)，接下分別將列跟行的位置用陣列表示
rows = np.array([[0,0],[3,3]])
cols = np.array([[0,2],[0,2]])
y = x[rows,cols]
print('矩陣四個角元素為：')
print(y)

# 或者我們也可以用前面介紹過的 :、...，兩個符號來取出想要的組合
a = np.array([[1,2,3], [4,5,6],[7,8,9]])

# b的意思是取出列1~2、行1~2的元素，也就是(1, 1)、(1, 2)、(2, 1)、(2, 2)，這邊也要注意1:3只會取到2，而且都是從0列0行開始算，所以python內的第0列代表我們看到的第1列
b = a[1:3, 1:3]

# c跟b一樣只是1:3用[1, 2]代表
c = a[1:3,[1,2]]

# d就是取出第1行之後的元素，也就是第2行第三行元素都取出
d = a[...,1:]
print(b)
print(c)
print(d)

"""
布林值索引
"""

x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print(x)
print('\n')

# 找出矩陣中大於5的元素
print('大於 5 的元素是：')
print(x[x >  5])

"""
~代表補碼運算符，就像我們平常說的0轉為非0的感覺，看下例，np.isnan是找出na的元素，我們加上~代表要找出非na的元素
"""

a = np.array([np.nan,  1,2,np.nan,3,4,5])
print(a[~np.isnan(a)])

# np.iscomplex是找出複數元素
a = np.array([1,  2+6j,  5,  3.5+5j])
print(a[np.iscomplex(a)])

"""
花式索引
根據索引數組的值作為目標數組的某個軸的下標來取值。對於使用一維整數作為索引，如果目標是一維陣列，那麼索引的結果就是對應位置的元素；如果目標是二維陣列，那麼就是對應下標的行
下面例子就是抓出x的第4、2、1、7列元素
"""

x=np.arange(32).reshape((8,4))
print(x[[4,2,1,7]])

# 我們也可以將順序倒過來從下往上開始，從下往上的話位置就是從1開始算而不是從0開始
x=np.arange(32).reshape((8,4))
print(x[[-4,-2,-1,-7]])

# 傳入多個索引陣列的話就要用到ix_，以下例子是先抓出第1、5、7、2列後，再將其元素以0、3、1、2的位置重新排序
x=np.arange(32).reshape((8,4))
print(x[np.ix_([1,5,7,2],[0,3,1,2])])

"""
Broadcast
是numpy 對不同形狀(shape)的數組進行數值計算的方式， 對數組的算術運算通常在相應的元素上進行。
如果兩個數組a和b形狀相同，即滿足a.shape == b.shape，那麼a*b的結果就是a與b數組對應位相乘。這要求維數相同，且各維度的長度相同
"""

a = np.array([1,2,3,4])
b = np.array([10,20,30,40])
c = a * b
print(c)

# 當運算中的2個數組的形狀不同時，numpy 將自動觸發Broadcast機制，也就是將全部陣列一同做運算
a = np.array([[ 0, 0, 0],
           [10,10,10],
           [20,20,20],
           [30,30,30]])
b = np.array([1,2,3])
print(a + b)

"""
char 字符串處理函數
我們先介紹下一般在處理字符串可能會用到的函數有哪些
add()：對兩個陣列的列行逐個字串元素分別進行連接
"""

print('連接兩個字串：')
print(np.char.add(['hello'],[' xyz']))
print('\n')
print('連接示例：')
print(np.char.add(['hello', 'hi'],[' abc', ' xyz']))

"""
multiply()：返回按元素多重連接後的字串
重複連接Runoob這個元素3次
"""

print(np.char.multiply('Runoob ',3))

"""
center()：居中字串，可以指定字元在左側和右側進行填充
str: 字串，width: 總字串長度，不足的會填充指定字元，fillchar: 填補字元
"""

print(np.char.center('Runoob', width = 20,fillchar = '*'))


# capitalize()：將字串第一個字母轉換為大寫
print(np.char.capitalize('runoob'))

# title()：將字串的每個單詞的第一個字母轉換為大寫
print(np.char.title('i like runoob'))

"""
lower()：陣列元素轉換為小寫
"""

# 操作陣列
print(np.char.lower(['RUNOOB','GOOGLE']))

# 操作字串
print(np.char.lower('RUNOOB'))

"""
upper()：陣列元素轉換為大寫
"""

# 操作陣列
print(np.char.upper(['runoob','google']))

# 操作字串
print(np.char.upper('runoob'))

"""
split()：指定分隔符號號對字串進行分割，並返回陣列清單
"""

# 分隔符號默認為空格
print(np.char.split ('i like runoob?'))

# 分隔符號為 .
print(np.char.split ('www.runoob.com', sep = '.'))

"""
splitlines()：返回元素中的行清單，以分行符號分割
\n，\r，\r\n 都可用作分行符號
"""

print(np.char.splitlines('i\nlike runoob?'))
print(np.char.splitlines('i\rlike runoob?'))

"""
strip()：移除元素開頭及結尾處的特定字元
移除字串頭尾的 a 字元
"""

print(np.char.strip('ashok arunooba','a'))

# 移除數組元素頭尾的 a 字元
print(np.char.strip(['arunooba','admin','java'],'a'))

"""
join()：通過指定分隔符號號來連接陣列中的元素
"""

# 操作字串
print(np.char.join(':','runoob'))

# 指定多個分隔符號運算元組元素
print(np.char.join([':','-'],['runoob','google']))

"""
replace()：使用新字串替換字串中的所有子字串
"""

print(np.char.replace ('i like runoob', 'oo', 'cc'))

"""
decode()：陣列元素依次調用str.decode，對陣列中的每個元素調用 str.encode 函數。 預設編碼是 utf-8
"""

a = np.char.encode('runoob', 'cp500')
print(a)

"""
encode()：陣列元素依次調用str.encode，對編碼的元素進行 str.decode() 解碼
"""

a = np.char.encode('runoob', 'cp500')
print(a)
print(np.char.decode(a,'cp500'))


"""
數學運算函數
around() 函數返回指定數位的四捨五入值
"""

a = np.array([1.0,5.55,  123,  0.567,  25.532])  
print(a)
print('\n')
print(np.around(a))
print(np.around(a, decimals = 1))

"""
floor() 返回數位的下舍整數
"""

a = np.array([-1.7,  1.5,  -0.2,  0.6,  10])
print(a)
print('\n')
print(np.floor(a))

"""
ceil() 返回數位的上入整數
"""

a = np.array([-1.7,  1.5,  -0.2,  0.6,  10])  
print(a)
print('\n')
print(np.ceil(a))

"""
接著介紹簡單的加減乘除: add()，subtract()，multiply() 和 divide()
"""

a = np.arange(9, dtype = np.float_).reshape(3,3)  
print(a)
print('\n')

b = np.array([10,10,10])  
print(b)
print('\n')
print('兩個陣列相加：')
print(np.add(a,b))
print('\n')
print('兩個陣列相減：')
print(np.subtract(a,b))
print('\n')
print('兩個陣列相乘：')
print(np.multiply(a,b))
print('\n')
print('兩個陣列相除：')
print(np.divide(a,b))

"""
reciprocal() 函數返回參數逐元素的倒數
"""

a = np.array([0.25,  1.33,  1,  100])  
print(a)
print('\n')
print(np.reciprocal(a))

"""
power() 函數將第一個輸入陣列中的元素作為底數，第二個輸入的陣列將作為第一個陣列元素的次方數
"""

a = np.array([10,100,1000])  
print(a)
print('\n') 
print(np.power(a,2))
print('\n')

b = np.array([1,2,3])  
print(b)
print('\n')
print(np.power(a,b))

"""
mod() 計算輸入陣列中相應元素的相除後的餘數。 函數remainder()也產生相同的結果
"""

a = np.array([10,20,30]) 
b = np.array([3,5,7])  
print(a)
print('\n')
print(b)
print('\n')
print(np.mod(a,b))
print('\n')
print(np.remainder(a,b))


