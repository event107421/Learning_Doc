import pandas as pd
import numpy as np

# 創建範例數據
boolean=[True,False]
gender=["男","女"]
color=["white","black","yellow"]
data=pd.DataFrame({
    "height":np.random.randint(150,190,100),
    "weight":np.random.randint(40,90,100),
    "smoker":[boolean[x] for x in np.random.randint(0,2,100)],
    "gender":[gender[x] for x in np.random.randint(0,2,100)],
    "age":np.random.randint(15,90,100),
    "color":[color[x] for x in np.random.randint(0,len(color),100) ]
})

# 以Series方式數據處理 =============================================================================
# map函數數據處理 ======================================================
# 原理：不論是利用字典還是函數進行映射，map方法都是把對應的數據逐個當作參數傳入到字典或函數中，得到映射後的值

# 把數據中的gender列的男替換為1，女替換為0，有以下兩種方式：
# 1.使用字典進行映射
data["gender"] = data["gender"].map({"男":1, "女":0})

# 2.使用函數
def gender_map(x):
    gender = 1 if x == "男" else 0
    return gender
# 注意這里傳入的是函數名，不帶括號
data["gender"] = data["gender"].map(gender_map)

# apply函數數據處理 ======================================================
# apply方法的作用原理和map方法類似，區別在於apply能夠傳入功能更為複雜的函數
# 假設在數據統計的過程中，年齡age列有較大誤差，需要對其進行調整（加上或減去一個值）
# 由於這個加上或減去的值未知，故在定義函數時，需要加多一個參數bias
# 此時用map方法是操作不了的（傳入map的函數只能接收一個參數），apply方法則可以解決這個問題
# 我們定義了一個解決年齡誤差的函數
def apply_age(x,bias):
    return x+bias

# 以元組的方式傳入額外的參數，執行後就可以看到age列中的資料都減了3
data["age"] = data["age"].apply(apply_age, args=(-3,))

# 以DataFrame方式數據處理 ============================================================
# 在DataFrame對象的大多數方法中，都會有axis這個參數，它控制了你指定的操作是沿著0軸還是1軸進行
# axis = 0代表操作對行columns進行，axis = 1代表操作對列row進行
# 以下例子就是當沿著軸0(axis=0)進行操作時，會將各欄(columns)默認以Series的形式作為參數，傳入到你指定的操作函數中，操作後合併並返回相應的結果
# 沿着0轴求和
data[["height", "weight", "age"]].apply(np.sum, axis=0)

# 沿着0轴取对数
data[["height","weight","age"]].apply(np.log, axis=0)

# 換看沿著軸1(axis=1)進行操作，當apply設置了axis=1，會默認將每一列數據以Series的形式(Series的索引為欄位名)傳入指定函數，返回相應的結果
# 在數據集中，有身高和體重的數據，所以根據這個，我們可以計算每個人的BMI指數(體檢時常用的指標，衡量人體肥胖程度和是否健康的重要標準)
# 計算公式是：體重指數BMI=體重/身高的平方（國際單位kg/㎡），因為需要對每個樣本進行操作，這裡使用axis=1的apply進行操作
def BMI(series):
    weight = series["weight"]
    height = series["height"]/100
    BMI = weight/height**2
    return BMI

data["BMI"] = data.apply(BMI, axis=1)


# applymap函數數據處理 ======================================================
df = pd.DataFrame({
    "A":np.random.randn(5),
    "B":np.random.randn(5),
    "C":np.random.randn(5),
    "D":np.random.randn(5),
    "E":np.random.randn(5),
})
df

# 現在想將DataFrame中所有的值保留兩位小數顯示，可以使用applymap
# 可以使用applymap是直接將dataframe中每個作為x傳入函數中
df.applymap(lambda x:"%.2f" % x)