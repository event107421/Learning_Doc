-- SQL自定義函數（CREATE FUNCTION） ====================================
-- 建立並使用自定義函數
可以使用 CREATE FUNCTION 語句建立自定義函數。

-- 語法格式如下：
CREATE FUNCTION <函數名> ( [ <引數1> <型別1> [ , <引數2> <型別2>] ] … )
  RETURNS <型別>
  <函數主體>
/*
語法說明如下：
<函數名>：指定自定義函數的名稱。注意，自定義函數不能與儲存過程具有相同的名稱。
<引數><型別>：用於指定自定義函數的引數。這裡的引數只有名稱和型別，不能指定關鍵字 IN、OUT 和 INOUT。
RETURNS<型別>：用於宣告自定義函數返回值的資料型別。其中，<型別>用於指定返回值的資料型別。
<函數主體>：自定義函數的主體部分，也稱函數體。所有在儲存過程中使用的 SQL 語句在自定義函數中同樣適用，包括前面所介紹的區域性變數、SET 語句、流程控制語句、游標等。除此之外，自定義函數體還必須包含一個 RETURN<VALUE> 語句，其中<VALUE>用於指定自定義函數的返回值。
在 RETURN VALUE 語句中包含 SELECT 語句時，SELECT 語句的返回結果只能是一行且只能有一列值
*/

-- 若要檢視資料庫中存在哪些自定義函數：
SHOW FUNCTION STATUS
-- 若要檢視資料庫中某個具體的自定義函數：其中<函數名>用於指定該自定義函數的名稱
SHOW CREATE FUNCTION <自定義函數名>

-- 修改自定義函數：利用語句來修改自定義函數的某些相關特徵，若要修改自定義函數的內容，則需要先刪除該自定義函數，然後重新建立。
ALTER FUNCTION <自定義函數名> [SQL敘述句]

-- 刪除自定義函數：自定義函數被建立後，一直儲存在資料庫伺服器上以供使用，直至被刪除。刪除自定義函數的方法與刪除儲存過程的方法基本一樣，可以使用 DROP FUNCTION 語句來實現，語法格式如下：
DROP FUNCTION [ IF EXISTS ] <自定義函數名>
/*
語法說明如下：
<自定義函數名>：指定要刪除的自定義函數的名稱。
IF EXISTS：指定關鍵字，用於防止因誤刪除不存在的自定義函數而引發錯誤。
*/

-- 使用流程控制：BEGIN...END 與 RETURN ================================
/*
可以讓多個陳述式變成一個邏輯的區塊，就可以使用 BEGIN...END 來讓 SQL 把它們視為單一的區塊來處理
因為一般在設定函數、IF、while迴圈等，後面只能緊接一句陳述句，所以如果有多句陳述句要一起執行就應該使用BEGIN 和 END 包起來，雖然是一個微不足道小細節，但開發撰寫時還是需要注意
至於 RETURN 則能夠立即無條件地終止一個查詢、預存程序或是批次，也就是說，位於 RETURN 之後的程式碼都不會被執行
*/

-- 利用BEGIN...END建立一個計算年齡函數 ==================================
-- 建立自訂函數
CREATE FUNCTION dbo.fn_GetAge(
@myDate datetime)
RETURNS int
AS
BEGIN

-- 宣告變數
DECLARE @age int, @day datetime

-- 以「年」為單位計算出年齡
SET @age = DATEDIFF(yy, @myDate, getdate()) -
    CASE WHEN @day < DATEADD(yy, DATEDIFF(yy, @myDate, @day), @myDate)
      THEN 1
      ELSE 0
    END
RETURN @age

END
GO

-- 呼叫自訂的函數
SELECT dbo.fn_GetAge('19990818') as age


--取每月最後一天工作日 ==========================
DECLARE @year INT, @month INT
SET @year = 2019
SET @month = 03

--計算當月份最後一天工作日，但這邊如果用在當月份有補班補課就要注意，因為補班補課系統不會知道
DECLARE @lastWorkDay DATETIME
SELECT @lastWorkDay = DATEADD(year, @year-1900, DATEADD(month, @month, '1900-1-1'))-1
SELECT @lastWorkDay = CASE DATEPART(weekday, @lastWorkDay)
WHEN 1 THEN DATEADD(day, -2, @lastWorkDay)
WHEN 7 THEN DATEADD(day, -1, @lastWorkDay)
ELSE @lastWorkDay END
SELECT 結果 = @lastWorkDay

--將上方寫成自定義函數 ===========================
CREATE FUNCTION f_lastWorkDay(
	@year INT,
	@month INT
)RETURNS DATETIME
AS
-- 不管哪一種程式語言都具備流程控制的功能，用來控制程式執行與流程的流向，透過流程控制可以讓程式更容易維護。
-- 要讓多個 T-SQL 陳述式變成一個邏輯的區塊，就可以使用 BEGIN...END 來讓 SQL Server 把它們視為單一的區塊來處理。
BEGIN
DECLARE @lastWorkDay DATETIME
SELECT @lastWorkDay = DATEADD(year,@year-1900,DATEADD(month, @month, '1900-1-1'))-1
-- 至於 RETURN 則能夠立即無條件地終止一個查詢、預存程序或是批次，也就是說，位於 RETURN 之後的程式碼都不會被執行。
RETURN(
	CASE DATEPART(weekday, @lastWorkDay)
	WHEN 1 THEN DATEADD(day, -2, @lastWorkDay)
	WHEN 7 THEN DATEADD(day, -1, @lastWorkDay)
	ELSE @lastWorkDay END
)
END
GO

--調用函數
SELECT dbo.f_lastWorkDay(2001, 11)

--DROP FUNCTION f_lastWorkDay


--每月第一個工作日 ===============================
--寫成自定義函數
CREATE FUNCTION f_lastWorkDay(
	@year INT,
	@month INT
)RETURNS DATETIME
AS
BEGIN
DECLARE @lastWorkDay DATETIME
SELECT @lastWorkDay = DATEADD(YEAR, @year-1900, DATEADD(MONTH, @month-1, '1900-1-1'))
RETURN(
	CASE DATEPART(weekday, @lastWorkDay)
	WHEN 1 THEN DATEADD(DAY, 1, @lastWorkDay)
	WHEN 7 THEN DATEADD(DAY, 2, @lastWorkDay)
	ELSE @lastWorkDay END
)
END
GO

--調用函數
SELECT dbo.f_lastWorkDay(2004, 8)

--DROP FUNCTION f_lastWorkDay