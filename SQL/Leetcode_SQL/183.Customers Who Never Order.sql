------------Problem------------
/*
Suppose that a website contains two tables, the Customers table and the Orders table. Write a SQL query to find all customers who never order anything.
某網站包含兩個表，Customers 表和 Orders 表。編寫一個 SQL 查詢，找出所有從不訂購任何東西的客戶。

Table: Customers.

+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+

Table: Orders.

+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+

Using the above tables as example, return the following:
例如給定上述表格，你的查詢應返回：

+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
*/

------------Answer------------
SELECT A.Name AS Customers
FROM Customers AS A
LEFT JOIN Orders AS B --用LEFT JOIN，將Customers表連接Orders表，此時，若是Customers內的人沒有買過東西在Orders表內就不會有資料，那串接後的結果就會出現NULL
ON A.Id = B.CustomerId
WHERE B.CustomerId IS NULL --接著我們對查詢結果下條件，找出結果為NULL的客戶，這就是沒有買過東西的客戶資料

-- 另一個解法
SELECT Name AS Customers
FROM Customers
WHERE Id NOT IN --也可用WHERE來找在另外一張表內沒有的Id，也就代表是沒有訂購任何東西的客戶
(
    SELECT CustomerId FROM Orders
)