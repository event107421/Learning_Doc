/*
程式中變數通常有分區域變數（Local Variable）與全域變數（Global Variable）
然而在 Microsoft SQL Server 裡，所有的變數都是區域變數，也就是說，所宣告的變數只能夠在同一個批次、預存程序或該變數所定義的區塊裡面被用到。
如果要宣告變數，只要使用 DECLARE 陳述式就可以了，要注意的是，變數名稱的開頭必須有 @ 符號。
*/

-- 先創一個資料表
CREATE TABLE mytable
(
	myid NVARCHAR(10),
	givenName NVARCHAR(50),
	email NVARCHAR(50)
);

-- 用Insert into一筆一筆資料進行匯入
INSERT INTO mytable SELECT '01','Brad','brad@test.com';
INSERT INTO mytable SELECT '02','Siliva','siliva@test.com';
INSERT INTO mytable SELECT '03','Allen','Allen@test.com';

-- 宣告變數的資料類別
DECLARE @find_myid NVARCHAR(10), @find_givenName nvarchar(10)

-- 檢查變數的初始值
SELECT [@find_myid] = @find_myid, [@find_givenName] = @find_givenName

-- 可以使用 SET 指派值
SET @find_myid = 01, @find_givenName = 'Siliva'

-- 或是使用 SELECT 指派值
SELECT @find_myid = 01, @find_givenName = 'Siliva'

-- 檢查變數的設定值
SELECT [@find_myid] = @find_myid, [@find_givenName] = @find_givenName

-- 宣告的變數可以直接帶入查詢式進行條件查詢
SELECT *
FROM mytable
WHERE myid = @find_myid

-- 既然已經會了宣告變數，那我們可以將其運用於製造動態語法查詢 ======================
/*
為何要製造動態語法查詢呢?因為程式語言都是以使用者為出發點，為了讓使用者很彈性，就必須寫一個複雜的查詢，此時就會讓程式設計師很痛苦

你想要給人查 1.商品符合關鍵字 2.價錢介於範圍值 3.產品種類的限制 4.人氣 5.庫存 ... 等條件，那這樣就必須寫很多條件，也就會變成Where ... and ... and ... and ... and ... and ...
那此時如果又加上判斷的語法，像是可能不選其他條件，只想下關鍵字 ... 等，那這樣就會很多的條件判斷，此時程式語法就會變得很複雜且不易閱讀

動態 SQL (Dynamic SQL) 是 T-SQL Programming 領域中非常有用的技巧，其主要目的是依據使用者所輸入的參數，變換組合 SQL 語法，可以讓開發人員撰寫出靈活、具有彈性的查詢語句
若能加以妥善操控的話，對查詢優化、效能提升也有幫助，甚至完成難以用其他做法達成的工作，但動態 SQL 非常容易遭受 SQL Injection 攻擊，所以在使用上要自行評估安全性
*/

-- 先用EXECUTE來示範如何製造動態語法查詢 ======================================
-- 宣告變數
DECLARE @SQLCommand nvarchar(200)
DECLARE @columnList nvarchar(50)
DECLARE @color varchar(10)

-- 定義變數
SET @columnList = N'ProductID 產品編號, Color 顏色'
SET @color = '''Black'''
/*
大家應該有注意到，在設定 @color 顏色變數時，在變數值的左右各用了 3 個單引號（'）來把 Black 包起來，第 1 個單引號代表變數值的型別是 nvarchar 型別，第 2 與第 3 個單引號最後會被視為只有一個單引號。
*/

-- 動態組出 T-SQL
SET @SQLCommand = 'SELECT ' + @columnList + ' FROM Production.Product WHERE Color = ' + @color

-- 執行動態組出的 T-SQL
EXECUTE (@SQLCommand)

/*
另外，除了利用動態語法組出查詢語法外，我們也可以利用ISNULL這個函數來做動態語法查詢
IsNull()函數接受2個參數，當第一個參數不為Null時，使用第一個參數；當第一個參數為Null時，使用第二個參數
參數不為Null就像是使用者選定了條件來查詢，所以 Where 欄位 = 參數 來查詢特定條件
參數為Null就像是使用者沒給條件就查詢，所以 Where 欄位 = 欄位
這是什麼意思呢，舉例來說就像是 Where 1 = 1 等於這個條件恆為真，所以會查到所有的資料
*/

DECLARE @uid int, @rank_id int, @bonus int, @bonusMoreThen int
DECLARE @account nchar(20), @password nchar(20)
DECLARE @email nchar(50), @name nvarchar(50), @nickname nvarchar(50), @phone nvarchar(50), @residence nvarchar(50)
DECLARE @date datetime, @birthday date
DECLARE @gender bit, @employee bit

set @uid = null
set @rank_id = null
set @bonus = null
set @bonusMoreThen = null

set @account = null
set @password = null

set @email = null
set @name = null
set @nickname = null
set @phone = null
set @residence = null

set @date = null
set @birthday = null

set @gender = null
set @employee = null

select * from account 
where rank_id = IsNull(@rank_id,rank_id)
and bonus = IsNull(@bonus,bonus)
and bonus > IsNull(@bonusMoreThen,1)

and account = IsNull(@account,account)
and password = IsNull(@password,password)

and email = IsNull(@email,email)
and name = IsNull(@name,name)
and nickname = IsNull(@nickname,nickname)
and phone = IsNull(@phone,phone)
and residence = IsNull(@residence,residence)

and date = IsNull(@date,date)
and birthday = IsNull(@birthday,birthday)

and gender = IsNull(@gender,gender)
and employee = IsNull(@employee,employee)

