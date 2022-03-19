"""
python正規表達式的模組
正規表達式(Regular Expression)是一種文字模式，包括普通字元（例如，a到z之間的字母）和特殊字元（稱為"元字元"）
正規表達式使用但個字串來描述、匹配一系列匹配某個句法規則的字串
"""

"""
正則字元簡單介紹
普通字元：
    普通字元包括沒有顯示指定為元字元的所有可列印和不可列印字元
    這包括所有大寫和小寫字母、所有數字、所有標點符號和一些其它符號

特殊字元：
    $：匹配輸入字串的結尾位置。如果設定了RegExp物件的Multline屬性，則$也匹配'\n'或'\r'。
    ()：匹配一個子表示式的開始和結束位置（匹配括號中的全部內容）。子表示式可以獲取供以後使用。
    *：匹配前面的子表示式零次或多次。
    +：匹配前面的子表示式一次或多次（至少有一次）。
    .：匹配除換行符\n之外的任何單詞。
    [ ]：匹配括號中一個字元，範圍描述 如[0-9 a-z A-Z]。
    ?：匹配前面的子表示式零次或一次，或指明一個非貪婪的限定。
    \：轉義字元，如*表示匹配*號。
    ^：匹配字串的開始位置（用在[ ]時，可以理解為取反，表示不匹配中括號中的字串）。
    {}：限定匹配的次數，如{n}表示匹配n個字元，{n,}表示至少匹配n個字元，{n,m}表示至少n個，最多m個（m和n均為非負整數）。
    |：兩項中取一項。

非列印字元：非列印字元也可以是正規表示式的組成部分。
    \b：匹配一個單詞邊界，即字與空格間的位置。（"This is Regex匹配單獨的單詞"is",正則就要寫成"\bis\b"）。
    \d：匹配數字。
    \w：匹配字母，數字，下劃線。
    \s：匹配空格。
    \B：非單詞邊界匹配。
    \D：匹配非數字。
    \W：匹配非（字母，數字，下劃線）。
    \S：匹配非空格。
量詞：
    量詞的三個重要概念
    貪婪(貪心)：如"*"字元，貪婪量詞會首先匹配整個字串，嘗試匹配時，它會選定儘可能多的內容，如果失敗則回退一個字元，然後再次嘗試，回退的過程就叫做回溯，它會每次回退一個字元，直到找到匹配的內容或者沒有字元可以回退。相比下面兩種貪婪量詞對資源的消耗是最大的。
    
    懶惰(勉強)：如"?"，懶惰量詞使用另一種方法匹配，它從目標的起始位置開始嘗試匹配，每檢查一個字元，並尋找它要匹配的內容，如此迴圈直到字串結尾處。
    
    佔有：如"+"，佔有量詞很像貪心式量詞，它會選擇儘可能多的內容，然後嘗試尋找匹配內容，但它只嘗試一次，不會回溯。就好比先抓一把石頭，然後從石頭中挑出黃金。
"""

import re

"""
解釋一下這個正則表示式的意思：r'[\':\s ,]*'
1：r指明這是一個正則表示式
2：[]內是一個字符集，字符集內的字元任何一個被匹配，都算匹配成功，比如r'a[bcd]e'，可以匹配到'abe'、'ace'、'ade'。
3：*代表匹配前一個字元0次或無限次。
4：\s代表的是空白字元，比如空格、換行符、製表符等等。
於是r'[\':\s ,]*'組合起來就是匹配字串中所有的的'（單引號）、\n（換行符）、：（冒號）、，（逗號）
最後re.sub(a, b, string)表示將string中a所匹配到的所有字元通通替換成b，我們這個例子就是將匹配到的'（單引號）、\n（換行符）、：（冒號）、，（逗號）通通替換成''（nothing）。
"""

a = 'eew \' eawr,2 fd\n sa:21'
# 前面r是正則表示式，匹配多種字元（串）
b = re.sub(r'[\':\s ,]*', '', a)
print(b)

"""
match 函數用法
re.match會從文本中的起始位置開始進行文字符的匹配，如果不是一開始第一個字符就匹配成功的話，就會直接返回一個none
簡單來說就是欲匹配的文本一開始就要符合我們定義的字符規則，不符合直接回傳none，符合就會回傳字符位置資訊

re.match(pattern, string, flags)
pattern: 匹配的規則，使用正則表達式的語法撰寫
string: 要進行匹配的字符串
flags: 設定一些正則表達式的匹配方式，像是規則是忽略大小寫，或使用UNICODE字符規則來解析字符等，如果沒有特別需求，可以忽略不寫 可以選擇的標誌，可以參考我上面有提到的正則表達式修飾符號
"""

