"""
在程式運行的過程中，換產生一些event或是message值得記錄下來做事後分析，python就有logging這個模組可以使用

logging level：logging 為開發者提供了 5 種程度不同的描述來紀錄訊息，分別是 debug、info、waring、error、critical，這五種的嚴重比較程度，如下：
CRITICAL > FATAL > ERROR / EXCEPTION > WARNING > WARN > INFO > DEBUG > NOTSET
"""

import logging
# 看完下面程式碼的執行結果，你可能會有疑問，為什麼 debug、info 的訊息沒有印出來呢?
# 這就跟 logger 的 level 有關係了。logger 有提供 level 可以過濾掉嚴重程度沒那麼高的 message。
logging.debug('Hello debug!')
logging.info('Hello info!')
logging.warning('Hello warning!')
logging.error('Hello error!')
logging.critical('Hello critical!')

# 舉例來說，如下面程式碼：
# 當我們把 logger 的 level 設為logging.INFO的時候，所有 debug() 的 message，將會被自動忽略，只有 info(), warning(), error(), critical() 才會處理。
# 如果我們把 level 設成logging.ERROR的時候，所有 debug(), info(), warning() 的訊息將會被忽略。
# 而在我們沒有設定 level 的時候，預設會是 logging.WARNING，但因為debug、info的level小於WARNING，這就是為什麼 debug、info 沒有印出來的原因。
logging.basicConfig(level=logging.INFO)
logging.debug('Hello debug!')
logging.info('Hello info!')
logging.warning('Hello warning!')
logging.error('Hello error!')
logging.critical('Hello critical!')

"""
basicConfig參數解釋：
filename：即日誌輸出的文件名，如果指定了這個信息之後，實際上會啟用 FileHandler，而不再是 StreamHandler，這樣日誌信息便會輸出到文件中了。
filemode：這個是指定日誌文件的寫入方式，有兩種形式，一種是 w，一種是 a，分別代表清除後寫入和追加寫入。
format：指定日誌信息的輸出格式(format的參數如下所示)：
    {
        %(levelno)s：打印日誌級別的數值。
        %(levelname)s：打印日誌級別的名稱。
        %(pathname)s：打印當前執行程序的路徑，其實就是sys.argv[0]。
        %(filename)s：打印當前執行程序名。
        %(funcName)s：打印日誌的當前函數。
        %(lineno)d：打印日誌的當前行號。
        %(asctime)s：打印日誌的時間。
        %(thread)d：打印線程ID。
        %(threadName)s：打印線程名稱。
        %(process)d：打印進程ID。
        %(processName)s：打印線程名稱。
        %(module)s：打印模塊名稱。
        %(message)s：打印日誌信息。
    }
datefmt：指定時間的輸出格式。
style：如果 format 參數指定了，這個參數就可以指定格式化時的佔位符風格，如 %、{、$ 等。
level：指定日誌輸出的類別，程序會輸出大於等於此級別的信息。
stream：在沒有指定 filename 的時候會默認使用 StreamHandler，這時 stream 可以指定初始化的文件流。指定將日誌的輸出流，可以指定輸出到sys.stderr，sys.stdout或者文件，默認輸出到sys.stderr，當stream和filename同時指定時，stream被忽略；
handlers：可以指定日誌處理時所使用的 Handlers，必須是可迭代的，與 filename & stream 不相容，無法共用。
"""

"""
自訂輸出的時間格式：
%Y：長年份，例如：2019
%y：短年份，例如：19
%m：月份：01 ~ 12
%B：月份完整名稱，例如：February
%b：月份縮寫名稱，例如：Feb
%d：日期：01 ~ 31
%H：小時 (24 小時制)：00 ~ 23
%I：小時 (12 小時制)：01 ~ 12
%w：星期：0 ~ 6，0 代表星期日
%A：星期完整名稱，例如：Friday
%a：星期縮寫名稱，例如：Fri
%P：AM 或 PM
%M：分鐘：00 ~ 59
%S：秒：00 ~ 61
"""

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M',
                    handlers=[logging.FileHandler('my.log', 'w', 'utf-8'), ])
logging.debug('Hello debug!')
logging.info('Hello info!')
logging.warning('Hello warning!')
logging.error('Hello error!')
logging.critical('Hello critical!')

# Handler的用法 ==================================
# 將日誌寫入到文件，這裡沒有使用 basicConfig 全局配置，而是，Logger 對象添加對應的 Handler 即可
# 最後可以發現日誌就會被輸出到 Alibaba.log 中
import logging
#先聲明一個 Logger 對象
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
#然後指定其對應的 Handler 為 FileHandler 對象
handler = logging.FileHandler('Alibaba.log')
#然後 Handler 對象單獨指定了 Formatter 對象單獨配置輸出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
# 在Alibaba.log日誌內寫入日誌訊息
logger.info('welcome to alibaba info')
logger.debug('Debugging')
logger.warning('Warning exists')
logger.info('Finish')
"""
logging 模塊提供的 Handler 有：
StreamHandler：logging.StreamHandler；日誌輸出到流，可以是 sys.stderr，sys.stdout 或者文件。
FileHandler：logging.FileHandler；日誌輸出到文件。
BaseRotatingHandler：logging.handlers.BaseRotatingHandler；基本的日誌回滾方式。
RotatingHandler：logging.handlers.RotatingHandler；日誌回滾方式，支持日誌文件最大數量和日誌文件回滾。
TimeRotatingHandler：logging.handlers.TimeRotatingHandler；日誌回滾方式，在一定時間區域內回滾日誌文件。
SocketHandler：logging.handlers.SocketHandler；遠程輸出日誌到TCP/IP sockets。
DatagramHandler：logging.handlers.DatagramHandler；遠程輸出日誌到UDP sockets。
SMTPHandler：logging.handlers.SMTPHandler；遠程輸出日誌到郵件地址。
SysLogHandler：logging.handlers.SysLogHandler；日誌輸出到syslog。
NTEventLogHandler：logging.handlers.NTEventLogHandler；遠程輸出日誌到Windows NT/2000/XP的事件日誌。
MemoryHandler：logging.handlers.MemoryHandler；日誌輸出到內存中的指定buffer。
HTTPHandler：logging.handlers.HTTPHandler；通過”GET”或者”POST”遠程輸出到HTTP服務器。
"""

