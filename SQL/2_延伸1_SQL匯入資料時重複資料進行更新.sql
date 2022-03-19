USE data_name

CREATE TABLE aa (a INT, b CHAR(1), c INT, data_date DATE) 

CREATE TABLE bb (a INT, b CHAR(1), c INT, data_date DATE) 

INSERT aa VALUES (1,'A',10,'2019-10-31') 
INSERT aa VALUES (2,'B',20,'2019-10-31') 
INSERT aa VALUES (3,'C',30,'2019-10-31')

INSERT bb VALUES (1,'A',10,'2019-11-01') 
INSERT bb VALUES (4,'D',20,'2019-11-01') 
INSERT bb VALUES (5,'E',30,'2019-11-01')

-- 查詢匯入的資料
SELECT *
FROM aa

-- 查詢匯入的資料
SELECT *
FROM bb

-- 如果只是單純的要判斷重複資料不要匯入目的資料表，可以用not in指令就可以達成
INSERT aa 
SELECT * FROM bb WHERE a not in (SELECT a FROM aa)

-- 那如果是碰到重複的主鍵要直接將其更新就可以利用merge函數
MERGE aa  AS Target 
USING (SELECT * FROM bb) AS Source 
ON (Target.a = Source.a AND Target.b = Source.b) 
WHEN MATCHED THEN 
    UPDATE SET Target.data_date = Source.data_date 
WHEN NOT MATCHED BY TARGET THEN 
    INSERT (a, b, c, data_date)
    VALUES (Source.a, Source.b, Source.c, Source.data_date);

-- 查詢執行結果
SELECT *
FROM aa