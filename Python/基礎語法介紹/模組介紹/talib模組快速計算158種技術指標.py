"""
mac安裝talib有許多坑，這邊紀錄一下
1.我們利用homebrew來安裝，所以在命令列中輸入：
brew install ta-lib

2.將剛剛安裝的ta-lib套件加入環境變數中
export TA_INCLUDE_PATH="$(brew --prefix ta-lib)/include"
export TA_LIBRARY_PATH="$(brew --prefix ta-lib)/lib"

3.接著利用homebrew安裝的python3來進行ta-lib套件安裝
python3 -m pip install ta-lib

做完以上步驟後，import talib試試，若還是出現類似錯誤訊息，如下：

4.再來就在命令列中輸入以下命令：
git clone https://github.com/mrjbq7/ta-lib.git
cd ta-lib
python3 setup.py install

5.接著我們debugging看看各個檔案是否存在，依次在命令列中輸入以下語法：
➜  which brew
/opt/homebrew/bin/brew

➜  brew --prefix ta-lib
/opt/homebrew/opt/ta-lib

➜  file $(brew --prefix ta-lib)/lib/libta_lib.dylib
/opt/homebrew/opt/ta-lib/lib/libta_lib.dylib: Mach-O 64-bit dynamically linked shared library arm64

➜  which python3
/opt/homebrew/bin/python3

➜  file /opt/homebrew/lib/python3.8/site-packages/talib/_ta_lib.cpython-38-darwin.so
/opt/homebrew/lib/python3.8/site-packages/talib/_ta_lib.cpython-38-darwin.so: Mach-O 64-bit bundle arm64

在Terminal中輸入以上命令後，若是跟上述結果一樣，就再import talib一次
"""

import numpy as np
import pandas as pd
import talib
import pymssql

# 透過『get_functions』語法，查看 TA-Lib 提供的所有技術指標的代碼
all_ta_label = talib.get_functions()
# 看一下清單
all_ta_label
# 共有 158 個技術指標可以運算
len(all_ta_label)

# 透過『get_function_groups』，取得分類後的技術指標清單
all_ta_groups = talib.get_function_groups()
# 看一下這個字典
all_ta_groups
# 有哪些大類別？
all_ta_groups.keys()
# 查看某類別底下的技術指標清單
all_ta_groups['Momentum Indicators']
# 查看所有類別的指標數量
table = pd.DataFrame({
            '技術指標類別名稱': list(all_ta_groups.keys()),
            '該類別指標總數': list(map(lambda x: len(x), all_ta_groups.values()))
        })
table

# 創建一個數據庫連接本機資料庫
conn = pymssql.connect(host = ".", database = "Investment")

# 先取出每日的資料
stock_price_daily_sql = ("SELECT Data_Date, yahoo_high_price AS high_price, yahoo_open_price AS open_price, yahoo_low_price AS low_price, yahoo_close_price AS close_price, yahoo_volum / 1000 AS trading_volum\
                                                    FROM stock_price\
                                                    WHERE 1 = 1\
                                                    AND stock_code = '8028'")

# 利用pandas的read_sql函數來做SQL語法的查詢
stock_price_daily = pd.DataFrame(pd.read_sql(stock_price_daily_sql, conn))
#显示所有行
pd.set_option("display.max_columns", None)

# 計算ADX
talib.ADX(stock_price_daily.high_price, stock_price_daily.low_price, stock_price_daily.close_price, timeperiod = 14)

# 計算RSI
talib.RSI(stock_price_daily.close_price, timeperiod = 6)

# 接下來我們可以利用get_functions來把所有技術指標名稱拉出來
# 然後利用for迴圈來將每個都計算出來

from talib import abstract

# 準備一份你想要計算並且併入 df 的技術指標清單
ta_list = ['MACD', 'SMA', 'STOCH']
# 這裡示範全部 158 種技術指標
ta_list = talib.get_functions()
# 裝執行錯誤的函數名稱
error_function = []

# 迴圈執行，看看結果吧！
for x in ta_list:
    try:
        # x 為技術指標的代碼，透過迴圈填入，再透過 eval 計算出 output
        output = eval('abstract.' + x + "(df[['open', 'high', 'low', 'close', 'volume']])")
        # 如果輸出是一維資料，幫這個指標取名為 x 本身；多維資料則不需命名
        output.name = x.lower() if type(output) == pd.core.series.Series else None
        # 透過 merge 把輸出結果併入 df DataFrame
        df = pd.merge(df, pd.DataFrame(output), left_on=df.index, right_on=output.index)
        df = df.set_index('key_0')
    except:
        error_function.append(x)