------------Problem------------
/*
Given a table salary, such as the one below, that has m=male and f=female values. Swap all f and m values (i.e., change all f values to m and vice versa) with a single update statement and no intermediate temp table.

Note that you must write a single update statement, DO NOT write any select statement for this problem.

給定一個 salary 表，如下所示，有 m = 男性 和 f = 女性 的值。交換所有的 f 和 m 值（例如，將所有 f 值更改為 m，反之亦然）。要求只使用一個更新（Update）語句，並且沒有中間的臨時表。

注意，您必只能寫一個 Update 語句，請不要編寫任何 Select 語句。


| id | name | sex | salary |
|----|------|-----|--------|
| 1  | A    | m   | 2500   |
| 2  | B    | f   | 1500   |
| 3  | C    | m   | 5500   |
| 4  | D    | f   | 500    |

After running your update statement, the above salary table should have the following rows:
運行你所編寫的更新語句之後，將會得到以下表:

| id | name | sex | salary |
|----|------|-----|--------|
| 1  | A    | f   | 2500   |
| 2  | B    | m   | 1500   |
| 3  | C    | f   | 5500   |
| 4  | D    | m   | 500    |

*/

------------Answer------------
UPDATE salary
SET sex = 
(
	--利用case when來判斷，若是sex這個欄位，當原本的值為m時就修改為f，其餘情況皆修改為m
	CASE sex
		WHEN 'm' THEN 'f'
		ELSE 'm'
	END
);

--也可以用IF寫
UPDATE salary 
SET sex = IF (sex = "m", "f", "m"); --當sex為m的時候就改成f其餘都改為m

--UPDATE用法解析
/*
修改(更新)資料：使用的 SQL 指令是「UPDATE」，給定條件後，更新其原本的值
UPDATE "表格名"
SET "欄位1" = [新值]
WHERE "條件";
*/