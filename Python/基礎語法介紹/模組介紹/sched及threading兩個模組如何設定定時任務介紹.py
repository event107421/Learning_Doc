"""
在一般寫程式時，除了寫完程式，若是想要定時執行此程式碼，無非是用linux系統中的crontab來做設定，依照規則定時去觸發執行程式碼
但我們也可以在程式內運用python自有的模組，設定固定的時間去做觸發程式的動作
"""
# sched模組 =========================================================================
# 通過sched模組可以實現通過自定義時間，自定義函式，自定義優先順序來執行函式
import time
import sched

schedule = sched.scheduler(time.time, time.sleep)

def func(string1, float1):
    print("now is", time.time(), " | output=", string1, float1)

print(time.time())

"""
schedule.enter(delay, priority, action, arguments)
delay：是一個整數或浮點數，代表多少秒後執行這個action任務
priority：是優先順序，0代表優先順序最高，1次之，2次次之，當兩個任務是預定在同一個時刻執行時，根據優先順序決定誰先執行。
action：就是你要執行的任務，可以簡單理解成你要執行任務的函式的函式名
arguments：是你要傳入這個定時執行函式名函式的引數，最好用括號包起來，如果只傳入一個引數的時候用括號包起來，該引數後面一定要加一個逗號，如果不打逗號，會出現錯誤。
"""
schedule.enter(2, 0, func, ("test1", time.time()))
schedule.enter(2, 0, func, ("test1", time.time()))
schedule.enter(3, 0, func, ("test1", time.time()))
schedule.enter(4, 0, func, ("test1", time.time()))

"""
此模組是通過最後執行run()程式碼來觸發所有定時任務，但這樣後面每個任務會一直被阻塞，直到所有任務全部執行結束
且每個任務在同一執行緒中執行，所以如果一個任務執行時間大於其他任務的等待時間，那麼其他任務會推遲任務的執行時間
但這樣保證沒有任務丟失，只是這些任務的呼叫時間會比設定的推遲
"""

schedule.run()
print(time.time())

"""
example2
"""

import sched
import time
from datetime import datetime
# 初始化sched模組的 scheduler 類
# 第一個引數是一個可以返回時間戳的函式，第二個引數可以在定時未到達之前阻塞。
schedule = sched.scheduler(time.time, time.sleep)
# 被週期性排程觸發的函式
def printTime(inc):
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    schedule.enter(inc, 0, printTime, (inc,))
# 預設引數60s
def main(inc=60):
    # enter四個引數分別為：間隔事件、優先順序（用於同時間到達的兩個事件同時執行時定序）、被呼叫觸發的函式，
    # 給該觸發函式的引數（tuple形式）
    schedule.enter(0, 0, printTime, (inc,))
    schedule.run()
# 10s 輸出一次
main(10)

# threading模組 =========================================================================
"""
通過運行sched套件已經知道其缺點，因為每個任務在同一執行緒中執行，所以如果一個任務執行時間大於其他任務的等待時間，那麼其他任務會推遲任務的執行時間
此時就可以換用threading，通過threading.Timer可以避免這個問題效果就是直接執行print(start)和print(end)，而定時任務會分開執行
"""
# example1
import time
from threading import Timer

def print_time(enter_time):
    print("now is", time.time(), "enter_the_box_time is", enter_time)

print(time.time())
Timer(5, print_time, (time.time(),)).start()
Timer(10, print_time, (time.time(),)).start()
print(time.time())

# example2
import datetime
import time

def doSth():
    print('test')
    # 假裝做這件事情需要一分鐘
    time.sleep(60)

def main(h=0, m=0):
    """h表示設定的小時，m為設定的分鐘"""
    while True:
        # 判斷是否達到設定時間，例如0:00
        while True:
            now = datetime.datetime.now()
            # 到達設定時間，結束內循環
            if now.hour==h and now.minute==m:
                break
            # 不到時間就等20秒之後再次檢測
            time.sleep(20)
        # 做正事，一天做一次
        doSth()

main()