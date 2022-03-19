"""
分支結構
我們寫的Python代碼都是一條一條語句順序執行，這種代碼結構通常稱之為順序結構
然而僅有順序結構並不能解決所有的問題，比如我們設計一個遊戲，遊戲第一關的通關條件是玩家獲得1000分
那麼在完成本局遊戲後，我們要根據玩家得到分數來決定究竟是進入第二關，還是告訴玩家“Game Over”
這裡就會產生兩個分支，而且這兩個分支只有一個會被執行
類似的場景還有很多，我們將這種結構稱之為"分支結構"或"選擇結構"
"""


# 用戶身份驗證 ======================================
username = input('請輸入用戶名: ')
password = input('請輸入口令: ')
# 如果希望輸入口令時 終端中沒有回顯 可以使用getpass模塊的getpass函數
# import getpass
# password = getpass.getpass('請輸入口令: ')
if username == 'admin' and password == '123456':
    print('身份驗證成功!')
else:
    print('身份驗證失敗!')

"""
如果if條件成立的情況下需要執行多條語句，只要保持多條語句具有相同的縮進就可以了
換句話說連續的代碼如果又保持了相同的縮進那麼它們屬於同一個代碼塊，相當於是一個執行的整體。
當然如果要構造出更多的分支，可以使用if…elif…else…結構
"""

# 分段函數求值 ========================================
"""
        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
"""

x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))

"""
根據實際開發的需要，分支結構是可以嵌套的
例如判斷是否通關以後還要根據你獲得的寶物或者道具的數量對你的表現給出等級（比如點亮兩顆或三顆星星），那麼我們就需要在if的內部構造出一個新的分支結構
同理elif和else中也可以再構造新的分支，我們稱之為嵌套的分支結構
"""

# 所以上面的例子可以改成另外一種寫法
x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
else:
    if x >= -1:
        y = x + 2
    else:
        y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))

"""
但這就產生一個問題，Python之禪中有這麼一句話"Flat is better than nested."
之所以提倡代碼"扁平化"是因為嵌套結構的嵌套層次多了之後會嚴重的影響代碼的可讀性，所以能使用扁平化的結構時就不要使用嵌套。
"""

# 英制單位英寸和公制單位厘米互換 ============================
value = float(input('請輸入長度: '))
unit = input('請輸入單位: ')
if unit == 'in' or unit == '英寸':
    print('%f英寸 = %f厘米' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
    print('%f厘米 = %f英寸' % (value, value / 2.54))
else:
    print('請輸入有效的單位')

# 擲骰子決定做什麼 ===========================================
from random import randint

face = randint(1, 6)
if face == 1:
    result = '唱首歌'
elif face == 2:
    result = '跳個舞'
elif face == 3:
    result = '學狗叫'
elif face == 4:
    result = '做俯臥撑'
elif face == 5:
    result = '念繞口令'
else:
    result = '講冷笑話'
print(result)

"""
上面的代碼中使用了random模塊的randint函數生成指定範圍的隨機數來模擬擲骰子。
"""
import math

# 判斷輸入的邊長能否構成三角形，如果能則計算出三角形的周長和面積 ========
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('周長: %f' % (a + b + c))
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('面積: %f' % (area))
else:
    print('不能構成三角形')

"""
上面的代碼中使用了math模塊的sqrt函數來計算平方根。
"""

# ifelse介紹 ============================================================
# 在 Python 中，使用 : 來做為區塊（Block）開始的標示
# 在 Python 中要去判斷「哪些程式碼屬於某層級之下」不是使用大括號 {} ，而是使用縮排判斷

# 一般if else ===========================================================
# 若condition 為真 (True)，則執行 statement1；反之，則執行statement2
if condition:
    statement1 for True condition
else:
    statement2 for False condition

# 範例如下
from sys import argv
if len(argv) > 1:
    print('Hello,', argv[1])
else:
    print('Hello, Guest')

# Python 中的 if..else 也有運算式（Expression）形式，if 條件式成立的話，會傳回 if 左邊的值，否則傳回 else 右邊的值
# 上面的程式也可以寫為
from sys import argv
print('Hello,', argv[1] if len(argv) > 1 else 'Guest')

# 有的時候需要判斷的可能狀況有很多種時，這時候就可以使用 if-elif-else 結構來描述我們的需求 ===========================
score = int(input("score: "))
if score >= 90:
    print('Grade is: A')
elif score >= 80:
    print('Grade is: B')
elif score >= 70:
    print('Grade is: C')
elif score >= 60:
    print('Grade is: D')
else:
    print('Grade is: F')

# 巢狀if敘述 ===============================================================
ID = input()
year = int(ID[1:3])
if year < 4:
    print("Graduated")
elif year <= 7 and year >= 4:
    if year == 7:
        print("Freshman")
    elif year == 6:
        print("Sophomore")
    elif year == 5:
        print("Junior")
    elif year == 4:
        print("Senior")
else:
    print("Not Registered Yet")

