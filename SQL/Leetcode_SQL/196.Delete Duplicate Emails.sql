------------Problem------------
/*
Write a SQL query to delete all duplicate email entries in a table named Person, keeping only unique emails based on its smallest Id.
編寫一個 SQL 查詢，來刪除 Person 表中所有重複的電子郵箱，重複的郵箱裡只保留 Id 最小的那個。

+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+

Id is the primary key column for this table.

For example, after running your query, the above Person table should have the following rows:
例如，在運行你的查詢語句之後，上面的 Person 表應返回以下幾行:

+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+

Note:

Your output is the whole Person table after executing your sql. Use delete statement.

*/

------------Answer------------
DELETE
-- SELECT *
FROM Person
-- 因為要把重複的資料刪除，保留最小ID的那筆，所以只要不在挑選出來的每個Email最小ID內，代表就是重複的資料並且ID不是重複資料內最小的
WHERE Id NOT IN(
	-- 此時已經找出每個Email的最小ID，所以就只要挑選這個欄位就好
    SELECT Id 
    FROM (
		-- 因為內部有重複資料，所以若是要去重複資料並且保留ID最小那筆，那就需要先找出每個Email其最小的ID
        SELECT MIN(Id) AS Id, Email
        FROM Person
        GROUP BY Email
    ) AS t
)

-- 另一解法
DELETE p1
-- SELECT p1.*
FROM Person AS p1, Person AS p2
WHERE p1.Email = p2.Email -- 因為我們是要刪除重複資料內ID不是最小的那筆資料，那也可以用WHERE來做篩選，把此張資料表做比對，當Email相同
AND p1.Id > p2.Id -- 就找出ID較大的那筆，就是所要刪除的那筆資料

-- DELETE函數用法
/*
如果需要在某些條件下直接由資料庫中去除一些資料。這可以藉由 DELETE FROM 指令來達成
DELETE FROM table_name
WHERE column_name operator value;

WHERE 條件式記得要加哦！不然 "全部的" 資料都會刪除了
*/