text = 'https://matters.news/@CHWang'
text1 = 'Matters.news'

print(re.match('https', text))
# span(): 傳回匹配的（起始位置,結束位置）
print(re.match('https', text).span())
print(re.match('matters', text))
print(re.match('matters', text1))
print(re.match('matters', text1, flags=re.I))

# 也可以使用group()函數來獲取匹配的字符，而不是返回一個字符的位置
"""
groups()函數：
groups(): 將匹配好的字符組合起來，形成一個tuple元數組

group()函數：
group(num=0): 選擇第幾個匹配好的字符
group(): 匹配好後，會回傳一個tuple，會根據匹配成功的字符一組一組返回，但由於match方法只會回傳一組，所以只要寫group()就好，其他的話，若我們想要回傳第一組就寫group(0)，以此類推
"""

text = 'Jack lives in HsinChu and he is 25 years old, but ...'
match_result = re.match(r'(.*) lives in ([a-z]*) and he is (\d+).*', text, re.I)

print(match_result.group())
print(match_result.group(1))
print(match_result.group(2))
print(match_result.group(3))
print(type(match_result.groups()))
print(match_result.groups())

"""
search()函數用法：
re.search會搜尋整個字符串，然後找到匹配的字符並且傳回，如果失敗，沒有匹配到任何字符則傳回none
如果成功，就會傳回一個匹配的對象，就可以使用group()來取得匹配成功的字符

re.search(pattern, string, flags) 
參數的用法與match一樣
"""

text = 'https://medium.com/@chwang12341'
text1 = 'Medium.Com'

print(re.search('https://', text))
print(re.search('dium', text))
print(re.search('medium', text).span())
print(re.search('co', text1))
print(re.search('co', text1, flags=re.I).span())

# 也可以使用group()函數來獲取匹配的字符，而不是返回一個字符的位置
text = 'Jen likes to eat cake and drink coke, but ...'
match_result = re.search('(.*) likes to eat (\w+) and drink ([a-z]*)', text, re.I|re.M)

print(match_result.group())
print(match_result.group(1))
print(match_result.group(2))
print(match_result.group(3))
print(match_result.groups())

"""
findall()函數用法
re.findall會直接找尋所有匹配的字符，裝進串列後返回，如果沒有找到匹配的字符，就會回傳一個空的串列喔
另外，re.findall會匹配所有符合規則的字符，而re.search與re.match只會匹配一次而已喔

findall(pattern, string, pos, endpos)
pattern: 匹配的規則，使用正則表達式的語法來撰寫
string:欲進行匹配的字符串
pos: 可選擇的參數，不一定要寫，指定開始匹配的位置，預設為0，也就是起始字符的位置
endpos: 可以選擇的參數，不一定要添加，指定結束匹配字符串的位置
"""

find_pattern = re.compile(r'[a-z]+', re.I)

match_result1 = find_pattern.findall('good 66 day Tom_28 Yep')
match_result2 = find_pattern.findall('good98MMorning66 Jen666 Yeah', 6,20)

print(match_result1)
print(match_result2)

"""
sub()函數用法
匹配好字符後，將它替換成我們想要的字符，這個方法相當方便，我們在進行數據處理時，有時候會有一些多餘的不要的空格、符號等等，就可以透過這個方法來一次拿掉

re.sub(pattern, repl, string, count = 0, flags)
pattern: 匹配的規則，使用正則表達式的語法來撰寫
repl: 欲替換的字符，也可以用函數的形式傳入喔
string: 要進行匹配的字符串
count: 匹配好字符後，替換的最大數量，預設為0，表示要全部替換
flags: 設定一些正則表達式的方式，像是規則是否忽略大小寫、使用UNICODE字符規則來解析字符等，如果沒有特別需求可以忽略不寫 可以選擇的標誌，可以參考我上面有提到的正則表達式修飾符號喔
"""

text = 'Jack/25/1993 and Jen/23/1995'

# 把中間的and與空格拿掉，用&替換
sub_result1 = re.sub('\sand\s', '&', text)
print(sub_result1)

# 狀況一: 再把/拿掉
sub_result2 = re.sub('/', '', sub_result1)
print(sub_result2)

# 狀況二: 再把/拿掉，但只要拿掉前兩個
sub_result3 = re.sub('/', '', sub_result1, 2)
print(sub_result3)

# 狀況三：也可以使用函數傳入
text = 'Jack66Jen58Ken28,Cathy38'

