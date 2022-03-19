"""
用Pandas把DataFrame數據寫入Excel文件，一般使用to_excel方法
"""
import pandas as pd
grades.head()

outputFile = "grades.xlsx"
grades.to_excel(outputFile)

# 如果你有多張表要寫入，一般方法永遠是後一張表覆蓋掉前一張表。即使每次修改sheet_name也不行，如下程式碼：
df1.to_excel(target_file, sheet_name='sheet1')
df2.to_excel(target_file, sheet_name='sheet2')
df3.to_excel(target_file, sheet_name='sheet3')

# 此時可以用全新文件的寫入方法，假如你有多張表要寫入到一個全新的文件中，方法非常簡單，使用一個叫ExcelWriter函數即可
# 建立一個test_new.xlsx空檔案，分別將df1、df2寫入不同sheet
writer = pd.ExcelWriter('test_new.xlsx')
df1.to_excel(writer, sheet_name='sheet1')
df2.to_excel(writer, sheet_name='sheet2')
writer.save()

"""
pandas模組內ExcelWriter函數介紹：

class pandas.ExcelWriter(path, engine=None, date_format=None, datetime_format=None, mode='w', **engine_kwargs)

參數：
path：str，xls或xlsx文件的路徑。

engine：str(可選參數)，用於編寫的引擎。如果為無，則默認為io.excel.<extension>.writer。注意：只能作為關鍵字參數傳遞。

date_format：str，默認為 None，格式字符串，用於寫入Excel文件的日期(例如“ YYYY-MM-DD”)。

datetime_format：str，默認為 None，寫入Excel文件的日期時間對象的格式字符串。 (例如“ YYYY-MM-DD HH：MM：SS”)。

mode：{'w', 'a'}, 默認為 'w'，要使用的文件模式(寫或追加)。
"""

# ExcelWriter這個插件有個坑，就是已經設置好的格式是無法更改的
# 因此，由pandas轉成excel的時候，必須將格式清除，尤其是表頭的格式，代碼如下：
import pandas.io.formats.excel
pandas.io.formats.excel.header_style = None

# 標準的保存pandas表到excel的形式為：
writer = pd.ExcelWriter(output_prefix + cv_excel_file_name)
# 這裡假設df是一個pandas的dataframe
df.to_excel(writer, 'Sheet1')
# 存檔
writer.save()
# 關閉檔案
writer.close()

# 如果要定制輸出的excel格式，那麼得在to_excel和save之間添加代碼：

writer = pd.ExcelWriter(output_prefix + cv_excel_file_name)
df.to_excel(writer, 'Sheet1')  # 这里假设df是一个pandas的dataframe

# =================== add self define code here =======================
# from xlsxwriter.workbook import Workbook
# from xlsxwriter.worksheet import Worksheet
workbook1 = writer.book
worksheets = writer.sheets
worksheet1 = worksheets['Sheet1']

writer.save()
writer.close()

# 我們在操作worksheet(各個工作表)中的各自前，需要往workbook(工作簿，也就是excel檔案)當中添加自定義格式集合
# 可以新增的格式如下程式碼：
bold = f.add_format({
        'bold': True, # 字體加粗
        'border': 1, # 單元格邊框寬度
        'align': 'left', # 水平對齊方式
        'valign': 'vcenter', # 垂直對齊方式
        'fg_color': '#F4B084', # 單元格背景顏色
        'text_wrap': True, # 是否自動換行
    })

format1 = workbook1.add_format({'bg_color': '#FFC7CE', 'font_color': '#9C0006'})
format2 = workbook1.add_format({'bold':  True, 'align': 'left', 'valign': 'top', 'text_wrap': True})

# 設置行格式(更改表頭格式)
worksheet1.set_row(0, cell_format=format2)

# 設置列寬(B列到AE列所有的列寬都為16)
worksheet1.set_column("B:AE", 16)

# 設置條件格式(令A列2到55行選出數值最大的一個'top1'，並用format1的格式和顏色進行渲染)
worksheet1.conditional_format('A2:A55', {'type': 'top', 'value': 1, 'format': format1})

# 上述使用ExcelWriter函數，因為在python中開啟檔案後，或是開啟連接後，都須在下一個close的指令將其關閉，如下程式碼：
file = open("１.txt")
data = file.read()
file.close()

"""
# 上面代碼存在２個問題：
# 1. 文件讀取發生異常，但沒有進行任何處理
# 2. 可能忘記關閉文件

此時，我們就可以使用python內的 with...as...函數進行程式碼改寫
"""

# with 語句適用於對資源進行訪問的場合，確保不管使用過程中是否發生異常都會執行必要的“清理”操作，釋放資源，比如文件使用後自動關閉／線程中鎖的自動獲取和釋放等
with pd.ExcelWriter(outputFile) as ew:
    grades.to_excel(ew)

# 在單個文件中寫入單獨的Sheet
with ExcelWriter('path_to_file.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Sheet1')
    df2.to_excel(writer, sheet_name='Sheet2')

# 也可以設置日期格式或日期時間格式
with ExcelWriter('path_to_file.xlsx',
                 date_format='YYYY-MM-DD',
                 datetime_format='YYYY-MM-DD HH:MM:SS') as writer:
    df.to_excel(writer)

# 還可以附加到現有的Excel文件
with ExcelWriter('path_to_file.xlsx', mode='a') as writer:
    df.to_excel(writer, sheet_name='Sheet3')

