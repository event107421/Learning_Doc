------------Problem------------
/*
Write a SQL query to rank scores. If there is a tie between two scores, both should have the same ranking. Note that after a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no "holes" between ranks.
編寫一個 SQL 查詢來實現分數排名。如果兩個分數相同，則兩個分數排名（Rank）相同。請注意，平分後的下一個名次應該是下一個連續的整數值。換句話說，名次之間不應該有“間隔”。



+----+-------+
| Id | Score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+

For example, given the above Scores table, your query should generate the following report (order by highest score):
例如，根據上述給定的 Scores 表，你的查詢應該返回（按分數從高到低排列）：

+-------+------+
| Score | Rank |
+-------+------+
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |
+-------+------+

*/

------------Answer------------
CREATE TABLE Scores(
  Id [int] NOT NULL,
  Score [float] NOT NULL
);

INSERT INTO Scores SELECT '1', 3.50;
INSERT INTO Scores SELECT '2', 3.65;
INSERT INTO Scores SELECT '3', 4.00;
INSERT INTO Scores SELECT '4', 3.85;
INSERT INTO Scores SELECT '5', 4.00;
INSERT INTO Scores SELECT '6', 3.65;

-- 解法一：在原本的分數表中，只要知道有幾個(去重複後的數字)大於原本分數表中的數字，接著再把數字自己算進去，所以再加上1，就可以得到排名了
SELECT b.score,
(
	SELECT COUNT(DISTINCT (a.score)) + 1
	FROM scores AS a
	WHERE a.score > b.score
) AS rank_num
FROM scores AS b
ORDER BY b.score DESC

-- 解法二：判斷原本的分數表中去重複後，各個數字有幾個數是小於等於它的，最後計算完個數後，因為有重複的數字已經被排除了，此時再把結果串回原本的表
SELECT A.Score, C.Sales_Rank
FROM (
	SELECT Score
	FROM Scores
) AS A
LEFT JOIN (
	SELECT Score, COUNT(Sales_Rank) AS Sales_Rank
	FROM (
		SELECT DISTINCT s1.Score, s2.Score AS Sales_Rank
		FROM Scores AS s1, Scores AS s2
		WHERE s1.Score <= s2.Score
		-- OR (s1.Score = s2.Score AND s1.Name = s2.Name) --如果有人名的話要再去比對人名
	) AS B
	GROUP BY Score
) AS C
ON A.Score = C.Score
ORDER BY A.Score DESC




