-- 製造日期的相關語法
/* 在做資料分析時我們常常都會需要進行日期的條件篩選，以下就把較常使用的日期整理出來 */

SELECT
DATEADD(yy, DATEDIFF(yy, 0,  GETDATE()), 0) AS YearFDt  -- 當年度第1天
,DATEADD(mm, DATEDIFF(mm, '', GETDATE())-2, '') AS Pre2FDt   -- 前2個月第1天
,DATEADD(DAY, -1, DATEADD(mm, DATEDIFF(mm, '', GETDATE())-1, '')) AS Pre2EDt    -- 前2個月最後1天
,DATEADD(mm, -1, DATEADD(mm, DATEDIFF(mm, '', GETDATE()), '')) AS Pre1FDt    -- 前1個月第1天
,DATEADD(DAY, -1, DATEADD(mm, DATEDIFF(mm, '', GETDATE()), '')) AS Pre1EDt   -- 前1個月最後1天
,DATEADD(mm, DATEDIFF(mm, '', GETDATE()), '') AS CurrFDt   -- 當月第1天
,DATEADD(DAY, -1, DATEADD(mm, DATEDIFF(mm, '', GETDATE())+1, '')) AS CurrEdt   -- 當月最後1天
,DATEADD(mm, DATEDIFF(mm, '', GETDATE())+1, '') AS LAStFDt -- 後1個月第1天
,DATEADD(DAY, -1, DATEADD(mm, DATEDIFF(mm, '', GETDATE())+2, '')) AS LAStEDt -- 後1個月最後1天
,DATEADD(yy, DATEDIFF(yy, 0,  GETDATE())+1, -1) AS YearEDt -- 當年度最後1天
--//每週起始第一天是星期天
,GETDATE()-DATEPART(dw, GETDATE()-7)+1 AS currwkSun1
,GETDATE()-DATEPART(dw, GETDATE()-7)+7 AS CurrwkSay
--//每週起始第一天是星期一
,GETDATE()-DATEPART(dw, GETDATE())+2 AS currwkMon
,GETDATE()-DATEPART(dw, GETDATE())+8 AS CurrwkSun
--//上一週起始第一天是星期天
,GETDATE()-7-DATEPART(dw, GETDATE()-7)+1 AS lASwkSun1
,GETDATE()-7-DATEPART(dw, GETDATE()-7)+7 AS lASwkSay
--//上一週起始第一天是星期一
,GETDATE()-7-DATEPART(dw, GETDATE()-7)+2 AS lASwkMon
,GETDATE()-7-DATEPART(dw, GETDATE()-7)+8 AS lASwkSun

/*
-- DATEADD函數介紹 =================
DATEADD是計算某日期加上一個數值，傳回的日期

DATEADD (datepart , number , date )

datepart：為間隔的單位，例如：DAY、MONTH、YEAR
number：是指定要加的數值
date：是要被加上的原始日期

例如：SELECT DATEADD(MONTH, 2, '2010-10-06')
結果為2010-12-06 00:00:00.000，也就是加了2個月後的日期

-- DATEDIFF函數介紹 =================
DATEDIFF是算兩個日期間的間隔，傳回帶正負號的整數

DATEDIFF ( datepart , startdate , enddate )

datepart：為間隔的單位，例如：DAY、MONTH、YEAR
startdate：計算間隔時間的起始日期
enddate：計算間隔時間的結束日期

例如：SELECT DATEDIFF(DAY, '2010-10-03', '2010-10-04')
結果為1，那就是代表兩個日期差一天

-- GETDATE函數介紹 =================
在撰寫資訊系統的時間記錄或LOG檔時，常會用到 getdate() 這個函式來取得系統時間
單純執行 SELECT GETDATE()會得到一個日期訊息，詳細了記錄了年-月-日 時:分:秒.毫秒。

例如：單純執行SELECT GETDATE()
結果為2019-10-27 15:17:57.623

-- DATEPART函數介紹 =================
DATEPART() 函數用於返回日期/時間的單獨部分，例如年、月、日、小時、分鐘等等
DATEPART(datepart, date)

datepart：指定要函數返回日期的哪個單獨部分
date：給函數做為返回基準的日期

SELECT GETDATE()
, DATEPART(YEAR, GETDATE()) AS '年'
, DATEPART(MONTH, GETDATE()) AS '月'
, DATEPART(DAY, GETDATE()) AS '日'
, DATEPART(DAYOFYEAR, GETDATE()) AS '本年一月一號至今的天數'
, DATEPART(WEEK , GETDATE()) AS '第N週'
, DATEPART(WEEKDAY , GETDATE()) AS '星期幾(代號)' 
			--星期日 = 1
            --星期一 = 2
            --星期二 = 3
            --星期三 = 4
            --星期四 = 5
            --星期五 = 6
            --星期六 = 7
, DATENAME(WEEKDAY, GETDATE()) AS '星期幾'
, DATEPART(HOUR, GETDATE()) AS '時'
, DATEPART(MINUTE, GETDATE()) AS '分'
, DATEPART(SECOND, GETDATE()) AS '秒'
, DATEPART(MILLISECOND, GETDATE()) AS '毫秒'
*/

