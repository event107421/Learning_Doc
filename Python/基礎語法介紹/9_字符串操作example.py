# 去空格及特殊符號
s.strip()
s.lstrip()
s.rstrip(',')

# 複製字符串
# strcpy(sStr1, sStr)
sStr = 'strcpy'
sStr = sStr
sStr = 'strcpy'
print(sStr)

# 連接字符串
# strcat(sStr1, sStr)
sStr = 'strcat'
sStr = 'append'
sStr += sStr
print(sStr)

# 查找字符
# strchr(sStr1, sStr)
sStr = 'strchr'
sStr = 's'
nPos = sStr1.index(sStr)
print(nPos)

# 比較字符串
# strcmp(sStr1, sStr)
sStr = 'strchr'
sStr = 'strch'
print(cmp(sStr1, sStr))

# 掃描字符串是否包含指定的字符
# strspn(sStr1, sStr)
sStr = '1345678'
sStr = '456'
# sStrand chars both in sStrand sStr
print(len(sStrand sStr))

# 字符串長度
# strlen(sStr1)
sStr = 'strlen'
print(len(sStr1))

# 將字符串中的大小寫轉換
# strlwr(sStr1)
sStr = 'JCstrlwr'
sStr = sStr1.upper()
# sStr= sStr1.lower()
print(sStr)

# 追加指定長度的字符串
# strncat(sStr1, sStr, n)
sStr = '1345'
sStr = 'abcdef'
n = 3
sStr += sStr[0:n]
print(sStr)

# 字符串指定長度比較
# strncmp(sStr1, sStr, n)
sStr = '1345'
sStr = '13bc'
n = 3
print(cmp(sStr1[0:n], sStr[0:n]))

# 複製指定長度的字符
# strncpy(sStr1, sStr, n)
sStr = ''
sStr = '1345'
n = 3
sStr = sStr[0:n]
print(sStr)

# 將字符串前n個字符替換為指定的字符
# strnset(sStr1, ch, n)
sStr = '1345'
ch = 'r'
n = 3
sStr = n * ch + sStr1[3:]
print(sStr)

# 掃描字符串
# strpbrk(sStr1, sStr)
sStr = 'cekjgdklab'
sStr = 'gka'
nPos = -1
for c in sStr1:
    if c in sStr:
        nPos = sStr1.index(c)
        break
print(nPos)

# 翻轉字符串
# strrev(sStr1)
sStr = 'abcdefg'
sStr = sStr1[::-1]
print(sStr)

# 查找字符串
# strstr(sStr1,sStr)
sStr = 'abcdefg'
sStr = 'cde'
print(sStr1.find(sStr))

# 分割字符串
# strtok(sStr1, sStr)
sStr = 'ab,cde,fgh,ijk'
sStr = ','
sStr = sStr1[sStr1.find(sStr) + 1:]
print(sStr)

s = 'ab,cde,fgh,ijk'
print(s.split(','))

# 連接字符串
delimiter = ','
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))

def addslashes(s):
    d = {'"': '\\"', "'": "\\'", "\0": "\\\0", "\\": "\\\\"}

    return ''.join(d.get(c, c) for c in s)

s = "John 'Johny' Doe (a.k.a. \"Super Joe\")\\\0"
print(s)
print(addslashes(s))

# 只顯示字母與數字
def OnlyCharNum(s, oth=''):
    s = s.lower();

    fomart = 'abcdefghijklmnopqrstuvwxyz013456789'
    for c in s:
        if not c in fomart:
            s = s.replace(c, '')

    return s

print(OnlyStr("a000 aa-b"))

# 百分比(%) ====================================================================
# 為Python最早格式化字串的方法，透過%運算符號，將在tuple中的一組變數依照指定的格式化方式輸出。
# 如格式化: 字串(%s)、 十進位整數(%d)、浮點數(%f)等。
# 缺點:不適合多個變數、可讀性低
print('%d' % 20) # 格式化整數
print('%f' % 1.11)  # 預設保留6位小數
print('%.1f' % 1.11)  # 取1位小數
print('My name is %s' % 'tom') # 格式化字串

