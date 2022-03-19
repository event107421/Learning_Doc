-- SQL索引(Index)介紹 ===========================================================
/*
索引用來快速地尋找那些具有特定值的記錄
如果沒有索引，執行查詢時必須從第一個記錄開始掃瞄整個表的所有記錄，直至找到符合要求的記錄
所以當表裡面的記錄數量越多，這個操作的代價就越高
如果作為搜尋條件的列上已經建立了索引，就無需掃瞄任何記錄即可迅速得到目標記錄所在的位置

唯一索引(非叢集索引 : UNIQUE INDEX) :
會依單一欄位以順序的方式做排序放在前一個記錄的後面，資料表中的任何索引值都不可以相同.有點像PRIMARY KEY

復合索引(叢集索引 : COMPOSITE INDEX) :
如果是唯一索引又是復合索引則多個欄位組合起來的值，不可以重複而單一欄位則可以重複
*/
-- MySQL提供多種索引類型供選擇：
-- 1.普通索引：這是最基本的索引類型，而且它沒有唯一性之類的限制。
  -- 普通索引可以通過以下幾種方式建立：
    -- 建立索引，例如：
    CREATE INDEX <索引的名字> ON tablename (列的列表);
    -- 修改表，例如：
    ALTER TABLE tablename ADD INDEX [索引的名字] (列的列表);
    -- 建立表的時候指定索引，例如：
    CREATE TABLE tablename ( [...], INDEX [索引的名字] (列的列表) );

-- 2.唯一性索引：這種索引和前面的「普通索引」基本相同，但有一個區別：索引列的所有值都只能出現一次，即必須唯一。
  -- 唯一性索引可以用以下幾種方式建立：
    -- 建立索引，例如：
    CREATE UNIQUE INDEX <索引的名字> ON tablename (列的列表);
    -- 修改表，例如：
    ALTER TABLE tablename ADD UNIQUE [索引的名字] (列的列表);
    -- 建立表的時候指定索引，例如：
    CREATE TABLE tablename ( [...], UNIQUE [索引的名字] (列的列表) );

-- 3.主鍵：主鍵是一種唯一性索引，但它必須指定為「PRIMARY KEY」，每個表只能有一個主鍵。
  -- 如果你曾經用過AUTO_INCREMENT類型的列，你可能已經熟悉主鍵之類的概念了。
  -- 主鍵一般在建立表的時候指定，例如：
  CREATE TABLE tablename ( [...], PRIMARY KEY (列的列表) ); 
  -- 但是，我們也可以通過修改表的方式加入主鍵，例如：
  ALTER TABLE tablename ADD PRIMARY KEY (列的列表); 

/*
4.全文索引：MySQL從3.23.23版開始支持全文索引和全文檢索，其索引類型為FULLTEXT。
  全文索引可以在VARCHAR或者TEXT類型的列上建立，它可以通過CREATE TABLE命令建立，也可以通過ALTER TABLE或CREATE INDEX命令建立。
  對於大規模的資料集，通過ALTER TABLE（或者CREATE INDEX）命令建立全文索引要比把記錄插入帶有全文索引的空表更快。
*/

-- 查看table內的所有索引
SELECT * FROM pg_indexes WHERE tablename = 'test';

-- 建立索引
create index index_name on table_name(columns);
create index index_name on table_name(columns_1, columns_2, ...);

-- 手動刪除索引
DROP INDEX index_name;

-- 顯示單個tableb容量大小
SELECT pg_size_pretty(pg_relation_size('test'));

-- 顯示單個索引大小
SELECT pg_size_pretty(pg_relation_size('test'));

-- 顯示指定表內所有索引大小
SELECT pg_size_pretty(pg_indexes_size('test'));

