------------Problem------------
/*
The Employee table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.
Employee 表包含所有員工，他們的經理也屬於員工。每個員工都有一個 Id，此外還有一列對應員工的經理的 Id。

+----+-------+--------+-----------+
| Id | Name  | Salary | ManagerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | NULL      |
| 4  | Max   | 90000  | NULL      |
+----+-------+--------+-----------+

Given the Employee table, write a SQL query that finds out employees who earn more than their managers. For the above table, Joe is the only employee who earns more than his manager.
給定 Employee 表，編寫一個 SQL 查詢，該查詢可以獲取收入超過他們經理的員工的姓名。在上面的表格中，Joe 是唯一一個收入超過他的經理的員工。

+----------+
| Employee |
+----------+
| Joe      |
+----------+
*/

------------Answer------------
SELECT A.Name AS Employee
FROM(
	-- 先抓出有主管的員工資料
    SELECT *
    FROM Employee
    WHERE ManagerId IS NOT NULL
) AS A
LEFT JOIN 
(
	--預備所有員工的資料
    SELECT Id AS boss_id, Name AS boss_name, Salary AS boss_salary
    FROM Employee
) AS B
--以員工的主管ID做串接，若是有對到代表其為員工主管
ON A.ManagerId = B.boss_id
--篩選員工薪水大於主管薪水的資料
WHERE A.Salary > B.boss_salary;

--較簡短的寫法
SELECT a.Name AS 'Employee'
FROM Employee AS a, Employee AS b
WHERE a.ManagerId = b.Id
AND a.Salary > b.Salary;