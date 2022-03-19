# 編碼
# 默認情況下，Python 3 源碼文件以 UTF-8 編碼，所有字符串都是 unicode 字符串。當然你也可以為源碼文件指定不同的編碼
# 類似在程式碼最上頭加上這行
-*- coding: utf-8 -*-

# python保留字
# 保留字即關鍵字，我們不能把它們用作任何標識符名稱。 Python 的標準庫提供了一個 keyword 模塊，可以輸出當前版本的所有關鍵字
import keyword
keyword.kwlist

# 多行註釋可以用多個 # 號，還有 ''' 和 """
# 第一個註釋
# 第二個註釋
 
'''
第三註釋
第四註釋
'''
 
"""
第五註釋
第六註釋
"""
print ("Hello, Python!")

# 行與縮進
if True:
    print ("True")
else:
    print ("False")

if True:
    print ("Answer")
    print ("True")
else:
    print ("Answer")
  print ("False")    # 縮進不一致，會導致運行錯誤

# 多行語句
# Python 通常是一行寫完一條語句，但如果語句很長，我們可以使用反斜杠(\)來實現多行語句，例如：
total = item_one + \
        item_two + \
        item_three

# 在 [], {}, 或 () 中的多行語句，不需要使用反斜杠(\)，例如：
total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']
		
# 數字(Number)類型
# int (整數), 如 1, 只有一種整數類型 int，表示為長整型，沒有 python2 中的 Long。
# bool (布爾), 如 True。
# float (浮點數), 如 1.23、3E-2
# complex (複數), 如 1 + 2j、 1.1 + 2.2j

# 字符串(String)
# python中單引號和雙引號使用完全相同。
# 使用三引號('''或""")可以指定一個多行字符串。
# 轉義符 '\'
# 反斜杠可以用來轉義，使用r可以讓反斜杠不發生轉義。 。如 r"this is a line with \n" 則\n會顯示，並不是換行

word = '字符串'
sentence = "這是一個句子。"
paragraph = """這是一個段落，
可以由多行組成"""

str='Runoob'
 
print(str)                 # 輸出字符串
print(str[0:-1])           # 輸出第一個到倒數第二個的所有字符
print(str[0])              # 輸出字符串第一個字符
print(str[2:5])            # 輸出從第三個開始到第五個的字符
print(str[2:])             # 輸出從第三個開始的後的所有字符
print(str * 2)             # 輸出字符串兩次
print(str + '你好')         # 連接字符串
 
print('------------------------------')
 
print('hello\nrunoob')      # 使用反斜杠(\)+n轉義特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一個 r，表示原始字符串，不會發生轉義