-- 日期格式轉換
SELECT CONVERT(VARCHAR, GETDATE(), 100) -- mon dd yyyy hh:mmAM (or PM)，Oct  2 2008 11:01AM          
SELECT CONVERT(VARCHAR, GETDATE(), 101) -- mm/dd/yyyy，10/02/2008                  
SELECT CONVERT(VARCHAR, GETDATE(), 102) -- yyyy.mm.dd，2008.10.02           
SELECT CONVERT(VARCHAR, GETDATE(), 103) -- dd/mm/yyyy
SELECT CONVERT(VARCHAR, GETDATE(), 104) -- dd.mm.yyyy
SELECT CONVERT(VARCHAR, GETDATE(), 105) -- dd-mm-yyyy
SELECT CONVERT(VARCHAR, GETDATE(), 106) -- dd mon yyyy
SELECT CONVERT(VARCHAR, GETDATE(), 107) -- mon dd, yyyy
SELECT CONVERT(VARCHAR, GETDATE(), 108) -- hh:mm:ss
SELECT CONVERT(VARCHAR, GETDATE(), 109) -- mon dd yyyy hh:mm:ss:mmmAM (or PM)，Oct  2 2008 11:02:44:013AM   
SELECT CONVERT(VARCHAR, GETDATE(), 110) -- mm-dd-yyyy
SELECT CONVERT(VARCHAR, GETDATE(), 111) -- yyyy/mm/dd
SELECT CONVERT(VARCHAR, GETDATE(), 112) -- yyyymmdd
SELECT CONVERT(VARCHAR, GETDATE(), 113) -- dd mon yyyy hh:mm:ss:mmm，02 Oct 2008 11:02:07:577     
SELECT CONVERT(VARCHAR, GETDATE(), 114) -- hh:mm:ss:mmm(24h)
SELECT CONVERT(VARCHAR, GETDATE(), 120) -- yyyy-mm-dd hh:mm:ss(24h)
SELECT CONVERT(VARCHAR, GETDATE(), 121) -- yyyy-mm-dd hh:mm:ss.mmm
SELECT CONVERT(VARCHAR, GETDATE(), 126) -- yyyy-mm-ddThh:mm:ss.mmm，2008-10-02T10:52:47.513
-- SQL create different date styles with t-sql string functions
SELECT REPLACE(CONVERT(VARCHAR, GETDATE(), 111), -/-, - -) -- yyyy mm dd
SELECT CONVERT(VARCHAR(7), GETDATE(), 126)                 -- yyyy-mm
SELECT RIGHT(CONVERT(VARCHAR, GETDATE(), 106), 8)          -- mon yyyy