-- SQL WHILE迴圈範例 =====================================
--定義迴圈參數
DECLARE  
@TotalNum INT, --執行次數
@Num INT       --目前次數

--設定迴圈參數
SET @TotalNum = 10 --執行次數
SET @Num =1        --目前次數 

--執行WHILE迴圈
WHILE @Num <= @TotalNum  --當目前次數小於等於執行次數
BEGIN

    /*
    這裡放要執行的SQL
    */

    --設定目前次數+1
    SET @Num = @Num + 1
END

-- 利用迴圈將資料一筆一筆匯入 ==================================
-- 建立暫存表
CREATE TABLE #TEMPTABLE
(  
Number INT,     -- 號碼
Value CHAR (20) -- 說明
)

-- 定義迴圈參數
DECLARE  
@TotalNum INT,  -- 執行次數
@Num INT,       -- 目前次數
@Value CHAR (20)-- Value

-- 設定迴圈參數
SET @TotalNum = 10 -- 執行次數
SET @Num =1        -- 目前次數 

-- 執行WHILE迴圈
WHILE @Num <= @TotalNum  -- 當目前次數小於等於執行次數
BEGIN
  -- 設@Value的值
  SET @Value='這是第'+ CONVERT(varchar,@Num)+'幾次執行'
  
  -- INERT到置存表裡
  INSERT #TEMPTABLE (Number,Value)
             VALUES (@Num,@Value)

  -- 設定目前次數+1
  SET @Num = @Num + 1
END