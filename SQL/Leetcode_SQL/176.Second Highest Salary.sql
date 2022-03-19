--Second Highest Salary
/*
Write a SQL query to get the second highest salary from the Employee table.
編寫一個 SQL 查詢，獲取 Employee 表中第二高的薪水（Salary）。

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+

For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.
例如上述 Employee 表，SQL查詢應該返回 200 作為第二高的薪水。如果不存在第二高的薪水，那麼查詢應返回 null。

+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+

*/

------------Answer------------
SELECT ISNULL((
	SELECT salary
	FROM(
		--接著利用已經去重複的薪資，對其做排序，並創出排序的號碼
		SELECT salary, ROW_NUMBER()over(ORDER BY salary DESC) AS row_num
		FROM(
				--先將薪資去重複，再從這些不重複的薪資中找出第二高的薪資數字
				SELECT DISTINCT salary FROM Employee 
			) AS A
		) AS B
	--這時已經得到排序的號碼了，我們需要的是第二高的薪水，所以取ROW_NUMBER為2的資料
	WHERE row_num = 2
--而這個題目會有一個問題，當資料只有一筆的時候就不會有第二高的薪水，所以就讓他回傳NULL
), NULL) AS SecondHighestSalary;

--另一解法
SELECT ISNULL((
	--對salary這個欄位做去重複的動作
	SELECT DISTINCT Salary
    FROM Employee
	--接著對其做由大到小排序
    ORDER BY Salary DESC
    OFFSET 1 ROWS --使用 OFFSET 和 FETCH 子句：依據薪資排序，但是跳過前 1 筆資料列
	FETCH NEXT 1 ROWS ONLY --取下一筆資料(第二筆)
--當資料只有一筆的時候就不會有下一筆，所以就讓他回傳NULL
), NULL) AS SecondHighestSalary

-- 函數用法補充 ===================================================================
-- ISNULL用法解析
/*
ISNULL 函數：以指定的取代值來取代 NULL。
ISNULL ( check_expression , replacement_value )

check_expression
這是要檢查 NULL 的運算式。check_expression 可以是任何類型。

replacement_value
這是 check_expression 是 NULL 時所傳回的運算式。replacement_value 必須是能夠隱含地轉換成 check_expresssion 類型的類型。
*/

-- ROW_NUMBER用法解析
/*
ROW_NUMBER為查詢的結果加上序號
也就是依照指定的方式對欄位排序，並逐筆加上順號的方式
*/

-- OFFSET & FETCH NEXT用法解析
/*
OFFSET - FETCH 是 ORDER BY 子句的延伸功能。

使用 OFFSET 和 FETCH 限制傳回的資料列。
讓你可以過濾篩選特定範圍的資料列。

提供了對結果集的分頁處理功能。
可以指定跳過的行數，指定要取回的資料列筆數。

而且，OFFSET 和 FETCH 子句是依據 draft ANSI SQL:2011 標準。
因此，會比 TOP 子句具備更好的 SQL 語言相容性。

ORDER BY {order_by_list}
OFFSET {offset_value} ROW(S)
FETCH FIRST|NEXT {fetch_value} ROW(S) ONLY

OFFSET N ROWS：代表略過Ｎ筆開始（可以單獨使用不用加上FETCH子句）
FETCH NEXT M ROWS ONLY：代表取接下來Ｍ筆資料（一定要配合OFFSET子句使用)
*/
