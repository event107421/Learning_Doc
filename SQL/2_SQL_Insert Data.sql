-- 先創一個資料表
CREATE TABLE mytable
(
	myid NVARCHAR(10),
	givenName NVARCHAR(50),
	email NVARCHAR(50)
);

--可以用Insert into一筆一筆資料進行匯入
INSERT INTO mytable SELECT '01','Brad','brad@test.com';
INSERT INTO mytable SELECT '02','Siliva','siliva@test.com';
INSERT INTO mytable SELECT '03','Allen','Allen@test.com';

-- 也可以一次Insert多筆資料
INSERT INTO mytable
VALUES ('01','Brad','brad@test.com')
,('02','Siliva','siliva@test.com')
,('03','Allen','Allen@test.com');

-- 但如果資料檔內有大量的資料怎麼辦?此時就可以用BULK INSERT讀檔進行匯入，最簡單的匯入語法如下
BULK INSERT fund_data FROM 'C:\Users\bill\Desktop\USB\自學部分\R\shiny\金融相關\基金介紹資料\2019-10-27_fund_data.txt' WITH(FIRSTROW=1,FIELDTERMINATOR=';')

-- 使用BULK INSERT讀檔進行匯入有些需注意的重點 ============================
/*
ps1.記得資料檔的路徑是根據SQLServer那台路徑為準，你不可能從台灣執行SQL遠端連線到美國的SQLServer去做Bulk Insert，除非你的SQL知道美國那台電腦的資料檔檔案路徑

ps2.還有要記得要在SSMS裡面設定你登入SQLServer的那個帳號的伺服器腳色喔，要把bulkadmin打勾

(安全性=>登入=>右鍵選擇該帳號並選擇屬性=>伺服器腳色=>bulkadmin打勾)

ps3.常見的錯誤訊息：

1.
錯誤訊息顯示：訊息 4861，層級 16，狀態 1，行 1
			  無法大量載入，因為檔案 "C:\目錄\ABC.txt" 無法開啟。作業系統錯誤碼 3(系統找不到指定的路徑。)。

解決方式：因我用SQL驗證方式登入，非同一台電腦，所以遠端a，沒有我"C:\目錄\ABC.txt" 之檔案，所以系統找不到指定的路徑，只要到你遠端a裡面相同路徑下建立就可以執行了。

2.
錯誤訊息顯示：訊息 4864，層級 16，狀態 1，行 3
			  大量載入資料轉換錯誤 (類型不符或指定字碼頁的字元無效) 於資料列 1，資料行 2 (CONTROLLER_ID)。

解決方式：表示你TXT檔內容裡面，資料列 1，資料行 2 ，有值輸入錯誤啦 。
*/

/*
-- 那如果有因為換行符號的關係, 就要用要用動態SQL才可以順利讀入
DECLARE @FileBulk VARCHAR(500)
SELECT @FileBulk='BULK INSERT mytable FROM ''C:\Users\72174\Desktop\1MUCHLMS2.txt'''

SELECT @FileBulk=@FileBulk + ' WITH' 
SELECT @FileBulk=@FileBulk + '(' 
SELECT @FileBulk=@FileBulk + 'FIRSTROW=1,' --從第一行開始讀取
SELECT @FileBulk=@FileBulk + 'FIELDTERMINATOR=''||'','--設定欄位分隔符號
--SELECT @FileBulk=@FileBulk + 'ROWTERMINATOR =''' + CHAR(10) + ''','--換行符號只能用動態SQL方式加入
SELECT @FileBulk=@FileBulk + 'BATCHSIZE=10000, '--每一萬筆就COMMIT一次，以免交易檔爆炸
SELECT @FileBulk=@FileBulk + 'ROWS_PER_BATCH=1000000, '--總共幾萬筆
SELECT @FileBulk=@FileBulk + 'KEEPNULLS, '--原本是NULL的就塞NULL,不要塞入TABLE SCHEMA註明的預設值
SELECT @FileBulk=@FileBulk + 'MAXERRORS=50, '
SELECT @FileBulk=@FileBulk + 'TABLOCK, '
SELECT @FileBulk=@FileBulk + 'DATAFILETYPE =''widechar'''--當檔案為unicode時要加上這個指令，不然會出現錯誤
SELECT @FileBulk=@FileBulk + ')'
 
PRINT @FileBulk
EXEC (@FileBulk)
*/