# str.format() => '{}'.format() ===============================================
# 使用大括號{}作為特殊字元，放在目標字串的指定位置，format()中則放入要拼接的變數、字串或數值。
# 範例1:不指定順序
# 缺點:當變數太多時，要撰寫的程式碼就會過長
name = "tom"
age = 20
strr = "my name is {} and my age is {}".format(name, age)
strr

# 範例2:指定順序、只要在{}內加入索引值(index)即可。
name = "tom"
age = 20
strr = "my name is {1} and my age is {0}".format(age, name)
strr

# str-formatting 除了可以指定格式化變數名稱及它的位置外，亦可調整輸出樣式，只要加入^（置中）、<（向左對齊）、>（向右對齊）等字元。
# 向右對齊
print('{:>10}'.format('test'))

# 向左對齊
print('{:10}'.format('test'))
# 等同
print('{:<10}'.format('test'))

# 置中
print('{:^10}'.format('test'))

# 調整輸出樣式，以'{:,}'的方式以逗號分隔數字
print('{:,}'.format(243554543))

# 將list串列值代入
print('The student is {students[1]}'.format(students = ['Tom', 'Jack', 'Amy']))

# 分開字串，可使用*方法分開字串
print('{} {} {} {} {} {}'.format(*'123456'))

# dic字典值代入，需在每個物件前面加上**
print('My age is {age} and gender is {gender}'.format(**{'age':20}, **{'gender':"female"}))

# f-string ======================================================================
# Python3.6+方可使用，只需要在字串前面加個f即可進行格式化，並將{}填入目標變數。
name = "tom"
age = 20
strr = f"my name is {name} and my age is {age}"
strr

# 可放表達式與呼叫函數:{}可以填入表達式或呼叫函數，Python會回傳求出的結果並填入字串內
print(f'A total number of {100 * 2 + 20}')

print(f'Complex number {(2 + 2j) / (2 - 3j)}')

print(f'convert STUDENT to lower words are {"STUDENT".lower()}')

import math
print(f'The answer is {math.log(math.pi)}')

score = 90
print(f'My score is {score}, so I am  {"good" if score > 80 else "bad"}.')

# 將list串列值代入
students=['Tom', 'Jack','Amy']
print(f'The student is {students[1]}')

# dic字典值代入
dic = {'name': "Tom",
       'age':20,
       'gender': "female"
      }
print(f'My name is {dic["name"]}, age is {dic["age"]} and gender is {dic["gender"]}')

# 大括號({})與跳脫字元
pens = 3
print(f'I have {pens} pens.')
# 引入tab 跳脫字元
print(f'I\thave \t{pens}\t pens.')
# 雙大括號 => 如果需要顯示大括號，則應輸入連續兩個大括號{{和}}
print(f'I have {pens} {{pens}}.')