-- SQL索引及查詢速度優化說明 ====================================================
/*
SQL索引建立原則和使用

SQL索引有兩種，聚集索引和非聚集索引：
 
1.聚集索引存儲記錄是物理上連續存在，而非聚集索引是邏輯上的連續，物理存儲並不連續
 
2.字典的拼音查詢法就是聚集索引，字典的部首查詢就是一個非聚集索引.
 
3.聚集索引和非聚集索引的根本區別是表記錄的排列順序和與索引的排列順序是否一致
 
4.聚集索引一個表只能有一個，而非聚集索引一個表可以存在多個。


建立索引的原則：

1.定義主鍵的數據列一定要建立索引。

2.定義有外鍵的數據列一定要建立索引。

3.對於經常查詢的數據列最好建立索引。

4.對於需要在指定範圍內的快速或頻繁查詢的數據列;

5.經常用在WHERE子句中的數據列。

6.經常出現在關鍵字order by、group by、distinct後面的字段，建立索引。
如果建立的是複合索引，索引的字段順序要和這些關鍵字後面的字段順序一致，否則索引不會被使用。

7.對於那些查詢中很少涉及的列，重複值比較多的列不要建立索引。

8.對於定義為text、image和bit的數據類型的列不要建立索引。

9.對於經常存取的列避免建立索引

10.限製表上的索引數目。對一個存在大量更新操作的表，所建索引的數目一般不要超過3個，最多不要超過5個。
索引雖說提高了訪問速度，但太多索引會影響數據的更新操作。


11.對複合索引，按照字段在查詢條件中出現的頻度建立索引。在復合索引中，記錄首先按照第一個字段排序。
對於在第一個字段上取值相同的記錄，系統再按照第二個字段的取值排序，以此類推。
因此只有復合索引的第一個字段出現在查詢條件中，該索引才可能被使用,因此將應用頻度高的字段，放置在復合索引的前面，會使系統最大可能地使用此索引，發揮索引的作用。


索引的不足之處：
1.雖然索引大大提高了查詢速度，同時卻會降低更新表的速度，如對錶進行INSERT、UPDATE和DELETE。因為更新表時，MySQL不僅要保存數據，還要保存一下索引文件。
 
2.建立索引會佔用磁盤空間的索引文件。一般情況這個問題不太嚴重，但如果你在一個大表上創建了多種組合索引，索引文件的會膨脹很快。

3.索引只是提高效率的一個因素，如果你的MySQL有大數據量的表，就需要花時間研究建立最優秀的索引，或優化查詢語句。


使用索引時，有以下一些技巧和注意事項：
1.索引不會包含有NULL值的列：只要列中包含有NULL值都將不會被包含在索引中，複合索引中只要有一列含有NULL值，那麼這一列對於此復合索引就是無效的。所以我們在數據庫設計時不要讓字段的默認值為NULL。

2.使用短索引：對列進行索引，如果可能應該指定一個前綴長度。例如，如果有一個CHAR(255)的列，如果在前10個或20個字符內，多數值是惟一的，那麼就不要對整個列進行索引。短索引不僅可以提高查詢速度而且可以節省磁盤空間和I/O操作。

3.索引列排序：MySQL查詢只使用一個索引，因此如果where子句中已經使用了索引的話，那麼order by中的列是不會使用索引的。
因此數據庫默認排序可以符合要求的情況下不要使用排序操作；盡量不要包含多個列的排序，如果需要最好給這些列創建複合索引。

4.like語句操作：一般情况下不鼓励使用like操作，如果非使用不可，如何使用也是一个问题。like “%aaa%” 不会使用索引，而like “aaa%”可以使用索引。


5.不要在列上進行運算：
select * from users where YEAR(adddate)<2007;

將在每個行上進行運算，這將導致索引失效而進行全表掃描，因此我們可以改成

select * from users where adddate<‘2007-01-01’;

6.不使用NOT IN和<>操作

7.索引的建立時機：
一般來說，在WHERE和JOIN中出現的列需要建立索引，但也不完全如此，

因為MySQL只對<，<=，=，>，>=，BETWEEN，IN，以及某些時候的LIKE才會使用索引。

因為在以通配符%和_開頭作查詢時，MySQL不會使用索引。
*/


