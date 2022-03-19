------------Problem------------
/*
Write a SQL query to find all duplicate emails in a table named Person.
編寫一個 SQL 查詢，查找 Person 表中所有重複的電子郵箱
+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+

For example, your query should return the following for the above table:
根據以上輸入，你的查詢應返回以下結果：

+---------+
| Email   |
+---------+
| a@b.com |
+---------+
*/

------------Answer------------
SELECT Email
FROM (
	-- 先計算每個Email在資料表內有幾筆
	SELECT Email, COUNT(Email) AS num
	FROM Person
	GROUP BY Email
) AS A
WHERE num > 1 -- 接著利用子查詢的方式，找出筆數大於1的Email

-- 也可以用having解法
SELECT Email
FROM Person
GROUP BY Email
-- 另外也可以先對其做Email筆數的計算，再利用HAVING對計算後的值做篩選，找出大於1筆的資料
HAVING COUNT(Email) > 1;

-- 子查詢用法解析
/*
可以在一個 SQL 語句中放入另一個 SQL 語句。當我們在 WHERE 子句或 HAVING 子句中插入另一個 SQL 語句時，我們就有一個子查詢 (Subquery) 的架構。
子查詢的作用是什麼呢？第一，它可以被用來連接表格。另外，有的時候子查詢是唯一能夠連接兩個表格的方式。
子查詢的語法如下：
SELECT "欄位1" 
FROM "表格" 
WHERE "欄位2" [比較運算素] 
(
	SELECT "欄位1" 
	FROM "表格"
	WHERE "條件"
);
*/