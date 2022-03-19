"""
Class 類的使用
在python內定義一個Class(類)

class Student(object):
    pass

關鍵字class後面跟著類名，類名通常是大寫字母開頭的單詞，緊接著是(object)，表示該類是從哪個類繼承下來的。
通常，如果沒有合適的繼承類，就使用object類，這是所有類最終都會繼承下來的類，後面再來解釋類的一些功能
簡單的說，類是對象的藍圖和模板，而對象是類的實例。從這句話我們可以看出，類是抽象的概念，而對象是具體的東西。
在面向對象編程的世界中，對象都有屬性和行為，每個對象都是獨一無二的，而且對像一定屬於某個類（型）。
當我們把一大堆擁有共同特徵的對象的靜態特徵（屬性）和動態特徵（行為）都抽取出來後，就可以定義出一個叫做"類"的東西。
"""

# 創建class(類) ======================
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

"""
這邊解釋一下__init__以及self

================ __init__ ================
__init__的含義，也如同其單詞本意一樣，用來初始化，也就是給對應的類Class本身，去初始化
對支持帶參數的類的初始化，這個用法，感覺就像，其他語言中的，對於Class初始化時，可以運行傳遞不同的參數一樣
也就是有點類似於，其他語言中的，傳遞特定參數去對類進行初始化
也就是每執行這個class(類)的時候在__init__內的參數(name、score)就會被賦值初始化

================== self ==================
此處的self，是個對象，Object，是當前類的實例
因此，在class(類)對應的

self.valueName
self.function()
中的

valueName：表示self對象，即實例的變量。與其他的，Class的變量，全局的變量，局部的變量，是相對應的。
function：表示是調用的是self對象，即實例的函數。與其他的全局的函數，是相對應的。

Python中為何要有self?
在類的代碼（函數）中，需要訪問當前的實例中的變量和函數的，即，訪問Instance中的：
--對應的變量（property)：Instance.ProperyNam，去讀取之前的值和寫入新的值
--調用對應函數（function）：Instance.function()，即執行對應的動作

需要訪問實例的變量和調用實例的函數，當然需要對應的實例Instance對象本身
而Python中就規定好了，函數的第一個參數，就必須是實例對象本身，並且建議，約定俗成，把其名字寫為self
所以，我們需要self(需要用到self)
"""

# 定義Class(類)，example_1 =========================
"""
在Python中可以使用class關鍵字定義類，然後在類中通過之前學習過的函數來定義方法，這樣就可以將對象的動態特徵描述出來
"""

class Student(object):
    # __init__是一個特殊方法用於在創建對象時進行初始化操作
    # 通過這個方法我們可以為學生對象綁定name和age兩個屬性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在學習%s.' % (self.name, course_name))

# PEP 8要求標識符的名字用全小寫多個單詞用下劃線連接
# 但是部分程序員和公司更傾向於使用駝峰命名法(駝峰標識)
def watch_movie(self):
    if self.age < 18:
        print('%s只能觀看《熊出沒》.' % self.name)
    else:
        print('%s正在觀看島國愛情大電影.' % self.name)

# 創建學生對象並指定姓名和年齡
stu1 = Student('駱昊', 38)
# 給對象發study消息
stu1.study('Python程序設計')
# 給對象發watch_av消息
stu1.watch_movie()
stu2 = Student('王大錘', 15)
stu2.study('思想品德')
stu2.watch_movie()

