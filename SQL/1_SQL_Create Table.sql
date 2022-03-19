-- char(n) 和 varchar(n) 的概念分別是 character(n) 和 character varying(n) 的別名
-- 創建表格語法 ====================================
CREATE TABLE fund_data
(
	fund_name VARCHAR(100) NULL,
	fund_ID VARCHAR(100) NOT NULL,
	fund_web VARCHAR(200) NULL,
	fund_area VARCHAR(50) NULL,
	fund_type VARCHAR(50) NULL,
	establishment_date DATETIME NOT NULL,
	PRIMARY KEY (fund_ID, establishment_date)
);


-- 如何限制存入資料的規則?
/*
1. 什麼是Constraint？
Constraint為限制哪一些資料才能儲存至表格中之語法，因此返回的資料必須遵循這個準則。
而這些限制語法可以在表格初創時藉由CREATE TABLE語句來指定一列或多列共用一個限制語法，或是之後藉由ALTER TABLE語句來指定。
*/

/*
2. UNIQUE(唯一值限制)：
保證一個欄位中的所有資料皆是不重複的值。而一個被指定為主鍵的欄位也一定會含有unique的特性，但是一個unique的欄位並不一定會是一個主鍵，需注意！！
*/

-- * 建置新表格時設定「唯一限制」的方式：
CREATE TABLE Employee
(
	EID integer not null UNIQUE,
	Last_Name varchar(30),
	First_Name varchar(30)
);

-- * 建置新表格時替「唯一限制欄位命名與多欄位」的方式：
CREATE TABLE Employee
(
	EID INTEGER NOT NULL,
	Last_Name VARCHAR(30) NOT NULL,
	First_Name VARCHAR(30) NOT NULL,
	Address VARCHAR(30),
	CONSTRAINT stu_Employee_Id UNIQUE (EID, Last_Name, First_Name)
);

-- * 改變現有表格架構來「設定唯一限制」的方式：
ALTER TABLE Employee add UNIQUE (EID);

-- * 改變現有表格架構來「設定唯一限制欄位命名與多欄位」的方式：
ALTER TABLE Employee add CONSTRAINT stu_Employee_Id UNIQUE (EID, Last_Name, First_Name);

-- * 改變現有表格架構來「移除唯一限制」的方式：
ALTER TABLE Employee drop CONSTRAINT stu_Employee_Id;

/*
3. check(檢查限制)：保證一個欄位中的所有資料都是符合某些條件。
*/

-- * 建置新表格時設定「檢查限制」的方式：
CREATE TABLE Employee
(
	EID integer NOT NULL CHECK (EID>0),
	Last_Name varchar(30),
	First_Name varchar(30)
);

-- * 建置新表格時替「檢查限制欄位命名與多欄位」的方式：
CREATE TABLE Employee
(
	EID integer NOT NULL,
	Last_Name varchar(30) NOT NULL,
	First_Name varchar(30) NOT NULL,
	Address varchar(30),
	CONSTRAINT chk_Employee CHECK (EID > 0 AND Last_Name != ‘XXX’)
);

-- * 改變現有表格架構來「設定檢查限制」的方式：
ALTER TABLE Employee add CHECK (EID>0);

-- * 改變現有表格架構來「設定多欄位的檢查限制」的方式：
ALTER TABLE Employee add CONSTRAINT chk_Employee CHECK (EID > 0 AND Last_Name != ‘XXX’);

-- * 改變現有表格架構來「移除檢查限制」的方式：
ALTER TABLE Employee drop CONSTRAINT chk_Employee;

/*
4. primary key(主鍵限制)：Primary Key中的每一筆資料都是表格中的唯一值。
一個資料表中只能有一個primary key，但是可以有多個unique。
主鍵可以包含一或多個欄位，所以當主鍵包含多個欄位時，又稱之為組合鍵 (Composite Key)。
*/

-- * 建置新表格時設定「主鍵」的方式：
CREATE TABLE Employee
(
	EID integer NOT NULL PRIMARY KEY,
	Last_Name varchar(30),
	First_Name varchar(30)
);

-- * 建置新表格時替「主鍵命名與多欄位的組合鍵」的方式：
CREATE TABLE Employee
(
	EID integer NOT NULL,
	Last_Name varchar(30) NOT NULL,
	First_Name varchar(30) NOT NULL,
	Address varchar(30),
	CONSTRAINT stu_Employee_Id PRIMARY KEY (EID, Last_Name, First_Name)
);

-- * 改變現有表格架構來「設定主鍵」的方式：
ALTER TABLE Employee add PRIMARY KEY(EID);

-- * 改變現有表格架構來「設定主鍵限制欄位命名與多欄位」的方式：
ALTER TABLE Employee add CONSTRAINT stu_Employee_Id PRIMARY KEY(EID, Last_Name, First_Name);

-- * 改變現有表格架構來「移除主鍵」的方式：
ALTER TABLE Employee drop CONSTRAINT stu_Employee_Id;

/*
5. FOREIGN KEY(外來鍵限制)：FOREIGN KEY是一個(/數個)指向其他表格中主鍵的欄位。外來鍵的目的是確定資料參考的完整性。
*/

-- * 新表格時設定「外來鍵」的方式：
CREATE TABLE Employee
(
	EID integer NOT NULL unique PRIMARY KEY,
	First_Name varchar(15) NOT NULL,
	Last_Name varchar(15) NOT NULL,
	Address varchar(30),
	Age integer CHECK(Age>0),
	Birth_Date datetime,
	Department_DID integer REFERENCES Department (DID)
	--或 Department_DID integer FOREIGN KEY (Department_DID) REFERENCES Department(DID)
);

