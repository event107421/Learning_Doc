# for迴圈介紹 ====================================================
"""
循環結構
如果在程序中我們需要重複的執行某條或某些指令
比如在我們的程序中要實現每隔1秒中在屏幕上打印一個"hello, world"這樣的字符串並持續一個小時，我們肯定不能夠將print('hello, world')這句代碼寫上3600遍
如果真的需要這樣做，那麼編程的工作就太無聊了。因此，我們還需要了解一下循環結構，有了循環結構我們就可以輕鬆的控制某件事或者某些事重複、重複、再重複的去執行。
在Python中構造循環結構有兩種做法，一種是for-in循環，一種是while循環。
"""

# 用for循環實現1~100求和 =======================

sum = 0  # 先產生一個變數讓for回權可以使用這個變數進行迭代
for x in range(101):
    sum += x
print(sum)

"""
range(101)可以產生一個0到100的整數序列。
range(1, 100)可以產生一個1到99的整數序列。
range(1, 100, 2)可以產生一個1到99的奇數序列，其中的2是數值序列的增量。
"""

# 猜數字遊戲 ===================================
"""
電腦出一個1~100之間的隨機數由人來猜
電腦根據人猜的數字分別給出提示大一點/小一點/猜對了
"""

import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('請輸入: '))
    if number < answer:
        print('大一點')
    elif number > answer:
        print('小一點')
    else:
        print('恭喜你猜對了~')
        break
print('你總共猜了%d次' % counter)
if counter > 7:
    print('你的智商餘額不足')

"""
上面的代碼中使用了break關鍵字來提前終止循環，需要注意的是break只能終止它所在的那個循環，這一點在使用嵌套的循環結構需要引起注意。
除了break之外，還有另一個關鍵字是continue，它可以用來放棄本次循環後續的代碼直接讓循環進入下一輪。
"""

# 輸出九九乘法表 ===================================
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()

"""
和分支結構一樣，循環結構也是可以嵌套的，也就是說在循環中還可以構造循環結構
"""

# 輸入一個正整數判斷它是不是質數 ====================
from math import sqrt

num = int(input('請輸入一個正整數: '))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是質數' % num)
else:
    print('%d不是質數' % num)

# 輸入兩個正整數計算最大公因數和最小公倍數 ===========
x = int(input('x = '))
y = int(input('y = '))
if x > y:
    x, y = y, x
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公因數是%d' % (x, y, factor))
        print('%d和%d的最小公倍數是%d' % (x, y, x * y // factor))
        break

# 打印各種三角形圖案
row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()

"""
# 在python內的for迴圈，當你只想要循環5次，不需要引用計數值，就可以直接使用_
for _ in range(5):
	print(_)
"""

# 將numbers內的每個元素做平方的處理，然後再用append一個一個加進空list內
numbers = [10, 20, 30]
squares = []
for number in numbers:
    squares.append(number ** 2)

# 上述for寫法也可以改成以下寫法，稱為for 包含式（comprehension)
numbers = [10, 20, 30]
squares = [number ** 2 for number in numbers]

# 至於 while，一般是用在結束條件不確定的情況下
print('Enter two numbers...')
m = int(input('Number 1: '))
n = int(input('Number 2: '))
while n != 0:
   r = m % n
   m = n
   n = r
print('GCD: {0}'.format(m))

# for也可以與條件式結合
numbers = [11, 2, 45, 1, 6, 3, 7, 8, 9]
odd_numbers = []
for number in numbers:
    if number % 2 != 0:
        odd_numbers.append(number)
print(odd_numbers)

#上述可以改寫成
numbers = [11, 2, 45, 1, 6, 3, 7, 8, 9]
print([number for number in numbers if number % 2 != 0])

# 也可以建立 dict 實例
names = ['caterpillar', 'justin', 'openhome']
passwds = [123456, 654321, 13579]
{name : passwd for name, passwd in zip(names, passwds)}