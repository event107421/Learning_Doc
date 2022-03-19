"""
這邊順便介紹相對路徑以及絕對路徑
相對路徑的相對則是不完整路徑，這個相對指的就是相對於當前資料夾路徑，其實就是你編寫的這個py檔所放的資料夾路徑
也就是說如果是用相對路徑寫法，檔案必須放在當前文件夾內才可以打開
"""

open('aaa.txt')
open('/data/bbb.txt')

"""
絕對路徑比較好理解，就是最完整的路徑，當你要打開python當下路徑外的其他路徑檔案，就要用絕對路徑
也就是說如果是用絕對路徑寫法就一定要從根目錄開始寫起
"""

# windows如下寫法
open('D:\\user\\ccc.txt')

# linux系統寫法
open('/usr/share/ccc.txt')

# 另外我們也可以透過os這個模組來獲得當前文件夾的絕對路徑，如下：

import os

# 表示當前所處的資料夾的絕對路徑

path1 = os.path.abspath('.')

# 表示當前所處的資料夾上一級資料夾的絕對路徑

path2 = os.path.abspath('..')

"""
./表示目前的目錄下的某個檔或資料夾，視後面跟著的名字而定

../表示目前的目錄上一級目錄的檔或資料夾，視後面跟著的名字而定
"""

# 我們可以利用以下語法來查詢路徑
print(os.path.dirname(os.path.abspath("__file__")))
print(os.path.pardir)
print(os.path.join(os.path.dirname("__file__"), os.path.pardir))
print(os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir)))

# 要例項化路徑，字串作為引數。
# Path物件的字串表示是該字串。
# 要建立引用相對於現有路徑的值的新路徑，請使用/運算子來擴充套件路徑。運算子的引數可以是字串或其他路徑物件。
import pathlib

usr = pathlib.PurePosixPath('/usr')
print(usr)

usr_local = usr / 'local'
print(usr_local)

usr_share = usr / pathlib.PurePosixPath('share')
print(usr_share)

root = usr / '..'
print(root)

etc = root / '/etc/'
print(etc)

# 正如示例輸出中的root值所示，操作符按照給定的方式組合路徑值，並且在包含父目錄引用“..”的情況下不會對結果進行解析。 但是，如果以os.sep開頭它被解釋為新的“根”引用。
# 具體路徑類的resolve()方法，通過檢視目錄和符號連結的檔案系統來解析路徑，並生成名稱引用的絕對路徑。
usr_local = pathlib.Path('/usr/local')
share = usr_local / '..' / 'share'
print(type(share.resolve()))
print(share.resolve())

# joinpath()可以組合路徑
root = pathlib.PurePosixPath('/')
subdirs = ['usr', 'local']
usr_local = root.joinpath(*subdirs)
print(usr_local)

# 使用with_name()建立新路徑，用不同的檔名替換路徑的名稱部分。
# 使用Use with_suffix()建立新路徑，用不同的值替換檔名的副檔名。
ind = pathlib.PurePosixPath('source/pathlib/index.rst')
print(ind)

py = ind.with_name('pathlib_from_existing.py')
print(py)

pyc = py.with_suffix('.pyc')
print(pyc)

# 解析路徑：Path物件具有用於從名稱中提取部分值的方法和屬性。例如，parts屬性會生成一系列基於路徑分隔符值解析的路徑段。
p = pathlib.PurePosixPath('/usr/local')
print(p.parts)

# 有兩種方法可以從給定的路徑物件中"向上"導航檔案系統層次結構。
# 父屬性引用包含路徑的目錄的新路徑例項，即os.path.dirname()返回的值。
# 父項屬性是迭代器，它產生父目錄引用，不斷地向上"提升"路徑層次直到到達根目錄。
p = pathlib.PurePosixPath('/usr/local/lib')

print('parent: {}'.format(p.parent))

print('\nhierarchy:')
for up in p.parents:
    print(up)

# 路徑的其他部分可以通過路徑物件的屬性來訪問。
# name屬性儲存最後一個路徑分隔符（與 os.path.basename()產生的值相同）後的最後一部分路徑。
# 字尾屬性儲存擴充套件分隔符後面的值，並且stem屬性保留後綴之前的名稱部分。
p = pathlib.PurePosixPath('./source/pathlib/pathlib_name.py')
print('path: {}'.format(p))
print('name: {}'.format(p.name))
print('suffix: {}'.format(p.suffix))
print('stem: {}'.format(p.stem))

# 建立Concrete路徑：Concrete Path類的例項可以通過引用檔案系統上的檔案，目錄或符號連結的名稱（或潛在名稱）的字串引數來建立。 該類還提供了幾種便捷方法來構建使用常用位置（如當前工作目錄和使用者主目錄）的例項。
home = pathlib.Path.home()
print('home: ', home)

cwd = pathlib.Path.cwd()
print('cwd : ', cwd)

# 目錄內容：有三種方法可以訪問目錄列表，以發現檔案系統上可用檔案的名稱。
# iterdir()是生成器，為包含目錄中的每個專案生成新的Path例項。
home = pathlib.Path.home()
print('home: ', home)

cwd = pathlib.Path.cwd()
print('cwd : ', cwd)

# 如果路徑不是目錄，則iterdir()會引發NotADirectoryError。
# 則可以使用glob()僅查詢匹配模式的檔案
p = pathlib.Path('.')

for f in p.glob('*.py'):
    print(f)

# 也可以透過rglob()來匹配
for f in p.rglob('*.py'):
    print(f)

# 讀寫檔案：每個Path例項都包含處理它所引用的檔案內容的方法。 要立即檢索內容，請使用read_bytes()或read_text()。
# 要寫入檔案，請使用write_bytes()或write_text()。
# 使用open()方法開啟檔案並保留檔案控制代碼，而不是將名稱傳遞給內建的open()函式。
f = pathlib.Path('example.txt')

f.write_bytes('This is the content'.encode('utf-8'))

with f.open('r', encoding='utf-8') as handle:
    print('read from open(): {!r}'.format(handle.read()))

print('read_text(): {!r}'.format(f.read_text('utf-8')))