# f-string大括號內所用的引號不能和大括號外的引號定義的符號相衝突，可依使用情況切換''和""。
# SyntaxError: invalid syntax 範例
print(f'I am {'Tom'}')
print(f"He said {"I'm Tom"}")
print(f'He said {"I'm Tom"}')

# 正確範例
print(f'I am {"Tom"}')
print(f"""He said {"I'm Tom"}""")
print(f'''He said {"I'm Tom"}''')

# backslash斜槓(\)的使用:大括號外的引號可以使用\，但大括號內不能使用\
print(f'''He\'ll say {"I'm Tom"}''')

name = "I\'m Tom"
print(f'''He'll say {name}''')

# 分割千分位
num = 1234567890.0987
print(f'num is {num:f}' )
print(f'num is {num:,f}' )

# lambda函數使用:大括號內也可放入lambda匿名函式，但lambda匿名函式的會被f-string誤判，為避免誤判的情況，需將lambda函式包在括號()內。
print(f"""even ? answer: {(lambda n : "Yes" if n %2 == 0 else "No") (10)}""")

# 樣板字串(Template String) =============================================================
# 需要從 Python 內建模組 string 引入Template
# 使用Template()包住目標字串，並使用錢$符號來標示變數
# 樣板字串預設使用錢$符號來標示變數
# 替換資料的格式為dictionary
# 最後使用substitute()來替換變數
from string import Template

s = Template('$who likes $what')
s.substitute(who='Tom', what='Python')

# 另外寫法
temp_str = '$who likes $what'
new = Template(temp_str)
dic = {'who': 'Tom', 'what': 'Python'}
new.substitute(dic)

### 最後總結 ===============================================================
### 雖然前面提到的str.format方法方便，但是很有可能在面對處理使用者輸入的值時，遭到惡意字元的注入，來看個範例:

# 金鑰、密碼、token等等
SECRET = 'this-is-a-secret'
class Error:
    def __init__(self):
        pass

# 使用者輸入惡意字元
user_input = '{error.__init__.__globals__[SECRET]}'
err = Error()
user_input.format(error=err)

### 如果改成Template String寫法，會得到一個ValueError的錯誤結果，較能有效防止洩漏機密資訊。
SECRET = 'this-is-a-secret'
class Error:
    def __init__(self):
        pass

# 使用者輸入惡意字元
user_input = '${error.__init__.__globals__[SECRET]}'
Template(user_input).substitute(error=err)

### 綜合以上的方法，可依照不同時機點，建議使用不同格式化字串的方式，下面簡單做個整理：
### 面對User輸入的字元，使用Template String，避免惡意腳本注入
### 非User輸入的字元，如果使用Python3.6以下的版本，採用str.format
### 非User輸入的字元且使用Python3.6以上的版本，推薦使用f-string方法

var1 = 'Hello World!'
var2 = "Runoob"

print("var1[0]: ", var1[0])
print("var2[1:5]: ", var2[1:5])

# 可以截取字符串的一部分并与其他字段拼接

var1 = 'Hello World!'

print("已更新字符串 : ", var1[:6] + 'Runoob!')

# \(在行尾時)：續行符
# \\：反斜杠符號
# \'：單引號
# \"：雙引號
# \a：響鈴
# \b：退格(Backspace)
# \e：轉義
# \000：空
# \n：換行
# \v：縱向製表符
# \t：橫向製表符
# \r：回車
# \f：換頁

# 字符串運算符
a = "Hello"
b = "Python"

print("a + b 輸出結果：", a + b)
print("a * 2 輸出結果：", a * 2)
print("a[1] 輸出結果：", a[1])
# 截取字符串中的一部分，遵循左閉右開原則，str[0,2] 是不包含第 3 個字符的
print("a[1:4] 輸出結果：", a[1:4])

# in:成員運算符 - 如果字符串中包含給定的字符返回 True
if ("H" in a):
    print("H 在變量 a 中")
else:
    print("H 不在變量 a 中")

# not in:成員運算符 - 如果字符串中不包含給定的字符返回 True
if ("M" not in a):
    print("M 不在變量 a 中")
else:
    print("M 在變量 a 中")

print(r'\n')
print(R'\n')

# 字符串格式化
print("我叫 %s 今年 %d 歲!" % ('小明', 10))

# %c：格式化字符及其ASCII碼
# %s：格式化字符串
# %d：格式化整數
# %u：格式化無符號整型
# %o：格式化無符號八進制數
# %x：格式化無符號十六進制數
# %X：格式化無符號十六進制數（大寫）
# %f：格式化浮點數字，可指定小數點後的精度
# %e：用科學計數法格式化浮點數
# %E：作用同%e，用科學計數法格式化浮點數
# %g：%f和%e的簡寫
# %G：%f 和 %E 的簡寫
# %p：用十六進制數格式化變量的地址

# 三引號允許一個字符串跨多行，字符串中可以包含換行符、製表符以及其他特殊字符
para_str = """這是一個多行字符串的實例
多行字符串可以使用製表符
TAB ( \t )。
也可以使用換行符 [ \n ]。
"""
print(para_str)

# 將字符串的第一個字符轉換為大寫
capitalize()

# 返回一個指定的寬度 width 居中的字符串，fillchar 為填充的字符，默認為空格。
center(width, fillchar)

# 返回 str 在 string 裡面出現的次數，如果 beg 或者 end 指定則返回指定範圍內 str 出現的次數
count(str, beg=0, end=len(string))

# Python3 中沒有 decode 方法，但我們可以使用 bytes 對象的 decode() 方法來解碼給定的 bytes 對象，這個 bytes 對象可以由 str.encode() 來編碼返回。
bytes.decode(encoding="utf-8", errors="strict")

# 以 encoding 指定的編碼格式編碼字符串，如果出錯默認報一個ValueError 的異常，除非 errors 指定的是'ignore'或者'replace'
encode(encoding='UTF-8', errors='strict')

# 檢查字符串是否以 obj 結束，如果beg 或者 end 指定則檢查指定的範圍內是否以 obj 結束，如果是，返回 True,否則返回 False.
endswith(suffix, beg=0, end=len(string))

# 把字符串 string 中的 tab 符號轉為空格，tab 符號默認的空格數是 8 。
expandtabs(tabsize=8)

# 檢測 str 是否包含在字符串中，如果指定範圍 beg 和 end ，則檢查是否包含在指定範圍內，如果包含返回開始的索引值，否則返回-1
find(str, beg=0
end = len(string))

# 跟find()方法一樣，只不過如果str不在字符串中會報一個異常.
index(str, beg=0, end=len(string))

# 如果字符串至少有一個字符並且所有字符都是字母或數字則返 回 True,否則返回 False
isalnum()

# 如果字符串至少有一個字符並且所有字符都是字母則返回 True, 否則返回 False
isalpha()

# 如果字符串只包含數字則返回 True 否則返回 False..
isdigit()

# 如果字符串中包含至少一個區分大小寫的字符，並且所有這些(區分大小寫的)字符都是小寫，則返回 True，否則返回 False
islower()

# 如果字符串中只包含數字字符，則返回 True，否則返回 False
isnumeric()

# 如果字符串中只包含空白，則返回 True，否則返回 False.
isspace()

# 如果字符串是標題化的(見 title())則返回 True，否則返回 False
istitle()

# 如果字符串中包含至少一個區分大小寫的字符，並且所有這些(區分大小寫的)字符都是大寫，則返回 True，否則返回 False
isupper()

# 以指定字符串作為分隔符，將 seq 中所有的元素(的字符串表示)合併為一個新的字符串
join(seq)

# 返回字符串長度
len(string)

# 返回一個原字符串左對齊,並使用 fillchar 填充至長度 width 的新字符串，fillchar 默認為空格。
ljust(width[, fillchar])

# 轉換字符串中所有大寫字符為小寫.
lower()

# 截掉字符串左邊的空格或指定字符。
lstrip()

# 創建字符映射的轉換錶，對於接受兩個參數的最簡單的調用方式，第一個參數是字符串，表示需要轉換的字符，第二個參數也是字符串表示轉換的目標。
maketrans()

# 返回字符串 str 中最大的字母。
max(str)

# 返回字符串 str 中最小的字母。
min(str)

# 把 將字符串中的 str1 替換成 str2,如果 max 指定，則替換不超過 max 次。
replace(old, new[, max])

# 類似於 find()函數，不過是從右邊開始查找.
rfind(str, beg=0, end=len(string))

# 類似於 index()，不過是從右邊開始.
rindex(str, beg=0, end=len(string))

# 返回一個原字符串右對齊,並使用fillchar(默認空格）填充至長度 width 的新字符串
rjust(width, [, fillchar])

# 刪除字符串字符串末尾的空格.
rstrip()

# num=string.count(str)) 以 str 為分隔符截取字符串，如果 num 有指定值，則僅截取 num 個子字符串
split(str="", num=string.count(str))

# 按照行('\r', '\r\n', \n')分隔，返回一個包含各行作為元素的列表，如果參數 keepends 為 False，不包含換行符，如果為 True，則保留換行符。
splitlines([keepends])

# 檢查字符串是否是以 obj 開頭，是則返回 True，否則返回 False。如果beg 和 end 指定值，則在指定範圍內檢查。
startswith(str, beg=0, end=len(string))

# 在字符串上執行 lstrip()和 rstrip()
strip([chars])

# 將字符串中大寫轉換為小寫，小寫轉換為大寫
swapcase()

# 返回"標題化"的字符串,就是說所有單詞都是以大寫開始，其餘字母均為小寫(見 istitle())
title()

# 根據 str 給出的表(包含 256 個字符)轉換 string 的字符, 要過濾掉的字符放到 deletechars 參數中
translate(table, deletechars="")

# 轉換字符串中的小寫字母為大寫
upper()

# 返回長度為 width 的字符串，原字符串右對齊，前面填充0
zfill(width)

# 檢查字符串是否只包含十進製字符，如果是返回 true，否則返回 false。
isdecimal()