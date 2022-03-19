-- Stored Routines（預存程序） =======================================
/* 在資料庫管理系統的應用中，不論是一般或網頁的應用程式，它們在執行資料查詢與維護的時候，都必須使用SQL敘述來請資料庫執行各種不同的工作。在比較複雜的應用程式需求下，很常會遇到類似下列的一組工作敘述： */
-- 如果表格存在就刪除
DROP TABLE IF EXISTS mycountry

-- 設定要處理的代碼
SET @my_code = 'JPN'

-- 查詢國家的人口數
-- SET您可以使用語句或在查詢中初始化此變量：SET @var = 1、SELECT @var2 := 2
SELECT @pop_var := Population
FROM country
WHERE Code = @my_code

-- 建立新表格
CREATE TABLE mycountry
SELECT Code, Name, GNP, Population
FROM country
WHERE Code = @my_code OR Population > @pop_var
ORDER BY Population

/*
但SQL敘述的特點是一次只能執行一件工作，所以要完成上列的工作，就必須執行數個SQL敘述
如果這樣的一組工作是很常執行的，就可以考慮把這些要執行的敘述建立為「Stored procedure」元件，如下：
*/
CREATE PROCEDURE new_mycountry [接上面的所有SQL敘述]

/* 就可以把這一組工作建立為Stored procedure元件，以後要執行這些工作時，可以直接「呼叫、call」這個建立好的Stored procedure元件即可，如下： */
CALL new_mycountry('JPN')

/*
Stored procedures是Stored routines其中一種元件，你可以視需要在資料庫中建立許多不同用途的Stored procedure
它可以包含你需要執行的一組工作，也可以依照需求設定必要的參數資料(例如上列「new_mycountry」中的國家代碼)
呼叫這些建立好的Stored procedure可以幫你省掉很多繁複的工作，請資料庫一次完成你要執行的工作
*/

/* Stored routines另外提供一種「Stored functions」元件，除了MySQL資料庫提供許多各種不同的函式外，你也可以建立自己的函式，這種函式稱為Stored functions。例如下列的範例： */
CREATE FUNCTION ROUND2 ... RETURNS double(30, 2)

/*
你同樣可以在資料庫中建立許多需要的Stored functions，把一些比較複雜工作建立為Stored functions元件以後，你就可以跟使用MySQL提供的函式一樣來使用它們，同樣可以簡化許多繁複的工作
在MySQL資料庫管理系統中，把Stored procedures與Stored functions合稱為「Stored routines」
*/

-- 所以從上面的例子，整理一下建立Stored Routines的方法：
CREATE PROCEDURE proc_name ([parameters])
　　[characteristics]
　　routine_body

CREATE FUNCTION func_name ([parameters])
RETURNS data_type
　　[characteristics]
　　routine_body

/*
其中characteristics可使用的參數為：
SQL Security {INVOKER|DEFINER}：指定routine要以建立者或執行者的權限執行。
DETERMINISTIC or NOT DETERMINISTIC：對於相同的input data若routine每次執行時都能產出相同的結果，則該routine即為DETERMINISTIC。預設值為NOT DETERMINISTIC 。
LANGUAGE SQL：routine所使用的語言，目前只支援SQL。
COMMENT 'string'：用來指定routine的註解。
*/

/*
從上述可知，Stored Routines有兩種形式，一是Stored procedures、另一Stored functions，兩種都是將一些常用的作業寫成預儲程式讓user調用，但有一些差異：
ㄧ、名稱與參數：procedure或function，名稱都需要有括弧，即使沒有任何參數。參數預設都是IN型態，所以可以省略，但是OUT跟INOUT須明確打出來，如範例一
二、DELIMITER：大致是說，所有的敘述，預設用分號(;)作為每一句敘述的結束，而stored routines裏頭有許多敘述，所以有許多分號，但是要告訴SQL把routine當成一整個敘述，裏頭的分號不管，所以要改變delimiter，可以是$$或//，只要不是分號就行，在routine的結尾用這個新的delimiter，如範例二
*/

/*
其他Stored Procedures與Stored Functions的差異
1. Procedure的Parameter可以定義為IN, OUT, INOUT，而Function的Parameter則必定是IN(系統預設，不能自行指定)。
2. Function必定有回傳值，因此必須包含一個RETURNS子句來定義傳回值的資料型態。
3. Procedure可以直接產生單一或多個Result Set，但Function不行。

-- 說明一下使用Stored Routines的優點：
更彈性的SQL語法
錯誤處理能力
合於SQL標準
程式碼封裝
可重覆利用
分離程式邏輯
易於維護
減少所需的網路頻寬
更好的安全性
*/

-- 範例一 ===============================
/* 無參數 */
CREATE PROCEDURE my_proc ()
 
