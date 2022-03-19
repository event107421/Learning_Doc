-- 複製資料表 ================================
SELECT * INTO new_table_name
FROM old_table_name

-- 修改資料表 ================================
-- 修改表內欄位名稱
ALTER TABLE table_name RENAME COLUMN A TO B

-- 修改表內欄位資料類型
ALTER TABLE talbe_name ALTER COLUMN column_name nVarchar

-- 新增欄位
ALTER TABLE talbe_name ADD new_column_name nVarchar

-- 刪除欄位
ALTER TABLE talbe_name DROP COLUMN column_name

-- 修改欄位默認值
-- 如果欄位已經有默認值，則需要先刪除欄位的約束，再添加新的默認值
ALTER TABLE talbe_name DROP CONSTRAINT 约束名
-- 最後再加入默認值
ALTER TABLE talbe_name ADD DEFAULT (0) FOR column_name WITH VALUES