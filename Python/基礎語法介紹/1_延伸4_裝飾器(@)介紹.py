# @操作符是用來提供調用的 ===================================================
# 範例1 ============
# 從以下例子輸出可以看出，這個運算其實在一開始import進去就已經執行了，這也是 f1 f2 f2r這幾行會在start前面出現的原因
# 而在這個時候f2這個函數已經消失，f2在執行後已經變成字符串了，这就是後面print(f2("1"))會出錯的原因
# 也就是說，實際上前面def那些程式碼中 @ 操作符完成了以下步驟的操作：
# f2 = f1(f2())，所以在print(f2)才會顯示f2rf1，因為def f2內預設的return f2r結果已經代入f1的函數中
# 然後f2已經被f1(f2)的返回值所覆蓋了。運行f2的結果已經固定成字符串，使用參數也無法運行，或者說f2已經不是一個函數，無法帶入參數。
def f1(arg):
    print ("f1")
    rl = arg()
    print (rl)
    return rl + "f1"

@f1
def f2(arg = ""):
    print ("f2")
    return arg + "f2r"

print("start")
print(f2)
print(f2("1")) #出錯
print(f1(None))

# 範例2 ================
# 因程式實行的時候由上往下，先定義funA、funB，然後運行funA(funC())。
# 此時desA=funC()，然後funA()有參數就會输出It's funA
def funA(desA):
    print("It's funA")

def funB(desB):
    print("It's funB")

@funA
def funC():
    print("It's funC")

# 範例3 ================
# @funB修飾裝飾器@funA，@funA修飾函數funC()，將funC()賦予值给funA()做為參數，再將funA(funC())賦值给funB()
# 執行以下範例程式碼一樣由上往下執行，先定義funA、funB，然後運行funB(funA(funC()))
# 此時desA=funC()，然後funA()輸出'It's funA'
# 接著desB=funA(funC())，然后funB()輸出'It's funB'。
def funA(desA):
    print("It's funA")

def funB(desB):
    print("It's funB")

@funB
@funA
def funC():
    print("It's funC")

# 範例4 ================
# 接著我們改寫一下函數funA、funB，@funA修飾函數funC()，將funC()賦予值给funA()做為參數，可以看到funA打印結果<function funC at 0x10df87ca0>，代表真的有參數傳遞情形
# 接著一樣看一下，將funA(funC())赋值给funB()時，可以發現打印結果雖然第一個函數調用結果有出來，但是打印參數傳遞的結果是None。
# 那是否可以理解為'裝飾器' 修飾 '裝飾器'時，僅是調用函數而已。
def funA(desA):
    print("It's funA")
    print('---')
    print(desA)

def funB(desB):
    print("It's funB")
    print('---')
    print(desB)

@funB
@funA
def funC():
    print("It's funC")

# 範例5 ====================
# 也可以用類別來示範
class myDecorator(object):

    def __init__(self, f):
        print("inside myDecorator.__init__()")
        self.f = f

    def __call__(self):
        print("inside myDecorator.__call__()")
        self.f()

@myDecorator
def aFunction():
    print("inside aFunction()")

print("Finished decorating aFunction()")

print(aFunction())

# 接下來進入重點，python內建三個常用的裝飾器 ==============================================
# Python面向對象編程中，類中定義的方法可以是 @classmethod 裝飾的類方法，也可以是 @staticmethod 裝飾的靜態方法，用的最多的還是不帶裝飾器的實例方法
# 類中一共定義了3個方法，m1 是實例方法，第一個參數必須是 self（約定俗成的）。 m2 是類方法，第一個參數必須是cls（同樣是約定俗成），m3 是靜態方法，參數根據業務需求定，可有可無。當程序運行時，大概發生了這麼幾件事（結合下面的圖來看）。

# 實例方法 ========================================================
# 實例方法的第一個參數必須是"self"，實例方法只能通過類實例進行調用，這時候"self"就代表這個類實例本身。通過"self"可以直接訪問實例的屬性。
class person(object):
    tall = 180
    hobbies = []
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def infoma(self):
        print('%s is %s years old %s heights' % (self.name, self.age, self.weight))

Bruce = person("Bruce", 25, 180)
Bruce.infoma()

# 類方法 ================================
class person(object):
    tall = 180
    hobbies = []
    def __init__(self, name, age, weight):
        person.name = name
        person.age = age
        person.weight = weight

    @classmethod     # 類的裝飾器
    def infoma(cls):   # cls表示類本身
        print('%s is %s years old %s heights' % (cls.name, cls.age, cls.weight))

# 直接調用類的裝飾器函數，通過cls可以訪問類的相關屬性
person.infoma()

# 也可以通過兩步驟來實現，第一步實例化person，第二步調用裝飾器
Bruce = person("Bruce", 25, 180)
Bruce.infoma()

# 靜態方法 ============================
# 與實例方法和類方法不同，靜態方法沒有參數限制，既不需要實例參數，也不需要類參數，定義的時候使用@staticmethod裝飾器。
# 同類方法一樣，靜態法可以通過類名訪問，也可以通過實例訪問
class person(object):
    tall = 180
    hobbies = []
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    @staticmethod    # 靜態方法裝飾器
    def infoma(name, age, weight):     # 沒有參數限制，既不要實例參數，也不用類參數
        print('%s is %s years old %s heights' % (name, age, person.tall))
        print(weight)
        print(person.hobbies)

# 靜態方法也可以透過類名來訪問
person.infoma("Bruce", 25, 180)

# 通過實例方法來訪問
Bruce.infoma("Bruce", 25, 180)

# 這三種方法的主要區別在於參數，實例方法被綁定到一個實例，只能通過實例進行調用；但是對於靜態方法和類方法，可以通過類名和實例兩種方式進行調用