-- * 建置新表格時替「外來鍵命名與多欄位的組合鍵」的方式：
CREATE TABLE Employee
(
	EID integer NOT NULL,
	Last_Name varchar(30) NOT NULL,
	First_Name varchar(30) NOT NULL,
	Address varchar(30),
	CONSTRAINT stu_Department_DID FOREIGN KEY (Department_DID) REFERENCES Department(DID)
);

-- * 改變現有表格架構來設定「外來鍵」的方式：
ALTER TABLE Employee add FOREIGN KEY (Department_DID) REFERENCES Department (DID);

-- * 改變現有表格架構來「設定外來鍵限制欄位命名與多欄位」的方式：
ALTER TABLE Employee add CONSTRAINT stu_Department_DID FOREIGN KEY (Department_DID) REFERENCES Department(DID);

-- * 改變現有表格架構來「移除外來鍵」的方式：
ALTER TABLE Employee drop CONSTRAINT stu_Department_DID;

/*
6. DEFAULT(預設限制)：用來設定欄位的預設值，即當在INSERT資料時，若該欄位沒指定值的話，則會採用預設值之內容。
*/

-- * 建置新表格時設定「預設值」的方式：
CREATE TABLE Employee
(
	EID integer NOT NULL PRIMARY KEY,
	Last_Name varchar(30) NOT NULL,
	First_Name varchar(30) NOT NULL,
	Address varchar(30) DEFAULT ‘未知’
);

-- * 改變現有表格架構來「設定預設值」的方式：
ALTER TABLE Employee add CONSTRAINT df_Address DEFAULT ‘未知’ for Address;
-- 或 ALTER TABLE Employee alter column Address set DEFAULT ‘未知’;

-- * 改變現有表格架構來「移除預設值」的方式：
ALTER TABLE Employee drop DEFAULT Address;
-- 或 ALTER TABLE Employee alter column Address drop DEFAULT;

/*
SQL資料型態說明

char與varchar的區別：
char (15)長度固定， 如'www.javazx.com' 存儲需要空間 14個字符
varchar(15) 可變長 如'www.javazx.com' 需要存儲空間 15字符,

例如：
char(10) 如果你存abc，需要空間為10，3個存abc，7個存空字符，因為char是固定長度
varchar(10)如果你存abc，需要空間為4，3個存abc，1個存長度，varchar是可變長度
超過10的部分，都會被截斷
從上面可以看得出來char 長度是固定的，不管你存儲的數據是多少他都會都固定的長度。而varchar則處可變長度但他要在總長度上加1字符，這個用來存儲位置。所以實際應用中用戶可以根據自己的數據類型來做。

由於char 固定長度，所以在處理速度上要比varchar快速很多，但是對費存儲空間，所以對存儲不大，但在速度上有要求的可以使用char類型，反之可以用varchar類型來實例。

而MySQL在資料表中還有分存儲引擎，如下：
myisam 存儲引擎：建議使用固定長度，數據列代替可變長度的數據列。
memory存儲引擎：目前都使用固定數據行存儲，因此無論使用char varchar列都沒關係，
innodb 存儲引擎：建議使用varchar 類型

對於MyISAM表，儘量使用Char，對於那些經常需要修改
而容易形成碎片的myisam和isam數據表就更是如此，它的缺點就是占用磁碟空間
對於InnoDB表，因為它的數據行內部存儲格式對固定長度的數據行和可變長度的數據行不加區分（所有數據行共用一個表頭部分，這個標頭部分存放著指向各有關數據列的指針），所以使用char類型不見得會比使用varchar類型好。事實上，因為char類型通常要比varchar類型占用更多的空間，所以從減少空間占用量和減少磁碟i/o的角度，使用varchar類型反而更有利

所以，char是固定長度的，而varchar會根據具體的長度來使用存儲空間。
比如char(255)和varchar(255)，在存儲字符串"hello world"的時候，char會用一塊255的空間放那個11個字符，而varchar就不會用255個，他先計算長度後只用11個再加上計算的到字符串長度信息，一般1-2個byte來，這樣varchar在存儲不確定長度的時候會大大減少存儲空間。

如此看來varchar比char聰明多了，那char有用武之地嗎？還是很不少優勢的。
一，存儲很短的信息，比如門牌號碼101，201……這樣很短的信息應該用char，因為varchar還要占個byte用於存儲信息長度，本來打算節約存儲的現在得不償失。
二，固定長度的。比如使用uuid作為主鍵，那用char應該更合適。因為他固定長度，varchar動態根據長度的特性就消失了，而且還要占個長度信息。
三，十分頻繁改變的column。因為varchar每次存儲都要有額外的計算，得到長度等工作，如果一個非常頻繁改變的，那就要有很多的精力用於計算，而這些對於char來說是不需要的。

還有一個關於varchar的問題是，varchar他既然可以自動適應存儲空間，那我varchar(8)和varchar(255)存儲應該都是一樣的，那每次表設計的時候往大的方向去好了，免得以後不夠用麻煩。這個思路對嗎？答案是否定的。mysql會把表信息放到內存中（查詢第一次後，就緩存住了，linux下很明顯，但windows下似乎沒有，不知道為啥），這時內存的申請是按照固定長度來的，如果varchar很大就會有問題。所以還是應該按需索取。
*/