# Formatter的用法
# 我們當然可以不借助於 basicConfig 來全局配置格式化輸出內容， Formatter 可以幫我們完成，每個 Handler 單獨配置輸出的格式
import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.WARN)
# 指定了一個 Formatter，並傳入了 fmt 和 datefmt 參數，這樣就指定了日誌結果的輸出格式和時間格式
formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y/%m/%d %H:%M :%S')
handler = logging.StreamHandler()
# handler 通過 setFormatter() 方法設置此 Formatter 對象即可
handler.setFormatter(formatter)
logger.addHandler(handler)

# 寫入日誌訊息
logger.debug('Debugging')
logger.critical('Critical Something')
logger.error('Error Occurred')
logger.warning('Warning exists')
logger.info('Finished')

# 捕獲 Traceback
# error() 方法中添加了一個參數，將 exc_info 設置為了 True，這樣我們就可以輸出執行過程中的信息了，即完整的 Traceback 信息
import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# FileHandler
file_handler = logging.FileHandler('result.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# StreamHandler
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# 紀錄堆疊追蹤資訊 ==========================================
# logging 模組也提供可以紀錄完整的堆疊追蹤 (stack traces)
# 若在 logging.error() 加上 exc_info 參數，並將該參數設為 True，就可以紀錄 Exception，如下程式碼：
"""
錯誤分為兩種：
1.語法錯誤：也叫做分析時的錯誤(parsing errors)，像一般在學Python時最常見到的直譯器所發出來的抱怨
2.例外情形(exceptions)：有的時候，就算你的語法完全正確，執行程式時仍然會出錯的情形，例外情況(Exception)有很多種類型，類型的名稱也在錯誤信息之中
"""
import logging

try:
    x = 5 / 0
except:
    logging.error("Catch an exception.", exc_info=True)

# 若沒有加上 exc_info=True 則無法紀錄 Exception：
import logging

try:
    x = 5 / 0
except:
    logging.error("Catch an exception.")

# 若要在 logging 內紀錄 exception 訊息，可使用 logging.exception()，它會將 exception 添加至訊息中
# 此方法的等級為 ERROR，也就是說 logging.exception() 就等同於 logging.error(exc_info=True)
# 輸出結果和 logging.error(exc_info=True) 相同
import logging

try:
    x = 5 / 0
except:
    logging.exception('Catch an exception.')

# 若不想使用 ERROR 級別紀錄 exception 訊息，可使用 DEBUG、INFO、WARNING、CRITICAL 級別並加上參數 exc_info=True 的設定
import logging

logging.basicConfig(level=logging.DEBUG)

try:
    x = 5 / 0
except:
    logging.debug('Catch an exception.', exc_info=True)
    logging.info('Catch an exception.', exc_info=True)
    logging.warning('Catch an exception.', exc_info=True)
    logging.critical('Catch an exception.', exc_info=True)

# Log 紀錄方式
logger.info('Start')
logger.warning('Something maybe fail.')
try:
    result = 10 / 0
except Exception:
    logger.error('Faild to get result', exc_info=True)
logger.info('Finished')

"""
但是如果錯誤發生在另外一支.py檔案裡面呢？
要怎麼知道Exception是發生在哪一支程式的哪一行，錯誤類型以及詳細內容又是什麼？？？這時候就要依靠sys與traceback套件來做這些事情
我們先定義一支新的.py程式叫做test.py，定義一個方法叫做run，再把a = 1 / 0移到方法裡面
"""
# 將以下程式碼存為test.py檔
# -*- coding: utf-8 -*-
def run():
    a = 1 / 0

# -*- coding: utf-8 -*-
import sys
import traceback
import test

try:
    test.run()
except Exception as e:
#    print(e)
    error_class = e.__class__.__name__ #取得錯誤類型
    detail = e.args[0] #取得詳細內容
    cl, exc, tb = sys.exc_info() #取得Call Stack
    lastCallStack = traceback.extract_tb(tb)[-1] #取得Call Stack的最後一筆資料
    fileName = lastCallStack[0] #取得發生的檔案名稱
    lineNum = lastCallStack[1] #取得發生的行號
    funcName = lastCallStack[2] #取得發生的函數名稱
    errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(fileName, lineNum, funcName, error_class, detail)
    print(errMsg)