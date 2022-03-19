# 在python中，常常看到很多函式(function)中出現以下的語句：if __name__ == '__main__':
# 先創一個放以下程式碼的if_name_main_example.py檔，作為範例檔 =====================================
print('我愛Python')
def love():
    print('我愛Python')

if __name__=="__main__":
    print('天天寫扣的，越來越愛python')
    love()

# 接下來我們將上面的py檔import進來執行，可以發現執行結果只有'我愛Python'，代表只有print第一行的結果，其他的結果都沒有出現
import if_name_main_example

# 原因在於：
# 當 Python 檔案（模組、module）被引用的時候，檔案內的每一行都會被 Python 直譯器讀取並執行（所以 cool.py內的程式碼會被執行）
# Python 直譯器執行程式碼時，有一些內建、隱含的變數，__name__就是其中之一，其意義是「模組名稱」。
# 若該檔案是(透過命令列)直接執行print(__name__)，其值會是 __main__，如下：
print(__name__)

# 那如果我們將print(__name__)加進import進來的程式碼內，如下 =======================================
# 要加在if __name__ == '__main__':這段程式碼的上面
def love():
    print('我愛Python')

print(__name__)
if __name__ == '__main__':
    love()
    print('天天寫扣的，越來越愛python')

# 加進程式碼後，我們可以再import一次結果變成import if_name_main_example ===========================
# 可以發現執行結果不同了，因為如果該檔案是被引用，其值就會變模組名稱
import if_name_main_example

### 結論 ========================================
# 簡而言之就是：__name__ 是當前檔案名，當檔案被直接運行時檔案名為__main__，所以if __name__ == '__main__'條件為真，就會執行下面的程式碼。
# 但當檔案是被導入進來時，程式即不被運行，因為__name__就會變成模組名稱，不為__main__，即只會執行if __name__ == '__main__'前面的程式碼。