------------Problem------------
/*
There is a table courses with columns: student and class

Please list out all classes which have more than or equal to 5 students.

For example, the table:

有一個courses 表 ，有: student (學生) 和 class (課程)。

請列出所有超過或等於5名學生的課。

例如,表:

+---------+------------+
| student | class      |
+---------+------------+
| A       | Math       |
| B       | English    |
| C       | Math       |
| D       | Biology    |
| E       | Math       |
| F       | Computer   |
| G       | Math       |
| H       | Math       |
| I       | Math       |
+---------+------------+

Should output:
應該輸出:

+---------+
| class   |
+---------+
| Math    |
+---------+

*/

------------Answer------------
SELECT class
FROM (
	-- 避免資料表中有重複的資料，所以先做去重複的動作，並利用這個已經去重複的資料表做計算
    SELECT DISTINCT student, class
    FROM courses
) AS A
-- 分不同做課程計算個數
GROUP BY class
-- 查詢條件計算後找出有學生個數大於等於5個的課程
HAVING COUNT(class) >= 5

-- HAVING函數用法解析
/*
當平時需要做一些函數運算時，要再對函數運算後產生的值來做篩選時，就不能用WHERE，這時就可以用HAVING
HAVING 子句必须放在 GROUP BY 子句之后，必须放在 ORDER BY 子句之前
*/