-- SQL查詢速度慢原因及優化方法 =========================================================
/*
SQL查詢速度慢的原因：

1、沒有索引或者沒有問題索引（這是慢最常見的，是程序設計的缺陷）
2、I/O吞小，形成了結局
3、沒有創建計算列導致查詢不優化
4、內存不足
5、網絡速度慢
6、查詢數據量過大（可以採用多種數據查詢方式，其他的減少數據量）
7、鎖或者死鎖（這也是慢速最常見的問題，是程序設計的缺陷）
8、sp_lock、sp_who、活動的用戶查看，原因是讀寫競爭資源
9、返回了過去的行和列
10、查詢語句不好，沒有優化


優化方法：

硬體、Server相關：

1、把數據、日誌、索引放到不同的I/O設備上，增加讀取速度，以前可以將Tempdb應放在RAID0上，SQL2000不在支持。數據量（尺寸）越大，提高I/O越重要.

2、縱向、橫向分割表，減少表的尺寸(sp_spaceuse)

3、升級硬體

4、提高網速

5、擴大服務器的內存。配置虛擬內存：虛擬內存大小應基於計算機上並發運行的服務進行配置。可考慮：將虛擬內存大小配置為至少是計算機中安裝的物理內存的 3 倍。將 SQL Server max server memory 服務器配置選項配置為物理內存的 1.5 倍（虛擬內存大小設置的一半）。

6、增加服務器CPU個數，但是必須明白並行處理串行處理更需要資源例如內存。單個任務分解成多個任務，就可以在處理器上運行。例如耽擱查詢的排序、連接、掃描和GROUP BY字句同時執行。但是更新操作UPDATE、INSERT、DELETE還不能並行處理。

7、DB Server 和APPLication Server 分離；OLTP和OLAP分離

8、分佈式分區視圖可用於實現數據庫服務器聯合體。聯合體是一組分開管理的服務器，但它們相互協作分擔系統的處理負荷。這種通過分區數據形成數據庫服務器聯合體的機制能夠擴大一組服務器，以支持大型的多層 Web 站點的處理需要。
  a、在實現分區視圖之前，必須先水平分區表
  b、在創建成員表後，在每個成員服務器上定義一個分佈式分區視圖，並且每個視圖具有相同的名稱。這樣，引用分佈式分區視圖名的查詢可以在任何一個成員服務器上運行
  系統操作如同每個成員服務器上都有一個原始表的複本一樣，但其實每個服務器上只有一個成員表和一個分佈式分區視圖。數據的位置對應用程序是透明的。

9、當服務器的內存夠多時，配製線程數量 = 最大連接數+5，這樣能發揮最大的效率；否則使用 配製線程數量 <最大連接數啟用SQL SERVER的線程池來解決,如果還是數量 = 最大連接數+5，嚴重的損害服務器的性能。

10、通過SQL Server Performance Monitor監視相應硬件的負載 Memory: Page Faults / sec計數器如果該值偶爾走高，表明當時有線程競爭內存。如果持續很高，則內存可能是瓶頸。

11、% DPC Time 指在範例間隔期間處理器用在緩延程序調用(DPC)接收和提供服務的百分比。 (DPC 正在運行的為比標準間隔優先權低的間隔)。由於 DPC 是以特權模式執行的，DPC 時間的百分比為特權時間 百分比的一部分。這些時間單獨計算並且不屬於間隔計算總數的一部 分。這個總數顯示了作為實例時間百分比的平均忙時。

12、%Processor Time計數器　如果該參數值持續超過95%，表明瓶頸是CPU。可以考慮增加一個處理器或換一個更快的處理器。

13、% Privileged Time 指非閒置處理器時間用於特權模式的百分比。 (特權模式是為操作系統組件和操縱硬件驅動程序而設計的一種處理模式。它允許直接訪問硬件和所有內存。另一種模式為用戶模式，它是一種為應用程序、環境分系統和整數分系統設計的一種有限處理模式。操作系統將應用程序線程轉換成特權模式以訪問操作系統服務)。特權時間的 % 包括為間斷和 DPC 提供服務的時間。特權時間比率高可能是由於失敗設備產生的大數量的間隔而引起的。這個計數器將平均忙時作為樣本時間的一部分顯示。

14、% User Time表示耗費CPU的數據庫操作，如排序，執行aggregate functions等。如果該值很高，可考慮增加索引，盡量使用簡單的表聯接，水平分割大表格等方法來降低該值。 Physical Disk: Curretn Disk Queue Length計數器該值應不超過磁盤數的1.5~2倍。要提高性能，可增加磁盤。 SQLServer:Cache Hit Ratio計數器該值越高越好。如果持續低於80%，應考慮增加內存。注意該參數值是從SQL Server啟動後，就一直累加記數，所以運行經過一段時間後，該值將不能反映系統當前值。


查詢語法相關：

1、根據查詢條件,建立索引,優化索引、優化訪問方式，限制結果集的數據量。注意填充因子要適當（最好是使用默認值0）。索引應該盡量小，使用字節數小的列建索引好（參照索引的創建），不要對有限的幾個值的字段建單一索引如性別字段。在必要是對全局或者局部臨時表創建索引，有時能夠提高速度，但不是一定會這樣，因為索引也耗費大量的資源。

2、如果是使用like進行查詢的話，簡單的使用index是不行的，但是全文索引，耗空間。 like ‘a%’ 使用索引 like ‘%a’ 不使用索引用 like ‘%a%’ 查詢時，查詢耗時和字段值總長度成正比，所以不能用CHAR類型，而是VARCHAR。對於字段的值很長的建全文索引。

3、重建索引 DBCC REINDEX、DBCC INDEXDEFRAG、收縮數據和日誌 DBCC SHRINKDB,DBCC SHRINKFILE。設置自動收縮日誌，對於大的數據庫不要設置數據庫自動增長，它會降低服務器的性能。在T-sql的寫法上有很大的講究，下面列出常見的要點：首先，DBMS處理查詢計劃的過程是這樣的：
  1、 查詢語句的詞法、語法檢查
  2、 將語句提交給DBMS的查詢優化器
  3、 優化器做代數優化和存取路徑的優化
  4、 由預編譯模塊生成查詢規劃
  5、 然後在合適的時間提交給系統處理執行
  6、 最後將執行結果返回給用戶其次，看一下SQL SERVER的數據存放的結構：一個頁面的大小為8K(8060)字節，8個頁面為一個盤區，按照B樹存放。

4、Commit和rollback的區別 Rollback:回滾所有的事物。 Commit:提交當前的事物. 沒有必要在動態SQL裡寫事物，如果要寫請寫在外面如： begin tran exec(@s) commit trans 或者將動態SQL 寫成函數或者存儲過程。

5、在查詢Select語句中用Where字句限制返回的行數,避免表掃描,如果返回不必要的數據，浪費了服務器的I/O資源，加重了網絡的負擔降低性能。如果表很大，在表掃描的期間將表鎖住，禁止其他的聯接訪問表,後果嚴重。

6、盡可能不使用光標，它佔用大量的資源。如果需要row-by-row地執行，盡量採用非光標技術，如：在客戶端循環，用臨時表，Table變量，用子查詢，用Case語句等等。游標可以按照它所支持的提取選項進行分類： 只進 必須按照從第一行到最後一行的順序提取行。 FETCH NEXT 是唯一允許的提取操作，也是默認方式。可滾動性可以在游標中任何地方隨機提取任意行。

7、用Profiler來跟踪查詢，得到查詢所需的時間，找出SQL的問題所在，用索引優化器優化索引

8、注意UNION和UNION ALL 的區別。 UNION ALL好

9、注意使用DISTINCT、ORDER BY，在沒有必要時不要用，它同UNION一樣會使查詢變慢。重複的記錄在查詢裡是沒有問題的

10、查詢時不要返回不需要的行、列

11、用sp_configure ‘query governor cost limit’ 或者SET QUERY_GOVERNOR_COST_LIMIT來限制查詢消耗的資源。當評估查詢消耗的資源超出限制時，服務器自動取消查詢,在查詢之前就扼殺掉。 SET LOCKTIME設置鎖的時間

12、用select top 100 / 10 Percent 來限制用戶返回的行數或者SET ROWCOUNT來限制操作的行

13、在SQL2000以前，一般不要用如下的字句: “IS NULL”, ” <> “, “!=”, “!> “, “! <“, “NOT”, “NOT EXISTS”, “NOT IN”, “NOT LIKE”, and “LIKE ‘%500′”，因為他們不走索引全是表掃描。也不要在WHere字句中的列名加函數，如Convert，substring等,如果必須用函數的時候，創建計算列再創建索引來替代.還可以變通寫法：WHERE SUBSTRING(firstname,1,1) = ‘m’改為WHERE firstname like ‘m%’（索引掃描），一定要將函數和列名分開。並且索引不能建得太多和太大。 NOT IN會多次掃描表，使用EXISTS、NOT EXISTS ，IN , LEFT OUTER JOIN 來替代，特別是左連接,而Exists比IN更快，最慢的是NOT操作.如果列的值含有空，以前它的索引不起作用，現在2000的優化器能夠處理了。相同的是IS NULL，“NOT”, “NOT EXISTS”, “NOT IN”能優化她，而” <> ”等還是不能優化，用不到索引。

14、使用Query Analyzer，查看SQL語句的查詢計劃和評估分析是否是優化的SQL。一般的20%的代碼佔據了80%的資源，我們優化的重點是這些慢的地方。

15、如果使用了IN或者OR等時發現查詢沒有走索引，使用顯示申明指定索引： SELECT * FROM PersonMember (INDEX = IX_Title) WHERE processid IN (‘男’，‘女’)

16、將需要查詢的結果預先計算好放在表中，查詢的時候再SELECT。

17、MIN() 和 MAX()能使用到合適的索引

18、數據庫有一個原則是代碼離數據越近越好，所以優先選擇Default，依次為Rules、Triggers、Constraint（約束如外健主健CheckUNIQUE……，數據類型的最大長度等等都是約束），Procedure這樣不僅維護工作小，編寫程序質量高，並且執行的速度快。

19、Between在某些時候比IN速度更快，Between能夠更快地根據索引找到範圍。用查詢優化器可見到差別。 select * from chineseresume where title in (‘男’,’女’) Select * from chineseresume where between ‘男’ and ‘女’ 是一樣的。由於in會在比較多次，所以有時會慢些。

20、用OR的字句可以分解成多個查詢，並且通過UNION 連接多個查詢。他們的速度只同是否使用索引有關，如果查詢需要用到聯合索引，用UNION all執行的效率更高.多個OR的字句沒有用到索引，改寫成UNION的形式再試圖與索引匹配。一個關鍵的問題是否用到索引。

21、盡量少用視圖，它的效率低。對視圖操作比直接對錶操作慢，可以用stored procedure來代替她。特別的是不要用視圖嵌套，嵌套視圖增加了尋找原始資料的難度。我們看視圖的本質：它是存放在服務器上的被優化好了的已經產生了查詢規劃的SQL。對單個表檢索數據時，不要使用指向多個表的視圖，直接從表檢索或者僅僅包含這個表的視圖上讀，否則增加了不必要的開銷，查詢受到干擾，為了加快視圖的查詢，MSSQL增加了視圖索引的功能。

22、在IN後面值的列表中，將出現最頻繁的值放在最前面，出現得最少的放在最後面，減少判斷的次數

23、當用SELECT INTO時，它會鎖住系統表(sysobjects，sysindexes等等)，阻塞其他的連接的存取。創建臨時表時用顯示申明語句，而不是 select INTO. drop table t_lxh begin tran select * into t_lxh from chineseresume where name = ‘XYZ’ –commit 在另一個連接中SELECT * from sysobjects可以看到 SELECT INTO 會鎖住系統表，Create table 也會鎖系統表(不管是臨時表還是系統表)。所以千萬不要在事物內使用它！ ！ ！這樣的話如果是經常要用的臨時表請使用實表，或者臨時表變量。

24、一般在GROUP BY 個HAVING字句之前就能剔除多餘的行，所以盡量不要用它們來做剔除行的工作。他們的執行順序應該如下最優：select 的Where字句選擇所有合適的行，Group By用來分組個統計行，Having字句用來剔除多餘的分組。這樣Group By 個Having的開銷小，查詢快.對於大的數據行進行分組和Having十分消耗資源。如果Group BY的目的不包括計算，只是分組，那麼用Distinct更快

25、一次更新多條記錄比分多次更新每次一條快，就是說批處理好

26、少用臨時表，盡量用結果集和Table類性的變量來代替它，Table 類型的變量比臨時表好

27、不要在一句話裡再三的使用相同的函數，浪費資源,將結果放在變量裡再調用更快

28、SELECT COUNT(*)的效率較低，盡量變通他的寫法，而EXISTS快.同時請注意區別： select count(Field of null) from Table 和 select count(Field of NOT null) from Table 的返回值是不同的。

29、按照一定的次序來訪問你的表。如果你先鎖住表A，再鎖住表B，那麼在所有的存儲過程中都要按照這個順序來鎖定它們。如果你（不經意的）某個存儲過程中先鎖定表B，再鎖定表A，這可能就會導致一個死鎖。如果鎖定順序沒有被預先詳細的設計好，死鎖很難被發現

30、分析select emp_name form employee where salary > 3000 在此語句中若salary是Float類型的，則優化器對其進行優化為Convert(float,3000)，因為3000是個整數，我們應在編程時使用3000.0而不要等運行時讓DBMS進行轉化。同樣字符和整型數據的轉換。

31、查詢的關聯同寫的順序：
select a.personMemberID, * from chineseresume a,personmember b where personMemberID= b.referenceid and a.personMemberID = ‘JCNPRH39681’ （A = B ,B = ‘號碼’）

select a.personMemberID, * from chineseresume a,personmember b where a.personMemberID= b.referenceid and a.personMemberID = ‘JCNPRH39681’ and b.referenceid = ‘JCNPRH39681’ （A = B ,B = ‘號碼’， A = ‘號碼’）

select a.personMemberID, * from chineseresume a,personmember b where b.referenceid= ‘JCNPRH39681’ and a.personMemberID = ‘JCNPRH39681’ （B = ‘號碼’， A = ‘號碼’）

(1)IF 沒有輸入負責人代碼 THEN code1=0 code2=9999 ELSE code1=code2=負責人代碼 END IF 執行SQL語句為: SELECT 負責人名 FROM P2000 WHERE 負責人代碼>=:code1 AND負責人代碼 <=:code2

(2)IF 沒有輸入負責人代碼 THEN SELECT 負責人名 FROM P2000 ELSE code= 負責人代碼 SELECT 負責人代碼 FROM P2000 WHERE 負責人代碼=:code END IF 第一種方法只用了一條SQL語句,第二種方法用了兩條SQL語句。在沒有輸入負責人代碼時,第二種方法顯然比第一種方法執行效率高,因為它沒有限制條件;在輸入了負責人代碼時,第二種方法仍然比第一種方法效率高,不僅是少了一個限制條件,還因相等運算是最快的查詢運算。我們寫程序不要怕麻煩

32、關於JOBCN現在查詢分頁的新方法（如下），用性能優化器分析性能的瓶頸，如果在I/O或者網絡的速度上，如下的方法優化切實有效，如果在CPU或者內存上，用現在的方法更好。請區分如下的方法，說明索引越小越好：
begin
DECLARE @local_variable table (FID int identity(1,1),ReferenceID varchar(20))
insert into @local_variable (ReferenceID)
select top 100000 ReferenceID from chineseresume order by ReferenceID
select * from @local_variable where Fid > 40 and fid <= 60
end

begin
DECLARE @local_variable table (FID int identity(1,1),ReferenceID varchar(20))
insert into @local_variable (ReferenceID)
select top 100000 ReferenceID from chineseresume order by updatedate
select * from @local_variable where Fid > 40 and fid <= 60
end

begin
create table #temp (FID int identity(1,1),ReferenceID varchar(20))
insert into #temp (ReferenceID)
select top 100000 ReferenceID from chineseresume order by updatedate
select * from #temp where Fid > 40 and fid <= 60 drop table #temp
end

(A)SQL的使用規範：
i.　盡量避免大事務操作，慎用holdlock子句，提高系統並發能力。

ii.　盡量避免反复訪問同一張或幾張表，尤其是數據量較大的表，可以考慮先根據條件提取數據到臨時表中，然後再做連接。

iii.　盡量避免使用游標，因為游標的效率較差，如果游標操作的數據超過1萬行，那麼就應該改寫；如果使用了游標，就要盡量避免在游標循環中再進行表連接的操作。

iv.　注意where字句寫法，必須考慮語句順序，應該根據索引順序、範圍大小來確定條件子句的前後順序，盡可能的讓字段順序與索引順序相一致，範圍從大到小。

v.　不要在where子句中的“=”左邊進行函數、算術運算或其他表達式運算，否則係統將可能無法正確使用索引。

vi.　盡量使用exists代替selectcount(1)來判斷是否存在記錄，count函數只有在統計表中所有行數時使用，而且count(1)比count(*)更有效率。

vii.　盡量使用“>=”，不要使用“>”。

viii.　注意一些or子句和union子句之間的替換

ix.　注意表之間連接的數據類型，避免不同類型數據之間的連接。

x.　注意存儲過程中參數和數據類型的關係。

xi.　注意insert、update操作的數據量，防止與其他應用衝突。如果數據量超過200個數據頁面（400k），那麼系統將會進行鎖升級，頁級鎖會升級成表級鎖。


(B)索引的使用規範：
i.　索引的創建要與應用結合考慮，建議大的OLTP表不要超過6個索引。

ii.　盡可能的使用索引字段作為查詢條件，尤其是聚簇索引，必要時可以通過indexindex_name來強制指定索引

iii.　避免對大表查詢時進行tablescan，必要時考慮新建索引。

iv.　在使用索引字段作為條件時，如果該索引是聯合索引，那麼必須使用到該索引中的第一個字段作為條件時才能保證系統使用該索引，否則該索引將不會被使用。

v.　要注意索引的維護，週期性重建索引，重新編譯存儲過程。


(C)操作符優化：
i.IN 操作符

用IN寫出來的SQL的優點是比較容易寫及清晰易懂，這比較適合現代軟件開發的風格。但是用IN的SQL性能總是比較低的，從Oracle執行的步驟來分析用IN的SQL與不用IN的SQL有以下區別：
ORACLE試圖將其轉換成多個表的連接，如果轉換不成功則先執行IN裡面的子查詢，再查詢外層的表記錄，如果轉換成功則直接採用多個表的連接方式查詢。由此可見用IN的SQL至少多了一個轉換的過程。一般的SQL都可以轉換成功，但對於含有分組統計等方面的SQL就不能轉換了。

推薦方案：在業務密集的SQL當中盡量不採用IN操作符，用EXISTS 方案代替。

ii.NOT IN操作符

此操作是強列不推薦使用的，因為它不能應用表的索引。
推薦方案：用NOT EXISTS 方案代替

iii.IS NULL 或IS NOT NULL操作（判斷字段是否為空）
判斷字段是否為空一般是不會應用索引的，因為索引是不索引空值的。

推薦方案：用其它相同功能的操作運算代替，如：a is not null 改為 a>0 或a>’’等。不允許字段為空，而用一個缺省值代替空值，如申請中狀態字段不允許為空，缺省為申請。

iv.> 及 < 操作符（大於或小於操作符）

大於或小於操作符一般情況下是不用調整的，因為它有索引就會採用索引查找，但有的情況下可以對它進行優化，如一個表有100萬記錄，一個數值型字段A，30萬記錄的A=0，30萬記錄的A=1，39萬記錄的A=2，1萬記錄的A=3。那麼執行A>2與A>=3的效果就有很大的區別了，因為A>2時ORACLE會先找出為2的記錄索引再進行比較，而A>=3時ORACLE則直接找到=3的記錄索引。

v.LIKE操作符

LIKE操作符可以應用通配符查詢，裡面的通配符組合可能達到幾乎是任意的查詢，但是如果用得不好則會產生性能上的問題，如LIKE ‘%5400%’ 這種查詢不會引用索引，而LIKE ‘X5400%’則會引用範圍索引。

一個實際例子：用YW_YHJBQK表中營業編號後面的戶標識號可來查詢營業編號 YY_BH LIKE ‘%5400%’ 這個條件會產生全表掃描，如果改成YY_BH LIKE ’X5400%’ OR YY_BH LIKE ’B5400%’ 則會利用YY_BH的索引進行兩個範圍的查詢，性能肯定大大提高。

vi.UNION操作符
UNION在進行錶鍊接後會篩選掉重複的記錄，所以在錶鍊接後會對所產生的結果集進行排序運算，刪除重複的記錄再返回結果。實際大部分應用中是不會產生重複的記錄，最常見的是過程表與歷史表UNION。如：
select * from ***fys
union
select * from ls_jg_dfys

這個SQL在運行時先取出兩個表的結果，再用排序空間進行排序刪除重複的記錄，最後返回結果集，如果表數據量大的話可能會導致用磁盤進行排序。

推薦方案：採用UNION ALL操作符替代UNION，因為UNION ALL操作只是簡單的將兩個結果合併後就返回。
select * from ***fys
union all
select * from ls_jg_dfys
*/