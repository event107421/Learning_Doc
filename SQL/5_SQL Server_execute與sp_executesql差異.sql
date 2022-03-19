/*
Microsoft SQL Server 提供兩種方式可以讓你執行動態建立的查詢字串：
一是 EXECUTE 命令 (通常用簡寫 EXEC)，另一是 sp_executesql。
大致上來說，EXEC 限制較少，使用簡單，只要組成字串且是合法的查詢指令即可執行(強調一下，合法指的是可以成功剖析、編譯，不代表沒有惡意)
而 sp_executesql 則可以傳參數，結構較嚴謹，因此得以撰寫更安全的動態查詢，提高執行計劃重用的機會，相對來說執行效率會更好，當然也是官方較建議的方式。

除此之外，兩者有一些重要的特性(https://dotblogs.com.tw/hunterpo/2010/02/05/13488)：
1. 權限：使用動態查詢時，所有參考到的安全性實體 (Securables)，執行的使用者必須具有直接存取權。例如，包含 INSERT 指令時，使用者就必須有該資料表的 INSERT 權限，即使此一動態查詢包含於預存程序當中也一樣
		 一旦發現 EXEC、sp_executesql 陳述式就會檢查權限。

2. 自成批次：動態查詢的執行是與進行呼叫的批次分開的，換句話說另成一個獨立單元進行剖析、最佳化、編譯執行計劃，而且是等到執行 EXEC 或 sp_executesql 陳述式時才會編譯。
			 可想而知，這一份計劃不同於含有 EXEC 或 sp_executesql 陳述式的批次所產生的。

3. 區域變數可及性：承上所述，包含 EXEC 或 sp_executesql 陳述式的批次指令是為外部批次，動態查詢則為內部批次，所有區域變數只有在被宣告的批次裡可以取用，內外層級皆然。

4. 區域暫存資料表可及性 - 外部批次所建立的區域暫存表可以被內部的動態查詢所存取，但內部批次所建立的區域暫存表只要超出批次作用範圍將自動銷毀。
*/

/*
-- EXEC 基本語法
EXEC使用時機有兩個，一是用來執行預存程序，另一則是本篇所關注的焦點 - 執行動態查詢字串。
簡化的語法表示會像 EXEC('tsql_string')，括號內只能是字串，包含純字元字串，或字串變數串接皆可，但不能有函數或任何命令，若有這樣的需求可以先拉到外部批次處理
*/
-- 例如：
-- 建構陳述式：SELECT COUNT(*) AS rows FROM [dbo].[Categories]
SET @cmd = @cmd + QUOTENAME(@schema) + '.' + QUOTENAME(@table) + ';';
EXEC (@cmd);

-- 底下為錯誤用法，要先把執行的語法設成一個變數來執行
EXEC (@cmd + QUOTENAME(@schema) + '.' + QUOTENAME(@table) + ';');

-- EXEC 與區域變數 ===================================================
/*
區域變數的範圍是宣告它的批次。(原文：The scope of a local variable is the batch in which it is declared.)
所以若是執行底下的指令：
*/
DECLARE @ProductID int
SET @ProductID = 1;

DECLARE @cmd VarChar(60);
SET @cmd = 'SELECT * FROM dbo.Products WHERE (ProductID = @ProductID);';
EXEC(@cmd);

/*
此時會收到必須宣告變數的錯誤訊息：
Msg 137, Level 15, State 2, Line 1
Must declare the scalar variable "@ProductID".
*/

-- 使用 EXEC 時，若想取用變數，就只能把變數串接到動態查詢裡，因此改用底下的方式就能順利執行：
DECLARE @ProductID int
SET @ProductID = 1;

DECLARE @cmd VarChar(60);
SET @cmd = 'SELECT * FROM dbo.Products WHERE (ProductID = ' + CAST(@ProductID AS VarChar(5)) + ');';
EXEC(@cmd);

/*
不過這樣做很危險！特別是變數為字元型別時 (含 char、nchar、varchar、nvarchar、text、ntext)
極可能招致資料隱碼 (SQL Injection) 攻擊，此為 EXEC 執行動態查詢的其中一個缺點，另一個缺點是效能問題
再度清除計劃快取，然後把上面的動態查詢多執行幾次，每次都給不同的 @ProductID，如下：
*/

DBCC FREEPROCCACHE;
GO

-- 2. 查詢產品資料 3 次
DECLARE @ProductID int
DECLARE @cmd VarChar(60)

