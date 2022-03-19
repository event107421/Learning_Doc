"""
模塊的使用
對於任何一種編程語言來說，給變量，函數這樣的標識符起名字都是一個讓人頭疼的問題，因為我們會遇到命名衝突這種尷尬的情況。
例如項目是由多人協作進行團隊開發的時候，團隊中可能有多個程序員都定義了名為foo的函數，那麼怎麼解決這種命名衝突呢？
答案其實很簡單，Python中每個文件就代表了一個模塊（module），我們在不同的模塊中可以有同名的函數
在使用函數的時候我們通過import關鍵字導入指定的模塊就可以區分到底要使用的是哪個模塊中的foo函數
"""

# 模組載入方法 ==============================================================
# 如果有一大堆數學相關的函式與常數定義，可以進行組合
def max(a, b):
    return a if a > b else b
def min(a, b):
    return a if a < b else b

def sum(*numbers): # numbers 接受可變長度引數
    total = 0
    for number in numbers:
        total += number
    return total

pi = 3.141592653589793
e = 2.718281828459045

# 把上述的程式存成xmath.py，就可以import進來
import xmath
print('# import xmath')
print(xmath.pi)
print(xmath.max(10, 5))
print(xmath.sum(1, 2, 3, 4, 5))

print('# import xmath as math')
import xmath as math # 為 xmath 模組取別名為 math
print(math.e)

print('# from xmath import min')
from xmath import min  # 將 min 複製至目前模組，不建議 from modu import *，易造>成名稱衝突
print(min(10, 5))

# 語法1：import [module]，表示 Import 整個 [module]
# 語法2：from [module] import [name1, name2, ...]，其中的name表示import module的其中一個 function
# 語法3：import [module] as [new_name]，表示Import 整個 [module]，但原本[module]的名字可能跟其他地方有衝突，因此利用as改名
# 語法4（不推薦）：from [module] import *，表示 Import 所有 [module] 底下的東西，語法4主要不推薦原因是容易造成名稱衝突，降低可讀性和可維護性

# 模塊的使用 ============================
"""
有兩個py檔內都寫了foo這個函數，如下
"""
# module1.py
def foo():
    print('hello, world!')


# module2.py
def foo():
    print('goodbye, world!')


"""
此時如果我們同時在程式中調用foo這個函數，那程式會將後導入的foo覆蓋前面導入的foo，如下
"""

from module1 import foo
from module2 import foo

# 會输出goodbye, world!
foo()

"""
所以我們就要將導入的模塊做區分，這樣我們就可以指定要使用哪個模塊的foo函數，如下
"""

import module1 as m1
import module2 as m2

m1.foo()
m2.foo()

# __name__ == '__main__' 使用 ================

"""
假如今天你寫了一個函數，存成py檔，可以直接調用執行後輸出結果，如下
"""
# module1.py
def foo():
    print('hello, world!')

foo()  # 直接執行module1.py檔，會直接輸出hello, world!

"""
所以，從輸出結果可以看到，如果你只是要單純執行這個函數，這完全沒有問題
但是問題會出在當你想要在別的檔案中使用你在 module1.py 中定義的函式時
例如你在相同目錄下有一個 module3.py 之後，當你要寫另外一個函數需要調用原本寫的foo函數，將它import進來，就會有個問題，如下
"""
# module3.py
import sys

sys.path.append('D:/python/')  # 加入你要import的函數存放路徑
from module1 import foo

print('goodbye, world!')
foo()

"""
從輸出結果可以看到，此時你原本預計的輸出會是goodbye, world!、hello, world!
但是結果會先出現一次hello, world!，接著才出現的輸出結果goodbye, world!、hello, world!，會多了一次hello, world!
從上面程式碼看到問題了嗎? module1.py 中的主程式在被引用的時候也被執行了，原因在於
1. 當 Python 檔案（模組、module）被引用的時候，檔案內的每一行都會被 Python 直譯器讀取並執行(所以 module1.py 內的程式碼會被執行)
2. Python 直譯器執行程式碼時，有一些內建、隱含的變數，__name__就是其中之一，其意義是「模組名稱」
   如果該檔案是被引用，其值會是模組名稱；但若該檔案是直接執行，其值會是 __main__
"""
# 這時我們在 module1.py 加上一行程式碼來做解釋，如下

# module1.py
def foo():
    print('hello, world!')


print('__name__:', __name__)
foo()

"""
從輸出結果可以看到，我們單純執行module1.py，結果會輸出兩行訊息
__name__: __main__
hello, world! 
這就應證了，當我們函數檔案是直接執行時，__name__這個輸出的值會是 __main__
"""
# 這時我們再直接執行module3.py，如下

# module3.py
import sys

sys.path.append('D:/python/')  # 加入你要import的函數存放路徑
from module1 import foo

print('goodbye, world!')
foo()

"""
從輸出結果可以看到，我們執行module3.py，結果會輸出四行訊息
__name__: module1
hello, world!
goodbye, world!
hello, world!
這也就應證了，當函數檔案是被引用時，其值會是模組名稱
所以被直接執行時與被引用 __name__ 這個輸出的值是顯示不同的
此時就回到上面的問題：要怎麼讓檔案在被引用時，不該執行的程式碼不被執行？當然就是靠 __name__ == '__main__' 做判斷
"""
# 我們在module1.py 加上一行程式碼，如下

# module1.py
def foo():
    print('hello, world!')


if __name__ == '__main__':
    foo()

# 然後我們再分別執行 module1.py 及 module3.py

import sys
sys.path.append('D:/python/')  # 加入你要import的函數存放路徑
from module1 import foo

print('goodbye, world!')
foo()

"""
此時我們可以從分別執行程式碼的結果看到，當執行 module1.py 輸出的結果是

hello, world!

而當我們執行 module3.py 輸出的結果是

goodbye, world!
hello, world!

多出來的那行 hello, world! 訊息消失了，為什麼加上輸出結果就正確了?
因為我們剛剛測試過每個python模塊（python文件）都包含內置的變量__name__，當函數檔案是直接執行時，__name__這個輸出的值會是 __main__ ，如果當函數檔案是被引用時，其值會是模組名稱
所以當函數檔案被直接執行時，__name__ == '__main__' 結果為真；而當函數檔案是被引用時，__name__ == '__main__' 結果為假，就不調用對應的方法
最後一點要說明的是，之所以常看見這樣的寫法，是因為該程式可能有「單獨執行」(例如執行一些本身的單元測試) 與「被引用」兩種情況，因此用上述判斷就可以將這兩種情況區分出來
"""

# 模組存放位置與程式碼不同位置載入方法 =========================================
# 通過sys模組導入自定義模組的path
# 因預設的位置沒有我們自己定義的目錄，所以要透過sys模組來將我們存放自定義模組的目錄加入
import sys
sys.path.append(r"/Users/bill/Desktop/pythonProject/work_code/tools")
print(sys.path)

# 此時就可以將存放於tools目錄下的模組載入
import xmath