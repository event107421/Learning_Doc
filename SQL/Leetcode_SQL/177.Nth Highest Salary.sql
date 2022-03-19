------------Problem------------
/*

Write a SQL query to get the nth highest salary from the Employee table.
編寫一個 SQL 查詢，獲取 Employee 表中第 n 高的薪水（Salary）。

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+

For example, given the above Employee table, the nth highest salary where n = 2 is 200. If there is no nth highest salary, then the query should return null.
例如上述 Employee 表，n = 2 時，應返回第二高的薪水 200。如果不存在第 n 高的薪水，那麼查詢應返回 null。

+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+

*/

------------Answer------------
CREATE TABLE Employee(
  Id [INT] NOT NULL,
  Salary [INT] NOT NULL
);

INSERT INTO Employee SELECT '1', 100;
INSERT INTO Employee SELECT '2', 200;
INSERT INTO Employee SELECT '3', 300;
INSERT INTO Employee SELECT '4', 400;
INSERT INTO Employee SELECT '5', 500;
INSERT INTO Employee SELECT '6', 600;

-- 解法一：
/*
LIMIT：LIMIT 後面直接設定一個value，代表限制回傳回幾筆，像是 LIMIT 1 就是回傳一筆資料；也可以在後面設定兩個value，像是 LIMIT 後面接[index, count]，例如 LIMIT 2,4，參數下面說明
  index：從哪個index開始傳回，Index是從0開始算，若以這個範例來看，資料會由第3筆資料開始回傳(2+1=3)
  count：由Index開始，總共要傳回幾筆資料，以此範例來說，總共會傳回第3、4、5、6共四筆資料
OFFSET：可以把它想成要略過筆數，以OFFSET 2為例，便可想成在找到的資料筆數中略過前二筆，即是由第三筆開始回傳
*/
CREATE FUNCTION get_nth_salary(N INT) RETURNS INT
BEGIN
  SET N = N - 1;
  RETURN (
	SELECT DISTINCT Salary
	FROM Employee 
	GROUP BY Salary
	ORDER BY Salary DESC Limit 1 OFFSET 2
  );
END

-- 解法二：解法一不適用於SQL Server，因其沒有Limit函數可使用，所以這邊將解法一的方法改寫為SQL Server適用的方法
CREATE FUNCTION get_nth_salary(N INT) RETURNS INT
BEGIN
  RETURN (
	SELECT Salary
	FROM (
		SELECT Salary
		, ROW_NUMBER() OVER (ORDER BY Salary DESC) as ROWNUM
		FROM Employee
		GROUP BY Salary
	 ) AS a
	WHERE ROWNUM = N
  );
END

-- 解法三：
CREATE FUNCTION get_nth_salary(N INT) RETURNS INT
BEGIN
  RETURN (
	SELECT MAX(Salary) FROM Employee E1
	WHERE (N - 1) = (SELECT COUNT(DISTINCT(E2.Salary)) FROM Employee E2 WHERE E2.Salary > E1.Salary)
  );
END

-- 解法四：把解法三WHERE的 ">" 條件，改成 ">=" ，這樣就可以將 N-1 改成 N
CREATE FUNCTION get_nth_salary(N INT) RETURNS INT
BEGIN
  RETURN (
	SELECT MAX(Salary) FROM Employee E1
	WHERE (N) = (SELECT COUNT(DISTINCT(E2.Salary)) FROM Employee E2 WHERE E2.Salary >= E1.Salary)
  );
END