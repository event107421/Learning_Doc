# -*- coding: utf-8 -*-
# sys 模組提供多個 Python 執行時的環境變數, 而 sys.argv() 是儲存執行指令的陣列, 第一個元素是程式本身。
# import sys
#
# n = len(sys.argv)
# for i in range(0, n):
#     print(sys.argv[i])

# 通過python編寫的大型代碼往往需要在服務器中運行，而服務器中往往不會安裝IDE，所以只能在控制台通過python yourcode.py使程序執行
# 如果程序中有參數需要調整，通過文本編輯器到程序裡去調整參數十分麻煩，並且不能保證代碼的一致性
# 所以就可以透過sys.argv來做輸入參數，執行程式的方法
# 以下程式碼需透過Terminal直接執行
import sys

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        a = sys.argv[1]
        b = sys.argv[2]
    elif len(sys.argv) == 2:
        a = sys.argv[1]
        b = input("请输入参数b ")
    elif len(sys.argv) == 1:
        a = input("请输入参数a ")
        b = input("请输入参数b ")

    print(a + b)
    print(sys.argv)

"""
sys.argv是命令行參數，既然提到命令行，那麼使用它時需要在命令行下，如Windows下的cmd（命令提示符）窗口下或Linux下的終端（Terminal）。
不能再IDE環境（Pycharm等編譯器）下使用，即使使用也只能用sys.argv[0]，因為在IDE下其他的argv只是系統參數，不能自己設置
sys.argv[]說白了就是一個從程序外部獲取參數的橋樑，從外部取得的參數可以是多個，所以獲得的是一個列表（list)
也就是說sys.argv其實可以看作是一個列表，所以才能用[]提取其中的元素。其第一個元素是程序本身，隨後才依次是外部給予的參數
"""

"""
我們可以在外部的Terminal輸入以下命令來運行此py檔：
1.我們先單純運行test.py，因此時病外有其他的參數，所以len(sys.argv) == 1，那sys.argv[0]就為程式本身的名稱
python3 test2.py

2.接著我們多增加一個參數，此時len(sys.argv) == 2，我們有sys.argv[0]為程式本身的名稱外，我們多了一個sys.argv[1]為我們在外部命令設定的日期字串'2021-06-21'
python3 test2.py '2021-06-21'

3.再來又多增加一個參數，此時len(sys.argv) == 3，我們有sys.argv[0]為程式本身的名稱外，我們多了兩個sys.argv[1]、sys.argv[2]為我們在外部命令設定的日期字串'2021-06-21'、'2021-06-22'
python3 test2.py '2021-06-21' '2021-06-22'
"""

import sys
import datetime

if __name__ == '__main__':

    if len(sys.argv) == 3:
        begin = datetime.datetime.strptime(sys.argv[1], "%Y-%m-%d")
        end = datetime.datetime.strptime(sys.argv[2], "%Y-%m-%d")
        a = sys.argv[0]
        b = sys.argv[1]
        c = sys.argv[2]
        print(a)
        print(b)
        print(c)
        print(begin)
        print(end)

    elif len(sys.argv) == 2:
        end = datetime.datetime.strptime(sys.argv[1], "%Y-%m-%d")
        begin = end
        a = sys.argv[0]
        b = sys.argv[1]
        print(a)
        print(b)
        print(begin)
        print(end)

    elif len(sys.argv) == 1:
        end = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) - datetime.timedelta(1)
        begin = end
        a = sys.argv[0]
        print(a)
        print(begin)
        print(end)


# *arg：表示任意多個無名參數，類型為tuple
# 透過 * 收集的引數會被放到一個 tuple 中，所以我們可以使用 for 來對它進行迭代
# 函數使用可變參數 ==============================
"""
其實上面的add函數還有更好的實現方案，因為我們可能會對0個或多個參數進行加法運算
而具體有多少個參數是由調用者來決定，我們作為函數的設計者對這一點是一無所知的
因此在不確定參數個數的時候，我們可以使用可變參數，這時就可以將上面函數進行改寫
"""

# 在參數名前面的*表示args是一個可變參數
# 即在調用add函數時可以傳入0個或多個參數
def add(*args):
    total = 0
    for val in args:
        total += val
    return total


print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9))

def plus(a, b, c=None):
    res = a + b + (c if c else 0)
    return res

def plus_1(*nums):
    res = 0
    for i in nums:
        res += i
    return res

print(plus_1(1, 2, 3))

# **kwargs參數說明 ====================================
"""
參名前加兩個*表示，參數在函數內部將被存放在以形式名為標識符的 dictionary 中
這時調用函數的方法則需要採用 arg1 = value1, arg2 = value2 這樣的形式
所以為了區分兩個不定參數，我們可以把 *args 稱作為數組參數，**kwargs 稱作為字典參數
用以下函數來說明
def kwargsFunc(**kwargs):
    print kwargs

此時，我們在kwargsFunc這個函數輸入參數就要用以下形式來做輸入

kwargsFunc(x = 1, y = 2, z = 3)

這時我們就會得到結果：{'y': 2, 'x': 1, 'z': 3} #存放在字典中

那這時如果我們用輸入*args的形式來輸入就會產生錯誤，例如我們輸入：

kwargsFunc(1,2,3)

這時程式就會報錯誤訊息，因為不能傳遞數組參數
"""

# **kwargs：關鍵字引數 Keyword Argument，為dict
# 如果已經有一個dict,在參數前面加**，函數會把dict中所有鍵值對轉換為關鍵字參數傳進去
dt = {'sep': ' # ', 'end': '\n\n'}
print('hello', 'world', **dt)

# 雖然我們可以用上面的單星號來收集到一個 tuple 中，但這樣哪能知道第幾個元素代表什麼、也無法隨心所欲的選擇參數傳入了。
# 這時我們就可以再次利用 ** 以及 dict 「具名」的性質來定義函式
def fun(**_settings):
    print(_settings)

fun(name='Sky', attack=100, hp=500)

# 還可以順便先給定預設值
def fun(**settings):
    settings.setdefault('name', 'Hello')
    settings.setdefault('attack', 50)
    settings.setdefault('defense', 0)
    settings.setdefault('hp', 150)
    print(settings)

fun(name='Sky', attack=100, hp=500)

# 在函數中也可以將*arg、**kwargs一起使用
# 使用時需將*arg放在**kwargs之前，否則會有"SyntaxError: non-keyword arg after keyword arg"的語法錯誤
def foo(*args, **kwarg):
    for item in args:
        print('In args:')
        print(item)

    for k,v in kwarg.items():
        print('In kwarg')
        print (k,v)
    print(30*'=')

foo(1, 2, 3, a=4, b=5)
