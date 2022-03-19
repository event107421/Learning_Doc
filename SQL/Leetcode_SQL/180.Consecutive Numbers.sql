------------Problem------------
/*
Write a SQL query to find all numbers that appear at least three times consecutively.
編寫一個 SQL 查詢，查找所有至少連續出現三次的數字。

+----+-----+
| Id | Num |
+----+-----+
| 1  |  1  |
| 2  |  1  |
| 3  |  1  |
| 4  |  2  |
| 5  |  1  |
| 6  |  2  |
| 7  |  2  |
+----+-----+

For example, given the above Logs table, 1 is the only number that appears consecutively for at least three times.
例如，給定上面的 Logs 表， 1 是唯一連續出現至少三次的數字。

+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+

*/

------------Answer------------
CREATE TABLE logs(
  Id [int] NOT NULL,
  Num [int] NOT NULL
);

INSERT INTO logs SELECT '1', '1';
INSERT INTO logs SELECT '2', '1';
INSERT INTO logs SELECT '3', '1';
INSERT INTO logs SELECT '4', '2';
INSERT INTO logs SELECT '5', '1';
INSERT INTO logs SELECT '6', '2';
INSERT INTO logs SELECT '7', '2';

-- 解法一：
SELECT DISTINCT num AS ConsecutiveNums
FROM (
	SELECT num, orde, COUNT(*) AS num_count
	FROM(
		SELECT Id, num, ROW_NUMBER() OVER(ORDER BY Id) - ROW_NUMBER() OVER(PARTITION BY num ORDER BY Id) AS orde
		FROM logs
	) AS w
	GROUP BY  num, orde
) AS s
WHERE num_count >= 3

-- 解法二：雖然此種方法只判斷下一筆及下兩筆資料，但後續再次出現也是符合至少三次出現的條件，只是這種方法在資料量大的時候會衍生很多資料，不太好的做法
SELECT DISTINCT l1.Num AS ConsecutiveNums
FROM logs AS l1
LEFT JOIN logs AS l2 
ON l1.Num = l2.Num
LEFT JOIN logs l3 
ON l2.Num = l3.Num
WHERE l1.id = l2.id -1 
AND l2.id = l3.id -1

-- 解法三：利用LAG或LEAD函數來取得下一筆及下兩筆的資料，接著判斷當前數字減去下一筆及下兩筆的資料等於0時，代表此數字已經連續第三次出現，後續再次出現也是符合至少三次出現的條件，但如果要判斷連續出現的次數更多時，程式碼就更多行
/*
LAG 函數可以給定三個參數：指定的欄位、位移的列數、預設值，其中預設值則是選擇性輸入
然後需要搭配 OVER ( [ partition_by_clause ] order_by_clause) 語法來指定排序的規則，[ partition_by_clause ]代表排序結果需不需要分組
*/
SELECT Num AS ConsecutiveNums
FROM (
	SELECT Id
	, Num
	, LAG(Num, 1, 0) OVER(ORDER BY Id) as last_1
	, LAG(Num, 2, 0) OVER(ORDER BY Id) as last_2
	FROM logs
) AS a
WHERE Num - last_1 = 0
AND Num - last_2 = 0
