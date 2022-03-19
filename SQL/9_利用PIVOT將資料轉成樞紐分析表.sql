/*
利用 PIVOT 扭轉資料，由直列轉為橫向資料(Long data to wide data)
面對數筆有意義資料要匯總成橫式資料時，可以考慮使用 PIVOT 來扭轉資料，讓資料呈現上更貼近人性
*/

-- EX1. 以下面為範例：
SELECT class, round((cast(a AS float) / cast((a + b + c) AS float)), 4)
FROM (
  -- 第一個區塊
  SELECT class, [2] AS 'a', [3] AS 'b', [4] AS 'c'
  FROM (
    SELECT class, record, status
    FROM #test
    WHERE status IN ('2', '3', '4')
  ) AS A
  PIVOT
  (
    -- 第二區塊
    SUM(record)
    -- 第三個區塊
    FOR status IN ([2], [3], [4])
  ) AS pivot_table
) AS B

/*
可以看到 PIVOT 語法使用上主要區分為三個區塊，第一個區塊當然就是撈出所需資料
接著第二區塊則利用 PIVOT 語法設定需匯總的欄位與方式
第三個區塊設定轉置欄位及其特定資料作為新欄位
執行後成功將個別獨立的資料轉置匯總呈橫向總表囉
*/

-- EX2. 使用 PIVOT，呈現各月(1~12月)的客戶消費彙總金額 ==============================
-- OrderMonth 資料行，資料類型是 INT
/*
在 PIVOT 的 IN 子句內：
使用數字當做資料行的名稱時，前後使用方括號[] 或 雙引號 ""
*/
SELECT *
FROM myInvoices
 PIVOT (SUM(SubTotal)
  FOR OrderMonth IN ([1],[2],[3], [4], [5],[6],[7],[8],[9],[10],[11],[12])) pvt
GO

-- EX3. 動態組合 PIVOT 陳述式，呈現各月(1~12月)的客戶消費彙總金額 
-- OrderMonth 資料行，資料類型是 INT
/*
QUOTENAME (Transact-SQL)
傳回 Unicode 字串，且附加了分隔符號，以便使輸入字串成為有效的 SQL Server 分隔識別碼。
*/
 
-- 01_sp_executesql + PIVOT + COALESCE() + QUOTENAME：適用 SQL Server 2005 版本
DECLARE @ColumnGroup NVARCHAR(MAX), @PivotSQL NVARCHAR(MAX) 

SELECT @ColumnGroup = COALESCE(@ColumnGroup + ',' ,'' ) + QUOTENAME(OrderMonth) 
FROM myInvoices 
GROUP BY QUOTENAME(OrderMonth) 
SELECT @PivotSQL = N'
SELECT * FROM myInvoices PIVOT (SUM(SubTotal) FOR OrderMonth 
 IN (' + @ColumnGroup +  N') ) AS pvt'
 
EXEC sp_executesql  @PivotSQL;
GO


CREATE TABLE #a(
  class varchar(20) NULL,
  data_date date NULL,
  status varchar(20) NULL,
  records int
);

