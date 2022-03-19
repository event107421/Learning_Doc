/* 
CTE是一個「暫存」且「具名」的結果集合
CTE 會暫時儲存 AS 括號中的 Query 結果，用在同一個執行中 SELECT 、 INSERT 、 UPDATE 、 DELETE
或是 CREATE VIEW 的 SELECT 上，也可以在定義 CTE 的 Query 中使用，今天介紹的遞迴就是一個例子
*/

-- 定義 CTE 的 名稱 和 欄位
WITH sampleCTE (id, name, phoneNumber, age)  
AS
-- 定義 CTE 的 Query  
(  
    SELECT
      id,
      name,
      phoneNumber,
      date_part('year', NOW()) - date_part('year', dob) AS age  
    FROM member
    WHERE phoneNumber IS NOT NULL  
)
-- 使用 CTE
SELECT *  
FROM sampleCTE
WHERE age >= 18

/*
遞迴查詢 (Recursive Query)：
定義遞迴查詢 CTE 的概念大致上是
1.取得所有資料作為第一層
2.資料 INNER JOIN CTE 取得下一層的資料(INNER JOIN的條件會根據下面兩點，稍微有點不同)
  儲存結構 (儲存 Parent 或是 Child)
  查詢目標 (查詢 Parent 或是 Child)
3.步驟 1 UNION 步驟 2
*/

-- 假設資料為某家族的族譜，查詢目標為取得 Grandpa 的所有子孫，資料如下：
CREATE TABLE FamilyTree
(
  Id INT NOT NULL,
  Name VARCHAR(100) NOT NULL,
  ChildName VARCHAR(100) NULL
);

INSERT FamilyTree VALUES (1, 'Grandpa', 'Dad');
INSERT FamilyTree VALUES (2, 'Grandpa', 'Uncle'); 
INSERT FamilyTree VALUES (3, 'Grandpa', 'Aunt');
INSERT FamilyTree VALUES (4, 'Dad', 'Me');
INSERT FamilyTree VALUES (5, 'Dad', 'Sister'); 
INSERT FamilyTree VALUES (6, 'Uncle', 'Cousin');
INSERT FamilyTree VALUES (7, 'Me', 'Daughter');
INSERT FamilyTree VALUES (8, 'Sister', 'Nephew'); 
INSERT FamilyTree VALUES (9, 'Daughter', 'Grandson');


-- 遞迴的部分必須使用 UNION ALL
WITH ChildrenCTE(Name, ChildName, ChildLevel) AS   
(  
  -- 取得所有資料 (每個人的孩子) 作為第一層
    SELECT Name, ChildName, 1 AS ChildLevel
    FROM FamilyTree
    UNION ALL
  -- 遞迴取得每個人的子孫(不含孩子)
  -- CTE 的查詢結果: 選取孫子(孩子的孩子)
    SELECT FT.Name, Children.ChildName, Children.ChildLevel + 1  
    FROM FamilyTree AS FT
    -- 使用 CTE 查詢: 父母名稱為資料中孩子名稱的資料
        INNER JOIN ChildrenCTE AS Children
        ON FT.ChildName = Children.Name
)  
SELECT *   
FROM ChildrenCTE
WHERE Name = 'Grandpa'
ORDER BY ChildLevel 

-- 利用CTE拆解分隔符號為資料列 ====================================
-- 宣告資料表變數
DECLARE @MENU_CLICK_COUNTER TABLE (
  MENU_ID INT,
  KEYWORD NVARCHAR(100),
  CLICK_COUNT INT
)

-- 塞入測試資料
INSERT INTO @MENU_CLICK_COUNTER (MENU_ID, KEYWORD, CLICK_COUNT)
  VALUES (1, N'福利,補助,購車', 33);
INSERT INTO @MENU_CLICK_COUNTER (MENU_ID, KEYWORD, CLICK_COUNT)
  VALUES (2, N'薪資,福利說明', 99);
INSERT INTO @MENU_CLICK_COUNTER (MENU_ID, KEYWORD, CLICK_COUNT)
  VALUES (3, N'離職,離職訪談', 11);

-- 查看目前資料
SELECT * FROM @MENU_CLICK_COUNTER;

-- 定義拆解字串符號
DECLARE @splitter VARCHAR(10) = ',';
DECLARE @splitterlength INT = LEN(@splitter) + 1;

-- 使用 CTE 搭配遞迴特性拆出關鍵字
WITH Split AS
(
  SELECT MENU_ID,
    1 AS startidx,
    CHARINDEX(@splitter, KEYWORD + @splitter) - 1 AS endidx
  FROM @MENU_CLICK_COUNTER
  WHERE LEN(KEYWORD) > 0

  UNION ALL

  SELECT
    s.MENU_ID,
    s.endidx + @splitterlength,  
    CHARINDEX(@splitter, m.KEYWORD + @splitter, s.endidx + 2) - 1
  FROM Split s -- 使用遞迴滾出每個 menu 被逗號分割的文字起始/結束字元位置
    JOIN @MENU_CLICK_COUNTER m 
      ON s.MENU_ID = m.MENU_ID 
      AND CHARINDEX(@splitter, m.KEYWORD + @splitter, s.endidx + 2) > 0
)
SELECT
  m.MENU_ID,
  SUBSTRING(m.KEYWORD, s.startidx, s.endidx - s.startidx + 1) AS KEYWORD,
  m.CLICK_COUNT
FROM @MENU_CLICK_COUNTER m
JOIN Split s ON m.MENU_ID = s.MENU_ID
ORDER BY m.MENU_ID
 