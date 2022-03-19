------------Problem------------
/*
Given a Weather table, write a SQL query to find all dates' Ids with higher temperature compared to its previous (yesterday's) dates.
給定一個 Weather 表，編寫一個 SQL 查詢，來查找與之前（昨天的）日期相比溫度更高的所有日期的 Id。

+---------+------------------+------------------+
| Id(INT) | RecordDate(DATE) | Temperature(INT) |
+---------+------------------+------------------+
|       1 |       2015-01-01 |               10 |
|       2 |       2015-01-02 |               25 |
|       3 |       2015-01-03 |               20 |
|       4 |       2015-01-04 |               30 |
+---------+------------------+------------------+

For example, return the following Ids for the above Weather table:
例如，根據上述給定的 Weather 表格，返回如下 Id:

+----+
| Id |
+----+
|  2 |
|  4 |
+----+

*/

------------Answer------------
SELECT w1.Id
FROM Weather AS w1
INNER JOIN Weather AS w2
ON DATEDIFF(DAY, w1.RecordDate, w2.RecordDate) = -1 --合併的條件是找昨日的日期，所以這時可以利用DATEDIFF來計算資料表內各個日期的差異天數，串接的條件就是找到兩個日期的差為-1，也就是w1的日期比w2大
AND w1.Temperature > w2.Temperature --找比昨日氣溫還高的今日日期

-- DATEDIFF函數用法解析
/*
DATEDIFF是算兩個日期間的間隔，傳回帶正負號的整數
DATEDIFF ( datepart , startdate , enddate )
datepart為間隔的單位，startdate跟enddate應該看字面的意思就知道了吧。

因此如果語法寫
SELECT DATEDIFF(DAY, '2010-10-03','2010-10-04'  )
出來的結果就是 1，代表相隔一天。
*/

-- DATEADD
/*
DATEADD是計算某日期加上一個數值，傳回的日期
DATEADD (datepart , number , date )
datepart一樣是單位，number是指定的數值，date是要被加上的原始日期

SELECT DATEADD(MONTH,2,'2010-10-06')

傳回的結果是2010-12-06 00:00:00.000
*/