------------Problem------------
/*
Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+

PersonId is the primary key column for this table.
PersonId 是上表主鍵

Table: Address

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+

AddressId is the primary key column for this table.
AddressId 是上表主鍵

Write a SQL query for a report that provides the following information for each person in the Person table, regardless if there is an address for each of those people:
編寫一個 SQL 查詢，滿足條件：無論 person 是否有地址信息，都需要基於上述兩表提供 person 的以下信息：

FirstName, LastName, City, State

*/

------------Answer------------
SELECT A.FirstName, A.LastName, B.City, B.State
FROM Person AS A
LEFT JOIN Address AS B --因條件是無論Person這張表是否有地址的資料都要顯示，所以我們就用LEFT JOIN，就算Person在地址這張表內沒資料也要顯示NULL
ON A.PersonId = B.PersonId --用PersonId做為連接的Key值

-- 用以下語法會有問題，因為題目是要求不論是否有Address的訊息都要提供Person表內的資料，當用WHERE時就會相當於是用INNER JOIN
/*
select A.FirstName, A.LastName, B.City, B.State
from Person as A, Address as B
where A.PersonId = B.PersonId
*/

-- LEFT JOIN 用法
/*
LEFT JOIN 可以用來建立左外部連接，查詢的 SQL 敘述句 LEFT JOIN 左側資料表 (table_name1) 的所有記錄都會加入到查詢結果中，即使右側資料表 (table_name2) 中的連接欄位沒有符合的值也一樣。
所以當使用LEFT JOIN後，第一張表的紀錄會全部顯示，若是跟第二章表連接後沒有對應的值，第一張表會顯示NULL
*/