SET @ProductID = 1;
SET @cmd = 'SELECT * FROM dbo.Products WHERE (ProductID = ' + CAST(@ProductID AS VarChar(5)) + ');';
EXEC(@cmd);

SET @ProductID = 2;
SET @cmd = 'SELECT * FROM dbo.Products WHERE (ProductID = ' + CAST(@ProductID AS VarChar(5)) + ');';
EXEC(@cmd);

SET @ProductID = 3;
SET @cmd = 'SELECT * FROM dbo.Products WHERE (ProductID = ' + CAST(@ProductID AS VarChar(5)) + ');';
EXEC(@cmd);
GO

-- 3. 查看快取
SELECT cacheobjtype, objtype, usecounts, [sql] 
FROM sys.syscacheobjects
WHERE (objtype = 'Proc') OR (objtype = 'Adhoc')
GO

/*
此時可以看到，不同的 @ProductID 會各自產生一份查詢計劃
編譯執行計劃會耗用 CPU 資源，如果這是在線環境裡非常頻繁使用的查詢，可就不妙了
*/

/*
除非有個好理由，否則應該少用 EXEC 方式執行動態查詢，例如在 SQL Server 2000 的版本中，字元字串限制在 4000 個字元
唯一突破限制的方式是宣告多個字元變數 @cmd1、@cmd2，再丟到 EXEC(@cmd1 + @cmd2) 執行
還好 SQL Server 2005 以後出現了 NVarChar(MAX) 型別，此限制已不存在，因此實務上所有的動態查詢都應該交由 sp_executesql 來執行
想像 sp_executesql 是一個空殼預存程序，查詢批次內容隨你指定，需要參數時也不用客氣，儘管在查詢字串以 @param 的格式指定
記得在內嵌參數定義字串裡一一宣告，最後再逐一給參數值即可，所有輸入字串部分都只接受 Unicode 型別
*/

-- 前面看過 EXEC 執行串接參數的動態查詢時，只要參數值改變就會產生新的查詢計劃，現在修改內容用 sp_executesql 執行看看：
DBCC FREEPROCCACHE;
GO

-- 2. 查詢產品資料 3 次
DECLARE @stmt NVarChar(60),
		@paramsDefinition NVarChar(20),
		@ProductID int

SET @stmt = N'SELECT * FROM dbo.Products WHERE (ProductID = @ProductID);'; 
SET @paramsDefinition = N'@ProductID int';

SET @ProductID = 1;
EXEC dbo.sp_executesql
		@stmt,
		@paramsDefinition,
		@ProductID;

SET @ProductID = 2;
EXEC dbo.sp_executesql
		@stmt,
		@paramsDefinition,
		@ProductID;

SET @ProductID = 3;
EXEC dbo.sp_executesql
		@stmt,
		@paramsDefinition,
		@ProductID;
GO

-- 3. 查看快取
SELECT cacheobjtype, objtype, usecounts, [sql] 
FROM sys.syscacheobjects
WHERE (objtype IN ('Proc', 'Prepared'))
GO

/*
從快取資訊中我們可以發現，同一份執行計劃重複利用了 3 次
*/

-- 除此之外，sp_executesql 支援輸出參數的能力，簡化了回傳值的方式。使用 EXEC 時，看看要回傳值需怎麼做：
SET @sql = N'INSERT INTO #T SELECT COUNT(*) FROM [dbo].[Products];'; 

-- 建立區域暫存表
CREATE TABLE #T(cnt int);

-- 利用外部批次建立的暫存表，內部可見的特性，將值寫入
EXEC(@sql);
SELECT cnt AS [total_products] FROM #T;

DROP TABLE #T;
GO

-- 反觀利用 sp_executesql 回傳值則好多了：
DECLARE @paramsDef NVarChar(20),
		@paramsDefinition NVarChar(20),
		@cnt int

SET @sql = N'SELECT @Cnt = COUNT(*) FROM [dbo].[Products];'; 
SET @paramsDef = N'@Cnt int OUTPUT'; -- 內嵌參數宣告為輸出參數

EXEC dbo.sp_executesql
		@Stmt = @sql,
		@Params = @paramsDef,
		@Cnt = @cnt OUTPUT;
SELECT @cnt AS [total_products];

/*
動態 SQL 無疑是開放使用者參與建構查詢指令，其實都是為了彈性，但也代表相當程度的資料隱碼攻擊風險，因此針對外來的輸入加以驗證是絕對必要的手段
官方對於 EXEC 、sp_executesql 的說明文件，幾乎一開頭就特別強調這一點
*/