-- 最後來講解一下BULK INSERT的參數
/*
BULK INSERT [ [ 'database_name'.][ 'owner' ].]{ 'table_name'FROM'data_file' }      
WITH  (  
        [ BATCHSIZE [ = batch_size ] ],      
        [ CHECK_CONSTRAINTS ],          
        [ CODEPAGE [ = 'ACP' | 'OEM' | 'RAW' | 'code_page' ] ],  
        [ DATAFILETYPE [ = 'char' | 'native'| 'widechar' | 'widenative' ] ],              
        [ FIELDTERMINATOR [ = 'field_terminator' ] ],  
        [ FIRSTROW [ = first_row ] ],  
        [ FIRE_TRIGGERS ],  
        [ FORMATFILE = 'format_file_path' ],  
        [ KEEPIDENTITY ],  
        [ KEEPNULLS ],  
        [ KILOBYTES_PER_BATCH [ = kilobytes_per_batch ] ],     
        [ LASTROW [ = last_row ] ],  
        [ MAXERRORS [ = max_errors ] ],  
        [ ORDER ( { column [ ASC | DESC ] } [ ,...n ] ) ],    
        [ ROWS_PER_BATCH [ = rows_per_batch ] ],  
        [ ROWTERMINATOR [ = 'row_terminator' ] ],            
        [ TABLOCK ],  
);

引數: 
1. 'database_name'：是包含指定表或檢視的資料庫的名稱。如果未指定，則系統預設為當前資料庫。 

2. 'owner'：是表或檢視所有者的名稱。當執行大容量複製操作的使用者擁有指定的表或檢視時，owner 是可選項。
			如果沒有指定 owner 並且執行大容量複製操作的使用者不擁有指定的表或檢視，則 MicrosoftR SQL Server? 將返回錯誤資訊並取消大容量複製操作。 

3. 'table_name'：是大容量複製資料於其中的表或檢視的名稱。只能使用那些所有的列引用相同基表所在的檢視。有關向檢視中複製資料的限制的更多資訊，請參見 INSERT。 

4. 'data_file'：是資料檔案的完整路徑，該資料檔案包含要複製到指定表或檢視的資料。BULK INSERT 從磁碟複製資料（包括網路、軟盤、硬碟等）。 
				data_file 必須從執行 SQL Server 的伺服器指定有效路徑。如果 data_file 是遠端檔案，則請指定通用命名規則 (UNC) 名稱。 

5. BATCHSIZE [ = batch_size ]：指定批處理中的行數。每個批處理作為一個事務複製至伺服器。SQL Server提交或回滾（在失敗時）每個批處理的事務。預設情況下，指定資料檔案中的所有資料是一個批處理。 

6. CHECK_CONSTRAINTS：指定在大容量複製操作中檢查 table_name 的任何約束。預設情況下，將會忽略約束。 

7. CODEPAGE [ = 'ACP' | 'OEM' | 'RAW' | 'code_page' ]：指定該資料檔案中資料的內碼表。僅當資料含有字元值大於 127 或小於 32 的 char、varchar 或 text 列時，CODEPAGE 才是適用的。
													   CODEPAGE 值 描述 ACP char、varchar 或 text 資料型別的列從 ANSI/Microsoft WindowsR 內碼表 ISO 1252 轉換為 SQL Server 內碼表。
													   OEM（預設值） char、varchar 或 text 資料型別的列被從系統 OEM 內碼表轉換為 SQL Server 內碼表。 RAW 並不進行從一個內碼表到另一個內碼表的轉換；這是最快的選項。
													   code_page 特定的內碼表號碼，例如 850。 

8. DATAFILETYPE [ = {'char' | 'native' | 'widechar' | 'widenative' } ]：指定 BULK INSERT 使用指定的預設值執行復制操作。DATAFILETYPE 值 描述 char（預設值） 從含有字元資料的資料檔案執行大容量複製操作。
																		native 使用 native（資料庫）資料型別執行大容量複製操作。要裝載的資料檔案由大容量複製資料建立，該複製是用 bcp 實用工具從 SQL Server 進行的。
																		widechar 從含有 Unicode 字元的資料檔案中執行大容量複製操作。 widenative 執行與 native 相同的大容量複製操作，不同之處是 char、varchar 和 text 列在資料檔案中儲存為 Unicode。
																		要裝載的資料檔案由大容量複製資料建立，該複製是用 bcp 實用工具從 SQL Server 進行的。該選項是對 widechar 選項的一個更高效能的替代，並且它用於使用資料檔案從一個執行 SQL Server 的計算機向另一個計算機傳送資料。
																		當傳送含有 ANSI 擴充套件字元的資料時，使用該選項以便利用 native 模式的效能。 

9. FIELDTERMINATOR [ = 'field_terminator' ]：指定用於 char 和 widechar 資料檔案的欄位終止符。預設的欄位終止符是 /t（製表符）。 

10. FIRSTROW [ = first_row ]：指定要複製的第一行的行號。預設值是 1，表示在指定資料檔案的第一行。 

11. FIRE_TRIGGERS：指定目的表中定義的任何插入觸發器將在大容量複製操作過程中執行。如果沒有指定 FIRE_TRIGGERS，將不執行任何插入觸發器。 

12. FORMATFILE [ = 'format_file_path' ]：指定一個格式檔案的完整路徑。格式檔案描述了含有儲存響應的資料檔案，這些儲存響應是使用 bcp 實用工具在相同的表或檢視中建立的。
										 格式檔案應該用於以下情況： 資料檔案含有比表或檢視更多或更少的列。列使用不同的順序。列分割符發生變化。資料格式有其它的改變。
										 通常，格式檔案通過 bcp 實用工具建立並且根據需要用文字編輯器修改。有關更多資訊，請參見 bcp 實用工具。 

13. KEEPIDENTITY：指定標識列的值存在於匯入檔案中。如果沒有指定 KEEPIDENTITY，在匯入的資料檔案中此列的標識值將被忽略，並且 SQL Server 將根據表建立時指定的種子值和增量值自動賦給一個唯一的值。
				  假如資料檔案不含該表或檢視中的標識列，使用一個格式檔案來指定在匯入資料時，表或檢視中的標識列應被忽略；SQL Server 自動為此列賦予唯一的值。有關詳細資訊，請參見 DBCC CHECKIDENT。 

14. KEEPNULLS：指定在大容量複製操作中空列應保留一個空值，而不是對插入的列賦予預設值。 

15. KILOBYTES_PER_BATCH [ = kilobytes_per_batch ]：指定每個批處理中資料的近似千位元組數（KB）。預設情況下，KILOBYTES_PER_BATCH 未知。 

16. LASTROW [ = last_row ]：指定要複製的最後一行的行號。預設值是 0，表示指定資料檔案中的最後一行。 

17. MAXERRORS [ = max_errors ]：指定在大容量複製操作取消之前可能產生的錯誤的最大數目。不能被大容量複製操作匯入的每一行將被忽略並且被計為一次錯誤。如果沒有指定 max_errors，預設值為 0。 

18. ORDER ( { column [ ASC | DESC ] } [ ,...n ] )：指定資料檔案中的資料如何排序。如果裝載的資料根據表中的聚集索引進行排序，則可以提高大容量複製操作的效能。
												   如果資料檔案基於不同的順序排序，或表中沒有聚集索引，ORDER 子句將被忽略。給出的列名必須是目的表中有效的列。預設情況下，大容量插入操作假設資料檔案未排序。
												   n是表示可以指定多列的佔位符。 

19. ROWS_PER_BATCH [ = rows_per_batch ]：指定每一批處理資料的行數（即 rows_per_bacth）。當沒有指定 BATCHSIZE 時使用，導致整個資料檔案作為單個事務傳送給伺服器。
										 伺服器根據 rows_per_batch 優化大容量裝載。預設情況下，ROWS_PER_BATCH 未知。 

20. ROWTERMINATOR [ = 'row_terminator' ]：指定對於 char 和 widechar 資料檔案要使用的行終止符。預設值是 /n（換行符）。 

21. TABLOCK：指定對於大容量複製操作期間獲取一個表級鎖。如果表沒有索引並且指定了 TABLOCK，則該表可以同時由多個客戶端裝載。預設情況下，鎖定行為是由表選項 table lock on bulk load 決定的。
			 只在大容量複製操作期間控制鎖會減少表上的鎖爭奪，極大地提高效能。註釋BULK INSERT 語句能在使用者定義事務中執行。
			 對於一個用 BULK INSERT 語句和 BATCHSIZE 子句將資料裝載到使用多個批處理的表或檢視中的使用者定義事務來說，回滾它將回滾所有傳送給 SQL Server 的批處理。
			 許可權只有 sysadmin 和 bulkadmin 固定伺服器角色成員才能執行 BULK INSERT。
*/

-- 將查詢後的結果匯入另一個已經創建的資料表
INSERT mytable_1 SELECT myid, email FROM mytable

-- 也可以將查詢後的結果直接存成另一個資料表
SELECT myid, email INTO mytable_2 FROM mytable

--刪除整張資料表
DROP TABLE mytable_1 

--刪除指定條件的資料
DELETE FROM mytable_2 WHERE myid = '03'



