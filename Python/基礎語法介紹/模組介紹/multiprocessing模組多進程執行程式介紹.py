import multiprocessing as mp
import os, time

# 因模組預設啟動方式是'spawn'，所以當我們直接執行mp.pool的時候會報錯
# 而mac默認的fork方式啟動進程， 所以我們需先把'spawn'改成'fork'即可通過
mp.set_start_method('fork')

"""
關於父進程和子進程的啟動方式有三種：

spawn：由父進程啟動一個Python解釋器進程，子進程只會繼承運行對象的run()方法這些資源可以由父進程分配。父進程中的非必須的文件描述符和句柄不會被繼承，這種啟動方式最慢;

fork：父進程使用os.fork()來產生的解釋器分叉，這種狀態下父進程和子進程是相同的，父進程的所有資源都有子進程繼承，安全分叉多線程進程管理起來會很困難;

forkserver: 程序啟動並選擇* forkserver * 啟動方法時，將啟動服務器進程。從那時起，每當需要一個新進程時，父進程就會連接到服務器並請求它分叉一個新進程。分叉服務器進程是單線程的，因此使用os.fork()是安全的。沒有不必要的資源被繼承。
"""

def main_map(i):
    result = i * i
    return result


if __name__ == '__main__':
    inputs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

      # 設定處理程序數量
    pool = mp.Pool(processes=4)

      # 運行多處理程序
    pool_outputs = pool.map(main_map, inputs)

      # 輸出執行結果
    print(pool_outputs)