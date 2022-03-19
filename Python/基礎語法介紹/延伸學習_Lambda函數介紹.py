# Lambda函式介紹 ============================================================
"""
在這篇我們來介紹python中可以映射到每個元素的函數

lambda匿名函數介紹
在這之前我們先來說一下python內一個匿名函數的用法，也就是lambda，它允許快速定義單行函數，可以用在任何需要函數的地方，那我們先說說lambda與def的區別

lambda與def的區別：
1.def創建的方法是有名稱的，而lambda沒有。

2.lambda會返回一個函數對象，但這個對像不會賦給一個標識符，而def則會把函數對象賦值給一個變量(函數名)。

3.lambda只是一個表達式，而def則是一個語句。

4.lambda表達式" : "後面，只能有一個表達式，def則可以有多個。

5.像if或for或print等語句不能用於lambda中，def可以。

6.lambda一般用來定義簡單的函數，而def可以定義復雜的函數。
"""

# 這邊舉一個簡單的範例，我們定義一個g函數，對任何單一參數取平方、多個參數運算
g = lambda x : x ** 2
print(g(3))

g = lambda x, y, z : (x + y) ** z
print(g(1,2,2))

# 再舉一個例子，這邊先用到map函數等等會做介紹，將一個list 裡的每個元素都平方
list(map(lambda x: x*x, [y for y in range(10)]))

# 上面寫法會好過定義一個def的函數
def sq(x):
    return x * x
list(map(sq, [y for y in range(10)]))

"""
因為後者多定義了一個(污染環境的)函數，尤其如果這個函數只會使用一次的話
"""

# 可以將lambda函式指派給一個變數，後續亦可以透過此變數傳入參數來進行呼叫
mutiply = lambda x, y: x * y
print(multiply(4, 2))

# Lambda函式支援IIFE(immediately invoked function expression)語法
# 意思是利用 function expression 的方式來建立函式，並且立即執行它
print((lambda x, y:x * y)(4, 2))

# 由以下範例可以得知，當Lambda函式經定義後，沒有進行呼叫的動作，他會回傳一個function object且包含了記憶體位址
exam = lambda title: print(title)
print(exam)

# 此時可以將參數傳入呼叫印出值
title = "HelloPython"
print(exam(title))

# Lambda函數應用 ==============================================================
# 以下內建方法會將串列(List)中的每個元素傳入Lambda函式進行條件判斷，最後回傳符合條件的元素
# filter() ===============================
numbers = [50, 2, 12, 30, 27, 4, 6, 11]
result = filter(lambda x: x > 10, numbers)

# 將結果轉成串列並印出
print(list(result))

# map() ===================================
numbers = [50, 2, 12, 30, 27, 4, 6, 11]
result = map(lambda x: x * 2, numbers)

# 將結果轉成串列並印出
print(list(result))

# reduce() ================================
# 此函數內建方法雖然與前兩個函數相同，但內部運作步驟不同
# 步驟1:將可疊代物件中的前兩個元素先進行Lambda運算式的運算
# 步驟2:接著將第一個步驟的運算結果和可疊代物件中的下一個元素(第三個)傳入Lambda函式進行運算
from functools import reduce

numbers = [50, 2, 12, 30, 27, 4, 6, 11]
result = reduce(lambda x, y: x + y, numbers)

print(result)

# sorted() ================================
cars = [
	("mazda", 2000)
	, ("toyota", 1000)
	, ("benz", 5000)
]

result = sorted(cars, key = lambda car: car[1])

print(result)

# if else =================================
# 例如你要定義一個最大值的函式
def max(m, n):
    return m if m > n else n

print(max(10, 3))

# 較簡單的函數可以透過lambda來做改寫
max = lambda m, n: m if m > n else n

print(max(10, 3))

# switch陳述句(因python並沒有switch-case功能，所以可以透過字典實現 ==============================
score = int(input('請輸入分數：'))
level = score // 10
{
    10 : print('Perfect'),
    9  : print('A'),
    8  : print('B'),
    7  : print('C'),
    6  : print('D')
}.get(level, print('E'))()

# 也可以透過lambda來改寫
score = int(input('請輸入分數：'))
level = score // 10
{
    10 : lambda: print('Perfect'),
    9  : lambda: print('A'),
    8  : lambda: print('B'),
    7  : lambda: print('C'),
    6  : lambda: print('D')
}.get(level, lambda: print('E'))()

# 這邊來比較一下Lambda函式與一般函式(Function)的差異為：
# 1.Lambda函式不需要定義名稱，而一般函式(Function)需定義名稱
# 2.Lambda函式只能有一行運算式，而一般函式(Function)可以有多行運算式
# 3.Lambda在每一次運算完會自動回傳結果，而一般函式(Function)如果要回傳結果要加上 return 關鍵字
# 4.建議避免過度使用與撰寫複雜的Lambda函式，複雜的邏輯運算，還是優先選擇一般函式(Function)較為理想，不然程式碼將不易維護