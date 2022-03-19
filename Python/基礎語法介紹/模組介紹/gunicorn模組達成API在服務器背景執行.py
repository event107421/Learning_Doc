"""
Gunicorn 又稱綠色獨角獸(源於icon)是Python Web服務器網關接口HTTP服務器。
Gunicorn 服務器與許多Web框架廣泛兼容，並且實現簡單，佔用服務器資源少且速度相當快。
除此之外也能設定 cpu 的 worker 數量或是 thread 處理。
"""
# 先在terminal使用pip 來安裝 Gunicorn 套件，不是單純在python內安裝就好，是要在Terminal中執行
# sudo pip install gunicorn

# 範例run.py
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return 'hello !'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

"""
當我們創建了一個.py檔的API時
一般若是在teminal執行此py檔時，當把terminal視窗關閉，api就會跟著關閉，所以我們必須利用gunicorn套件來達成背景執行
此時我們在Terminal內輸入以下語法： sudo gunicorn -w 1 -b 0.0.0.0:80 run:app
上面的指令分成三部分，第一個部分為 -w 就是 worker 的個數，簡單來說就是同一個時間能夠處理(process)多少工作量。官方是建議一個 CUP 可以設置2-4個 worker。
-b 設定服務所綁定的端口，格式為 HOST:PORT。
最後一個為執行的程式名稱，假設我的檔名為 run.py 我就要在最後面加上 run:app。
執行後他會顯示目前你的運行狀態，另外每一個程序都會有一個 PID，如果我需要停止監聽這項服務就必須利用 kill 指令搭配此PID來結束程序。
例如我們可以在Terminal輸入 ps aux | grep gunicorn ，此段語法是查詢Gunicorn背景有哪些服務正在運行
接著如果我們要停止API運行，就可以利用kill指令，在Terminal輸入 sudo kill -9 12705，其中12705是那個運行API的PID
"""

