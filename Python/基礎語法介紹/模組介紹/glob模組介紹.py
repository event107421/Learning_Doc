"""
這邊介紹下glob這個好用的套件，使用UNIX shell規則查找與一個模式匹配的文件名
基本用法：
1.glob.glob（pathname)：返回所有匹配的文件路徑列表。它只有一個參數pathname，定義了文件路徑匹配規則，這裏可以是絕對路徑，也可以是相對路徑。

2.glob.iglob(pathname)：獲取一個可編歷對象，使用它可以逐個獲取匹配的文件路徑名。與glob.glob()的區別是，glob.glob同時獲取所有的匹配路徑，而glob.iglob一次只獲取一個匹配路徑。
"""

import glob
print(glob.glob(r'E:\*\*.doc'))
print(glob.glob(r'.\*.py'))

f = glob.iglob(r'.\*.py')
for py in f:
  print(py)

"""
通配符：
萬用字元-星號*：星號*匹配一個檔案名段中的0個或多個字元
"""

import glob

for name in glob.glob('tmp/*'):
  print(name)

# 如果要列出子目錄中的文件，必須把子目錄包含在模式中
import glob

for name in glob.glob('tmp/one/*'):
    print('\t', name)

for name in glob.glob('tmp/*/*'):
    print('\t', name)

# 單配符-問號?：問號?會匹配檔案名中該位置的單個字元。
import glob
for name in glob.glob('tmp/chec?_traffic.sh'):
    print(name)

"""
字元區間-[a-z]：使用字元區間[a-z]，可以匹配多個字元中的一個字元。\
區間可以匹配所有小寫字母
"""

import glob
for name in glob.glob('tmp/one/[a-z]*'):
    print(name)

# 用glob套件可以返回所有匹配的文件路徑列表
# 基本用法:
# glob.glob同時獲取所有的匹配路徑，而glob.iglob一次只獲取一個匹配路徑。
import glob

path = r'F:\展示的平台\金融相關\基金歷史資料'  # 資料夾名稱
# 通配符，星號匹配一個文件名段中的0個或多個字符。
print(glob.glob(path + "/*.csv"))
f = glob.iglob(path + "/*.csv")
for py in f:
    print(py)

# 可以用*通配符查找資料夾下的子目錄名reduce(lambda x, y: x+y, [1,2,3,4,5])
path = r'F:\展示的平台'  # 資料夾名稱
for name in glob.glob(path + '/*/*'):
    print('\t', name)

# 字符區間，可以匹配檔案開頭多個字符中的一個字符
for name in glob.glob(path + '/[a-z]*'):
    print(name)