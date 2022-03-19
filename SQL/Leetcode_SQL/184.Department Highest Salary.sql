------------Problem------------
/*
The Employee table holds all employees. Every employee has an Id, a salary, and there is also a column for the department Id.
Employee 表包含所有員工信息，每個員工有其對應的 Id, salary 和 department Id。

+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |
+----+-------+--------+--------------+

The Department table holds all departments of the company.
Department 表包含公司所有部門的信息。

+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+

Write a SQL query to find employees who have the highest salary in each of the departments. For the above tables, your SQL query should return the following rows (order of rows does not matter).

Explanation:

Max and Jim both have the highest salary in the IT department and Henry has the highest salary in the Sales department.

編寫一個 SQL 查詢，找出每個部門工資最高的員工。例如，根據上述給定的表格，Max、Jim 在 IT 部門有最高工資，Henry 在 Sales 部門有最高工資。

+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| IT         | Jim      | 90000  |
| Sales      | Henry    | 80000  |
+------------+----------+--------+

Explanation:

Max and Jim both have the highest salary in the IT department and Henry has the highest salary in the Sales department.


*/

------------Answer------------
--較佳解法
SELECT d.Name AS Department, e.Name AS Employee, e.Salary 
FROM Employee AS e, Department AS d 
-- 利用部門ID，將其部門名稱串回查詢結果
WHERE e.DepartmentId = d.id
-- 上述查詢條件完成後，找出包含最高薪水以及部門ID的資料
AND (e.Salary, e.DepartmentId) IN 
(
	-- 先找出每個部門的最高薪資
	SELECT MAX(Salary), DepartmentId 
	FROM Employee 
	GROUP BY DepartmentId
);


-- 這解法會有一個問題，如果只有一筆員工資料時也會顯示
SELECT Employee_Department.Department, e.Name AS Employee, Employee_Department.salary
FROM 
(
	SELECT MAX(A.Salary) AS Salary, A.DepartmentId, B.Name AS Department
	FROM Employee AS A
	-- 將部門名稱串回Employee表
	LEFT JOIN Department AS B
	ON A.DepartmentId = B.Id
	-- 按照部門的ID以及部門名稱取出個別最高的薪資員工
	GROUP BY A.DepartmentId, B.Name
) AS Employee_Department
--接著利用取出來的部門ID以及各部門分別最高的薪水，找出這些員工
LEFT JOIN Employee AS e
ON Employee_Department.DepartmentId = e.DepartmentId
AND Employee_Department.Salary = e.Salary