"""
PEP8 Coding Style
因為 Python 是利用縮排來表示區塊的語言，所以已經確保 Coding Style 基本的一致性，但Windows 與 Linux 不一致的 Tab 間距則可能會破壞這樣的一致性
而為了進一步確保一致性，Python 在 PEP8 - Style Guide for Python Code 就闡明了詳細的 Coding Style
1. 以 4 個空格進行縮排(Use 4 spaces per indentation level)：利用 4 個空格取代 Tab
2. 限制每行最多 79 字元
3. 限制註解或者長字串不超過每行 72 字元
4. Import 模組應該 1 行 1 個
5. 模組名稱應儘量短，並全部小寫 (Modules should have short, all-lowercase names)
6. 類別名稱應使用 CapWords 命名 (Class names should normally use the CapWords convention)
7. 類別名稱每個單字首字大寫
8. 函數名稱應使用小寫 (Function names should be lowercase)
9. 常數(Constants)應大寫，並以底線分割單字

駝峰命名法：
第一個單詞以小寫字母開始；從第二個單詞開始以後的每個單詞的首字母都採用大寫字母
例如：myFirstName、myLastName，這樣的變量名看上去就像駱駝峰一樣此起彼伏，故得名
"""
# 實際上，bank 中的函式操作，都是與傳入的 dict 實例，也就是代表帳戶狀態的物件高度相關，可以將原本bank.py的函數組織成一個類別
# 定義一個存款與取款的class(類) example_2 ======================
# 在 Account 類別中，__init__ 定義了物件的初始流程，取代了原本的 account 函式
class Account:
    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.balance = 0
        
    def deposit(self, amount): #存款動作: amount代表存入金額
        if amount <= 0:
            raise ValueError('must be positive')
        self.balance += amount
        
    def withdraw(self, amount): #取款動作: amount代表取款金額
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise RuntimeError('balance not enough')


# 定義完class之後，就可以寫一些存取款動作
acct1 = Account('123–456–789', 'Justin') #開一個帳戶
acct1.deposit(100)
acct1.withdraw(30)
print(acct1.balance) #餘額是 70

# 類別(Class)介紹 ============================================================
# 類別名稱的命名原則習慣上使用Pascal命名法，也就是每個單字字首大寫，不得使用空白或底線分隔單字
#範例一
class Cars:
    pass
#範例二
class MyCars:
    pass

# 物件(Object) ===============================================================
# 就是透過類別(Class)實際建立的實體，就像實際生產出來的汽車(例如：Mazda)。類別(Class)與物件(Object)的關係就像汽車設計圖與汽車實體。
# 在類別名稱後加上一對小括號，並指派給一個變數即可產生一個實例
# 建立Cars類別的物件
mazda = Cars()

# 建構式(Constructor) =========================================================
# 通常我們會在建構式(Constructor)中初始化物件(Object)的屬性值(Attribute)
# 物件初始的設定，在產生物件時可以一併設定屬性，在類別裡加上 __init__() 初始方法，在產生實例時就會自動執行
def __init__(self, color, seat):
    self.color = color  # 顏色屬性
    self.seat = seat  # 座位屬性

# 方法(Method) ================================================================
# 定義方法(Method)和函式(Function)的語法很像，都是def關鍵字開頭，接著自訂名稱
# 但是方法(Method)和建構式(Constructor)一樣至少要有一個self參數
def drive(self):
    print(f"My car is {self.color} and has {self.seat} seats.")

# 最後我們把上面例子整理一下，就可以寫出一個汽車類別 ===================================
# 汽車類別
class Cars:
    # 建構式
    def __init__(self, color, seat):
        self.color = color  # 顏色屬性
        self.seat = seat  # 座位屬性

    # 方法(Method)
    def drive(self):
        print(f"My car is {self.color} and has {self.seat} seats.")

# 執行以下程式碼代入類別中
mazda = Cars("blue", 4)
mazda.drive()

# 類別中self的介紹 ====================================================
# Python規定，無論是構造方法還是例項方法，最少要包含一個引數，並沒有規定該引數的具體名稱。
# 之所以將其命名為 self，只是程式設計師之間約定俗成的一種習慣，遵守這個約定，可以使我們編寫的程式碼具有更好的可讀性（大家一看到 self，就知道它的作用）。
# 同一個類別可以產生多個物件，當某個物件呼叫類方法時，該物件會把自身的引用作為第一個引數自動傳給該方法，換句話說，Python 會自動繫結類方法的第一個引數指向呼叫該方法的物件。
class Person:
    name = "xxx"
    def __init__(self, name):
        self.name = name

print(Person.name)
zhangsan = Person("zhangsan")
print(zhangsan.name)
lisi = Person("lisi")
print(lisi.name)

# 訪問可見性問題 =========================================
# https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/08.%E9%9D%A2%E5%90%91%E5%AF%B9%E8%B1%A1%E7%BC%96%E7%A8%8B%E5%9F%BA%E7%A1%80.md