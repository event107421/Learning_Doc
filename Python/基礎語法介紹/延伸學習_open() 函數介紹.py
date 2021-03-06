# python open() 函數用於打開一個文件，創建一個 file 對象，相關的方法才可以調用它進行讀寫
# 函數語法：
open(name[, mode[, buffering]])

"""
參數說明：
name : 一個包含了你要訪問的文件名稱的字符串值。
mode : mode 決定了打開文件的模式：只讀，寫入，追加等。所有可取值見如下的完全列表。這個參數是非強制的，默認文件訪問模式為只讀(r)。
buffering : 如果 buffering 的值被設為 0，就不會有寄存。如果 buffering 的值取 1，訪問文件時會寄存行。如果將 buffering 的值設為大於 1 的整數，表明了這就是的寄存區的緩衝大小。如果取負值，寄存區的緩衝大小則為系統默認。

不同模式打開文件的列表：
t：文本模式 (默認)。
x：寫模式，新建一個文件，如果該文件已存在則會報錯。
b：二進制模式。
+：打開一個文件進行更新(可讀可寫)。
U：通用換行模式（不推薦）。
r：以只讀方式打開文件。文件的指針將會放在文件的開頭。這是默認模式。
rb：以二進制格式打開一個文件用於只讀。文件指針將會放在文件的開頭。這是默認模式。一般用於非文本文件如圖片等。
r+：打開一個文件用於讀寫。文件指針將會放在文件的開頭。
rb+：以二進制格式打開一個文件用於讀寫。文件指針將會放在文件的開頭。一般用於非文本文件如圖片等。
w：打開一個文件只用於寫入。如果該文件已存在則打開文件，並從開頭開始編輯，即原有內容會被刪除。如果該文件不存在，創建新文件。
wb：以二進制格式打開一個文件只用於寫入。如果該文件已存在則打開文件，並從開頭開始編輯，即原有內容會被刪除。如果該文件不存在，創建新文件。一般用於非文本文件如圖片等。
w+：打開一個文件用於讀寫。如果該文件已存在則打開文件，並從開頭開始編輯，即原有內容會被刪除。如果該文件不存在，創建新文件。
wb+：以二進制格式打開一個文件用於讀寫。如果該文件已存在則打開文件，並從開頭開始編輯，即原有內容會被刪除。如果該文件不存在，創建新文件。一般用於非文本文件如圖片等。
a：打開一個文件用於追加。如果該文件已存在，文件指針將會放在文件的結尾。也就是說，新的內容將會被寫入到已有內容之後。如果該文件不存在，創建新文件進行寫入。
ab：以二進制格式打開一個文件用於追加。如果該文件已存在，文件指針將會放在文件的結尾。也就是說，新的內容將會被寫入到已有內容之後。如果該文件不存在，創建新文件進行寫入。
a+：打開一個文件用於讀寫。如果該文件已存在，文件指針將會放在文件的結尾。文件打開時會是追加模式。如果該文件不存在，創建新文件用於讀寫。
ab+：以二進制格式打開一個文件用於追加。如果該文件已存在，文件指針將會放在文件的結尾。如果該文件不存在，創建新文件用於讀寫。