/* var1為IN型態 */
CREATE PROCEDURE my_proc (var1 INT, OUT var2 VARCHAR(10))


-- 範例二 ===============================
-- Stored Procedure 範例
/* 定義PROCEDURE */
DELIMITER $$
CREATE PROCEDURE my_proc (IN var1 INT, OUT var2 INT)
BEGIN
  SET var2 = var1 + 100;
END $$
DELIMITER ;
 
/* 調用PROCEDURE */
CALL my_proc (1, @ret);
SELECT @ret; -- output 101
 
/* 定義PROCEDURE - 返回result sets */
DELIMITER $$
CREATE PROCEDURE my_proc2 ()
BEGIN
  SELECT * FROM categories;
END $$
DELIMITER ;
 
/* 調用PROCEDURE - 接收result sets */
CALL my_proc2();  -- output categories所有資料列

-- Stored Function 範例
/* 定義FUNCTION */
DELIMITER $$
CREATE FUNCTION my_func (var1 INT, var2 INT)
  -- 返回值的資料型態
  RETURNS INT
  -- 表示只要輸入的資料一樣, 返回值也會相同.
  DETERMINISTIC
BEGIN
  DECLARE ret_val INT;
  SET ret_val := var1 + var2;
  RETURN ret_val;
END $$
/* 調用FUNCTION output 3 */
SELECT my_func(1, 2);

/*
修改Stored Routines =============================================
只可以用來修改routine的characteristics，而且只可以用來修改SQL SECURITY與COMMENT。

ALTER PROCEDURE proc_name [characteristics]
ALTER FUNCTION func_name [characteristics]

ALTER FUNCTION f
　　SQL SECURITY INVOKER
　　COMMENT 'this is a comment';

註：characteristics的撰寫順序不重要。

刪除Stored Routine ==============================================
DROP PROCEDURE [IF EXISTS] proc_name
DROP FUNCTION [IF EXISTS] func_name
若是沒有加上IF EXISTS，則當要刪除的routine不存在時會產生error；加上IF EXISTS後，當要刪除的routine不存在時只會產生warning。

取得Stored Routine的Metadata ====================================
  SELECT * FROM INFORMATION_SCHEMA.ROUTINES
  WHERE ROUTINE_NAME = 'routine_name'
  AND ROUTINE_SCHEMA='db_name';
  SHOW PROCEDURE STATUS LIKE 'w%';
  SHOW FUNCTION STATUS;
  SHOW CREATE PROCEDURE proc_name;
  SHOW CREATE FUNCTION func_name;
  Stored Routine Privileges and Execution Security
  CREATE ROUTINE
  EXECUTE
  ALTER ROUTINE
  GRANT OPTION
*/

-- 接下來討論預存程序內的傳遞參數方法 ================================
-- 在MySQL中預儲程序參數有以下三種方法：
-- 預存程序傳參：預存程序的括弧裡，可以聲明參數，命令如下：
CREATE PROCEDURE p([in/out/inout] 參數名  參數類型 ..)

-- in：給參數傳入值，定義的參數就得到了值，範例如下：
CREATE PROCEDURE p1(IN num INT)  
BEGIN  
  DECLARE i INT DEFAULT 0;  
  DECLARE total INT DEFAULT 0;  
  WHILE i<=num DO  
    SET total := i + total;  
    SET i := i+1;  
  END WHILE;  
  SELECT total;  
END

-- out：模式定義的參數只能在過程體內部賦值，表示該參數可以將某個值傳遞迴調用他的過程（在預存程序內部，該參數初始值為 null，無論調用者是否給預存程序參數設定值）
CREATE PROCEDURE p2(OUT num INT)  
BEGIN  
 SELECT num AS num_1;  
 IF (num IS NOT NULL) THEN  
 SET num = num + 1;  
 SELECT num AS num_2;  
 ELSE  
 SELECT 1 INTO num;  
 END IF;  
 SELECT num AS num_3;  
END
SET @num = 10;  
CALL p2(@num);
SELECT @num AS num_out;

-- inout：調用者還可以通過 inout 參數傳遞值給預存程序，也可以從預存程序內部傳值給調用者
CREATE PROCEDURE p3(INOUT age INT)  
BEGIN  
  SET age := age + 20;  
END
SET @currage =18;
CALL p3(@currage);  
SELECT @currage; 

/*
所以如果僅僅想把資料傳給 MySQL 預存程序，那就使用"in"型別參數
如果僅僅從 MySQL 預存程序傳回值，那就使用"out"型別參數
如果需要把資料傳給 MySQL 預存程序，還要經過一些計算後再傳回給我們，此時，要使用"inout"型別參數
*/