# 將匹配好的數字做平方計算
def square(match_result):
    num = int(match_result.group('number'))

    return str(num ** 2)

# 給定我們匹配值一個名稱，用?P<name>
final_result = re.sub('(?P<number>\d+)', square, text)
print(final_result)

"""
finditer()函數用法
re.finditer的用法與re.findall相似，找到所有符合匹配規則的字符後，以迭代器的形式傳回

re.finditer(pattern, string, flags) 
"""

match_result = re.finditer(r'[a-z]+', '68Jack66Jen58Ken28,Cathy38', re.I)

for name in match_result:
  print(name.group())

"""
我們從上面幾個例子都有看到使用compile()函數，以下說明函數用法
compile()函數介紹：
re.compile可以幫助我們編譯正則表達式，並生成一個pattern對象，來供給match、search、findall函數使用
簡單來說，就是我們只要定義好一次正則表達式的規則，就能用這個定義好的pattern規則，來提供match、search、findall函數匹配字符

re.compile(pattern,flags=0)

pattern：編譯時用的表示式字串
flags：編譯標誌位，用於修改正規表示式，如：是否區分大小寫，多行匹配等
常用的flags有：
re.S(DOTALL)：使.匹配包括換行符在內的所有字元。
re.I(IGNORECASE)：匹配對大小寫不敏感。
re.L(LOCALE)：做本地化識別（locale-aware）匹配，法語等。
re.M(MULTILINE)：多行匹配，影響^和$。
re.X(VERBOSE)：該標誌通過給予更靈活的格式以便將正規表示式寫的更易於理解。
re.U：根據Unicode字符集解析字元，這個標誌影響\w、\W、\b、\B
"""

# 範例一： ==================================================
text = '68Jack66Jen58Ken28,Cathy38'

# 匹配字母，並忽略大小寫
pattern = re.compile(r'([a-z]+)', re.I)

# match預設從第一個位置開始匹配
compile_result1 = pattern.match(text)
# None，因為match會從第一個位置開始匹配，如果不通過就會返回none
print(compile_result1)

# 從第3個位置開始匹配
compile_result2 = pattern.match(text, 2, 20)
print(compile_result2)
print(compile_result2.group(0))
# start(): 起始位置，傳入要查詢的組別，像是第一組就寫start(0)，以此類推
print(compile_result2.start(0))
# end(): 結束位置，傳入要查詢的組別，像是第一組就寫end(0)，以此類推
print(compile_result2.end(0))
print(compile_result2.span())

# 範例二： ==================================================
pattern = re.compile("\\d+")

# None（從頭部開始匹配）
match = pattern.match("aaa123bbb123ccc123")
print(match)

# <_sre.SRE_Match object; span=(3, 6), match='123'>
match = pattern.match("aaa123bbb123ccc123", 3, 6)
print(match)

# 123,返回匹配的字串，如果需要獲得整個匹配的字串時，可以使用group()或者group(0)
print(match.group())
# 3,返回匹配的字串在整個字串的起始位置
print(match.start())
# 6,返回匹配的字串在整個字串的結束位置
print(match.end())
# (3, 6),返回（start(), end()）
print(match.span())

"""
split()函數用法
re.split將匹配的字符進行切割，並且回傳一組串列

re.split(pattern, string, maxsplit, flags)
pattern: 匹配的規則，使用正則表達式的語法撰寫
string: 欲進行匹配的字符串
maxsplit: 分割的次數，如maxsplit=1，代表分割一次，預設為0，表示不限分割次數
flags: 設定一些匹配的模式
"""

text = 'Jack66Jen58Ken28Cathy'

# 用數字來做為分隔依據
print(re.split('\d+', text))

# 分隔，並將數字也傳進陣列
print(re.split('(\d+)', text))

# 如果匹配的一句剛好在前後的位置，就會傳回空值
text1 = '66Jack66Jen58Ken28Cathy38'
print(re.split('\d+', text1))

# 如果找不到匹配會回串全部字串
print(re.split('\s+', text1))

"""
注意：
匹配時將我們需要爬取的數據，用（）來包住它的匹配規則，才會被獨立出來放入串列
舉個例子來說，我們想要爬取文本字符串中符合我們指定格式的字符串，但是我們只想要取得|Example_format|前後的數值，並分別放入串列，這時候我們就需要將它們括號起來，像是(\d+)|Example_format|(\d+)這樣
如下：
"""

text = '6658|Example_format|2020'
print(re.findall(r'(\d+)(?:\WExample_format\W)(\d+)', text))
