import pandas as pd
import numpy as np

# Merge數據合併 =================================================
# 在日常的數據處理中，經常需要將兩張表拼接起來使用，這樣的操作對應到SQL中是join，在Pandas中則是用merge來實現
# merge的參數
# on：列名，join用來對齊的那一列的名字，用到這個參數的時候一定要保證左表和右表用來對齊的那一列都有相同的列名
# left_on：左表對齊的列，可以是列名，也可以是和dataframe同樣長度的arrays
# right_on：右表對齊的列，可以是列名，也可以是和dataframe同樣長度的arrays
# left_index / right_index: 如果是True的haunted以index作為對齊的key
# how：數據融合的方法
# sort：根據dataframe合併的keys按字典順序排序，默認是，如果置false可以提高表現
# suffix：如果和表合併的過程中遇到有一列兩個表都同名，但是值不同，合併的時候又都想保留下來，就可以用suffixes給每個表的重複列名增加後綴

# inner join：此為內連接，它在拼接的過程中會取兩張表的鍵（key）的交集進行合併
df_1.merge(df_2, how='inner', on='userid')

# left join：merge時，以左邊表格的鍵為基准進行配對，如果左邊表格中的鍵在右邊不存在，則用缺失值NaN填充
df_2.merge(df_1, how='left', on='userid')

# right join：merge時，以右邊表格的鍵為基准進行配對，如果右邊表格中的鍵在左邊不存在，則用缺失值NaN填充
df_2.merge(df_1, how='right', on='userid')

# outer join：此為外連接，在拼接的過程中它會取兩張表的鍵（key）的聯集進行合併，對於沒有匹配到的地方，使用缺失值NaN進行填充
df_1.merge(df_2, how='outer', on='userid')

# suffix參數使用
result = pd.merge(left, right, on='k', suffixes=['_l', '_r'])

# 更新表的nan值
# 使用combine_first會只更新左表的nan值，而update則會更新左表的所有能在右表中找到的值
combine_first
update

# concat數據合併 ==============================================================
# concat縱向合併，預設是axis=0
# 定義資料集
# np.ones((3,4))創造出3列4行值都是1的陣列
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*2, columns=['a','b','c','d'])

# 但是單純合併的話左邊的每列index都是按照df1、2、3的index
res = pd.concat([df1, df2, df3], axis=0)
print(res)

# 所以我們合併後要重新設定index
res = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
print(res)

# join_axes(依照 axes 合併)
# 定義資料集
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'], index=[1,2,3])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['b','c','d','e'], index=[2,3,4])

# 依照df1.index進行橫向合併
res = pd.concat([df1, df2], axis=1, join_axes=[df1.index])
print(res)

# 移除join_axes
res = pd.concat([df1, df2], axis=1)
print(res)

# join合併方式 ================================================================
# 定義資料集
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'], index=[1,2,3])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['b','c','d','e'], index=[2,3,4])
# 函數默認join='outer'
# 依照column來做縱向合併，有相同的column上下合併在一起，其他獨自的column自成一欄，原本沒有值的位置皆以NaN填補。
res = pd.concat([df1, df2], axis=0, join='outer')
print(res)

# 另外一個合併方式是只有相同的column合併在一起，其他的會被拋棄
res = pd.concat([df1, df2], axis=0, join='inner')
print(res)

# append(添加數據)，只有縱向合併，没有橫向合併
# 定義資料集
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
s1 = pd.Series([1,2,3,4], index=['a','b','c','d'])

# 將df2合併到df1的下面，以及重置index，並打印出結果
res = df1.append(df2, ignore_index=True)
print(res)

# 合併多個df，將df2與df3合併至df1的下面，以及重置index，並打印出結果
res = df1.append([df2, df3], ignore_index=True)
print(res)

#合并series，将s1合并至df1，以及重置index，並打印出結果
res = df1.append(s1, ignore_index=True)
print(res)

# 嘗試從函數庫中取出內建資料集 ======================================
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np

iris = load_iris()
#由於原始資料是將類別的結果分開存放，所以我們分別取出資料
x = pd.DataFrame(iris['data'], columns=iris['feature_names'])
y = pd.DataFrame(iris.target, columns=['target_names'])

data = pd.concat([x,y], axis=1)
data