INSERT INTO #a select 'a', '2019-04-01', 'current', '10'
INSERT INTO #a select 'a', '2019-04-01', 'M1', '12'
INSERT INTO #a select 'a', '2019-04-01', 'M2', '15'
INSERT INTO #a select 'a', '2019-04-01', 'M3', '1'
INSERT INTO #a select 'a', '2019-04-01', 'M4', '2'
INSERT INTO #a select 'a', '2019-04-02', 'current', '5'
INSERT INTO #a select 'a', '2019-04-02', 'M1', '1'
INSERT INTO #a select 'a', '2019-04-02', 'M2', '14'
INSERT INTO #a select 'a', '2019-04-02', 'M3', '20'
INSERT INTO #a select 'a', '2019-04-02', 'M4', '2'
INSERT INTO #a select 'a', '2019-04-03', 'current', '10'
INSERT INTO #a select 'a', '2019-04-03', 'M1', '12'
INSERT INTO #a select 'a', '2019-04-03', 'M2', '15'
INSERT INTO #a select 'a', '2019-04-03', 'M3', '1'
INSERT INTO #a select 'a', '2019-04-03', 'M4', '2'
INSERT INTO #a select 'a', '2019-04-04', 'current', '5'
INSERT INTO #a select 'a', '2019-04-04', 'M1', '1'
INSERT INTO #a select 'a', '2019-04-04', 'M2', '14'
INSERT INTO #a select 'a', '2019-04-04', 'M3', '20'
INSERT INTO #a select 'a', '2019-04-04', 'M4', '2'
INSERT INTO #a select 'a', '2019-04-05', 'current', '10'
INSERT INTO #a select 'a', '2019-04-05', 'M1', '12'
INSERT INTO #a select 'a', '2019-04-05', 'M2', '15'
INSERT INTO #a select 'a', '2019-04-05', 'M3', '1'
INSERT INTO #a select 'a', '2019-04-05', 'M4', '2'
INSERT INTO #a select 'a', '2019-04-06', 'current', '5'
INSERT INTO #a select 'a', '2019-04-06', 'M1', '1'
INSERT INTO #a select 'a', '2019-04-06', 'M2', '14'
INSERT INTO #a select 'a', '2019-04-06', 'M3', '20'
INSERT INTO #a select 'a', '2019-04-06', 'M4', '2'
INSERT INTO #a select 'b', '2019-04-01', 'current', '100'
INSERT INTO #a select 'b', '2019-04-01', 'M1', '15'
INSERT INTO #a select 'b', '2019-04-01', 'M2', '1'
INSERT INTO #a select 'b', '2019-04-01', 'M3', '16'
INSERT INTO #a select 'b', '2019-04-01', 'M4', '20'
INSERT INTO #a select 'b', '2019-04-02', 'current', '5.'
INSERT INTO #a select 'b', '2019-04-02', 'M1', '12'
INSERT INTO #a select 'b', '2019-04-02', 'M2', '140'
INSERT INTO #a select 'b', '2019-04-02', 'M3', '24'
INSERT INTO #a select 'b', '2019-04-02', 'M4', '22'
INSERT INTO #a select 'b', '2019-04-03', 'current', '100'
INSERT INTO #a select 'b', '2019-04-03', 'M1', '15'
INSERT INTO #a select 'b', '2019-04-03', 'M2', '1'
INSERT INTO #a select 'b', '2019-04-03', 'M3', '16'
INSERT INTO #a select 'b', '2019-04-03', 'M4', '20'
INSERT INTO #a select 'b', '2019-04-04', 'current', '5.'
INSERT INTO #a select 'b', '2019-04-04', 'M1', '12'
INSERT INTO #a select 'b', '2019-04-04', 'M2', '140'
INSERT INTO #a select 'b', '2019-04-04', 'M3', '24'
INSERT INTO #a select 'b', '2019-04-04', 'M4', '22'
INSERT INTO #a select 'b', '2019-04-05', 'current', '100'
INSERT INTO #a select 'b', '2019-04-05', 'M1', '15'
INSERT INTO #a select 'b', '2019-04-05', 'M2', '1'
INSERT INTO #a select 'b', '2019-04-05', 'M3', '16'
INSERT INTO #a select 'b', '2019-04-05', 'M4', '20'
INSERT INTO #a select 'b', '2019-04-06', 'current', '5.'
INSERT INTO #a select 'b', '2019-04-06', 'M1', '12'
INSERT INTO #a select 'b', '2019-04-06', 'M2', '140'
INSERT INTO #a select 'b', '2019-04-06', 'M3', '24'
INSERT INTO #a select 'b', '2019-04-06', 'M4', '22'


SELECT *
FROM #a
PIVOT (
  SUM(records)
  FOR data_date IN ([2019-04-01], [2019-04-02], [2019-04-03], [2019-04-04], [2019-04-05], [2019-04-06])
) AS pv


DECLARE @cols NVARCHAR(MAX)= N'' --儲存動態欄位之用
SELECT @cols = @cols + iif(@cols = N'',QUOTENAME(data_date),N',' + QUOTENAME(data_date))
FROM 
(
    SELECT DISTINCT(data_date) 
    FROM #a 
) as t

print @cols

DECLARE @sql NVARCHAR(MAX)
-- 組動態SQL語法，將語法先設定為字串(紅色部分)
SET @sql = N'
SELECT class, status, ' + @cols + '
FROM #a
PIVOT
(
  SUM(records) 
  FOR data_date
  IN ('
  + @cols
  + ')
) AS t'

PRINT @sql
EXEC sp_executesql @sql