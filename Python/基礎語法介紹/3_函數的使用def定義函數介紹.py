"""
函數的作用
編程大師Martin Fowler先生曾經說過："代碼有很多種壞味道，重複是最壞的一種！"
要寫出高質量的代碼首先要解決的就是重複代碼的問題
"""

"""
定義函數
在Python中可以使用def關鍵字來定義函數，和變量一樣每個函數也有一個響亮的名字，而且命名規則跟變量的命名規則是一致的。
在函數名後面的圓括號中可以放置傳遞給函數的參數，這一點和數學上的函數非常相似，程序中函數的參數就相當於是數學上說的函數的自變量
而函數執行完成後我們可以通過return關鍵字來返回一個值，這相當於數學上說的函數的因變量
"""


# 求階乘 ================================
def factorial(num):
    """
    :param num: 非負整數
    :return: num的階乘
    """
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result


m = int(input('m = '))
n = int(input('n = '))
# 當需要計算階乘的時候不用再寫循環求階乘而是直接調用已經定義好的函數
print(factorial(m) // factorial(n) // factorial(m - n))

"""
Python的math模塊中其實已經有一個factorial函數了，事實上要計算階乘可以直接使用這個現成的函數而不用自己定義
下面例子中的某些函數其實Python中也是內置了，我們這裡是為了講解函數的定義和使用才把它們又實現了一遍，實際開發中不建議做這種低級的重複性的工作
"""

# 函數默認參數 ==============================
"""
在Python中，函數的參數可以有默認值，也支持使用可變參數，所以Python並不需要像其他語言一樣支持函數的重載
因為我們在定義一個函數的時候可以讓它有多種不同的使用方式，下面是兩個小例子
我們給下面兩個函數的參數都設定了默認值，這也就意味著如果在調用函數的時候如果沒有傳入對應參數的值時將使用該參數的默認值
所以在上面的代碼中我們可以用各種不同的方式去調用add函數，這跟其他很多語言中函數重載的效果是一致的。
"""

from random import randint


def roll_dice(n=2):
    """
    搖色子
    :param n: 色子的個數
    :return: n顆色子點數之和
    """
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    return a + b + c


# 如果沒有指定參數那麼使用默認值搖兩顆色子
print(roll_dice())
# 搖三顆色子
print(roll_dice(3))
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
# 傳遞參數時可以不按照設定的順序進行傳遞
print(add(c=50, a=100, b=200))

# 當發現到兩個程式片段極為類似，只有當中幾個計算用到的數值或變數不同時，可以使用函式來封裝程式片段，將流程中引用不同數值或變數的部份設計為參數
max1 = a if a > b else b
max2 = x if x > y else y
# 可以將上述程式改成函式
def max(a, b):
    return a if a > b else b
#將函式指向maximum
maximum = max
maximum(10, 20)

# 在 Python 中，可以使用 lambda 表示式來定義一個函式，這樣的函式稱為 λ 函式或是匿名函式（Anonymous function）
lambda a, b: a if a < b else b

# 也可以將其指定給變數
min = lambda a, b: a if a < b else b
minimum = min
min(10, 20) # 傳回10
minimum(10, 20) # 傳回10

# 實際上，def是個陳述句，Python執行到def時，會產生一個函式物件，為function的實例，即然函式是個物件，它可以指定給其它的變數
def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)

print(gcd(20, 30)) # 顯示 10

def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)

print(gcd(20, 30))         # 顯示 10
print(type(gcd))           # 顯示 <class 'function'>

gcd2 = gcd
print(gcd2(20, 30))        # 顯示 10
print(id(gcd), id(gcd2))   # 兩個顯示的數字相同

# 在下例中，如果沒有指定第三個參數c的值，則預設值是0
def sum(a, b, c = 0):
    return a + b + c

print(sum(10, 20, 30))   # 顯示 60
print(sum(10, 20))       # 顯示 30

# 事實上，在呼叫函式時，並不一定要依參數宣告順序來傳入引數，而可以指定參數名稱來設定其引數值，稱之為關鍵字引數
def sum(a, b, c = 0):
    return a + b + c

print(sum(c = 30, a = 10, b = 20))  # 顯示 60

# 像sum這種加總數字的需求，事先可能不知道要傳入的引數個數，可以在定義函式的參數時使用*，表示該參數接受不定長度引數
def sum(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(sum(1, 2))        # 顯示 3
print(sum(1, 2, 3))     # 顯示 6
print(sum(1, 2, 3, 4))  # 顯示 10

# 你傳入函式的引數，會被收集在一個Tuple中，再設定給numbers參數。有趣的是，如果你有個函式擁有固定的參數，你可以將一個Tuple傳入，只要在傳入時加上*，則Tuple中每個元素會自動指定給各個參數
def sum3(a, b, c):
    return a + b + c

numbers = (1, 2, 3)
print(sum3(*numbers))

# 如果函式參數個數固定，你也可以傳給函式一個字典物件，只要在物件前加上**，則Python會依字典物件的鍵名稱，將值指定給對應名稱的參數
def sum3(a, b, c):
    return a + b + c

args = {'a' : 1, 'b' : 2, 'c' : 3}
print(sum3(**args))

# 函式中還可以定義函式，稱之為區域函式（Local function），可以使用區域函式將某個函式中的演算組織為更小的單元
# 例如，在底下的範例中，尋找最小值的演算就實作為區域函式的方式
def selection(number):
    # 找出未排序中最小值
    def min(m, j):
        if j == len(number):
            return m
        elif number[j] < number[m]:
            return min(j, j + 1)
        else:
            return min(m, j + 1)

    for i in range(0, len(number)):
        m = min(i, i + 1)
        if i != m:
            number[i], number[m] = number[m], number[i]


number = [1, 5, 2, 3, 9, 7]
selection(number)
print(number)  # 顯示 [1, 2, 3, 5, 7, 9]

# 以下為定義函數要注意的事項 =======================
# 在Python中不支援其它語言函式重載的概念，也就是在Python中同一個名稱空間中，不能有相同的函式名稱，後者定義會覆蓋前者定義
def sum(a, b):
    return a + b

def sum(a, b, c):
    return a + b + c

# 使用預設值指定時，必須小心指定可變動物件時的一個陷阱
# 在上例中，你的 arr預設值設定為空串列，由於def是個陳述，執行到def的函式定義時，就建立了空串列物件，而這個物件會一直存在，如果你沒有指定arr的串列物件 時，所使用的就一直會是一開始指定的預設空串列物件，也因此，隨著每次呼叫都不指定arr的值，你附加的對象，都是同一個物件
def appendTo(element, arr = []):
    arr.append(element)
    return arr

appendTo(10, [1, 2, 3])
appendTo(10)
appendTo(20, [4, 5, 6])
appendTo(20)
appendTo(30)
appendTo(40)

# 可以在一個函式中，同時使用*與**
def some(*arg1, **arg2):
    print(arg1)
    print(arg2)
some(1, 2, 3)
some(a = 1, b = 22, c = 3)
some(2, a = 1, b = 22, c = 3)