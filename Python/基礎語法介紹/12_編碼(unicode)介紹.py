# 在 Python 3.x 中，預設原始碼檔案必須是 UTF-8 編碼
text = '測試'
# 顯示 "<class 'str'>"
print(type(text))
# 顯示 2
print(len(text))

# Python內部的表示是unicode編碼
# encode表示將unicode編碼的字符串轉換成big5編碼
# decode表示將Big5編碼的字符串轉換成unicode編碼
'元'.encode('Big5')
'元'.encode('UTF-8')
'元'.encode('Big5').decode('Big5')

# 如果需在網頁進行關鍵字搜尋，需要把中文字符轉成網址可辨識的字符
import urllib

urllib.quote(u'中文測試'.encode('utf8'))