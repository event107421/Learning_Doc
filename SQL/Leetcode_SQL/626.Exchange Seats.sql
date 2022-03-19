------------Problem------------
/*

Mary is a teacher in a middle school and she has a table seat storing students' names and their corresponding seat ids.

The column id is continuous increment.
 

Mary wants to change seats for the adjacent students.
 

Can you write a SQL query to output the result for Mary?

小美是一所中學的信息科技老師，她有一張 seat 座位表，平時用來儲存學生名字和與他們相對應的座位 id。

其中縱列的 id 是連續遞增的

小美想改變相鄰倆學生的座位。

你能不能幫她寫一個 SQL query 來輸出小美想要的結果呢？


+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Abbot   |
|    2    | Doris   |
|    3    | Emerson |
|    4    | Green   |
|    5    | Jeames  |
+---------+---------+

For the sample input, the output is:

假如數據輸入的是上表，則輸出結果如下：

+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Doris   |
|    2    | Abbot   |
|    3    | Green   |
|    4    | Emerson |
|    5    | Jeames  |
+---------+---------+
Note:
If the number of students is odd, there is no need to change the last one's seat.

注意：

如果學生人數是奇數，則不需要改變最後一個同學的座位。

*/

------------Answer------------
SELECT 
(
	CASE 
		--id代表學生人數，相鄰要換座位，也就代表說1變2，2變1，可以利用餘數來判斷，若是為1而且其id等於學生人數，代表學生人數為奇數，此同學不須換座位
		WHEN id%2 = 1 AND id = (SELECT COUNT(*) FROM (SELECT DISTINCT student FROM seat) AS A) THEN id
		--當id除以2餘數為1的時候，將原來的id + 1
		WHEN id%2 = 1 THEN id + 1
		--其餘情況，也就是除以2整除的情況，那就把id - 1
		ELSE id - 1
	END
) AS id, student
FROM seat
-- 再按照更換後的id排序，即可得到換座位後的資料
ORDER BY id

--CASE WHEN用法解析
/*
CASE 是 SQL 用來做為 IF-THEN-ELSE 之類邏輯的關鍵字
使用 IF...ELSE 的缺點就是當條件一多時，程式碼看去就不容易懂，維護起來也不方便。所以 SQL Server 特別提供了另外一個簡單的指令：CASE...WHEN。
*/

--IF用法解析
/*
SQL語法可以做一些簡單的判斷式
IF(判斷式,TRUE,FALSE)
*/
