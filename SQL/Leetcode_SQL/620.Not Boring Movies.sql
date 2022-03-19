------------Problem------------
/*
X city opened a new cinema, many people would like to go to this cinema. The cinema also gives out a poster indicating the movies’ ratings and descriptions.
Please write a SQL query to output movies with an odd numbered ID and a description that is not 'boring'. Order the result by rating.

For example, table cinema:

某城市開了一家新的電影院，吸引了很多人過來看電影。該電影院特別注意用戶體驗，專門有個 LED顯示板做電影推薦，上面公佈著影評和相關電影描述。

作為該電影院的信息部主管，您需要編寫一個 SQL查詢，找出所有影片描述為非 boring (不無聊) 的並且 id 為奇數 的影片，結果請按等級 rating 排列。

例如，下表 cinema:

+---------+-----------+--------------+-----------+
|   id    | movie     |  description |  rating   |
+---------+-----------+--------------+-----------+
|   1     | War       |   great 3D   |   8.9     |
|   2     | Science   |   fiction    |   8.5     |
|   3     | irish     |   boring     |   6.2     |
|   4     | Ice song  |   Fantacy    |   8.6     |
|   5     | House card|   Interesting|   9.1     |
+---------+-----------+--------------+-----------+
For the example above, the output should be:
+---------+-----------+--------------+-----------+
|   id    | movie     |  description |  rating   |
+---------+-----------+--------------+-----------+
|   5     | House card|   Interesting|   9.1     |
|   1     | War       |   great 3D   |   8.9     |
+---------+-----------+--------------+-----------+

*/

------------Answer------------
SELECT *
FROM cinema
WHERE 1 = 1
-- 利用除以2的餘數為1，判斷是否為奇數
AND id%2 = 1 
-- 找出description不等於boring
AND description != 'boring'
-- 按照rating由大到小排序
ORDER BY rating DESC;

-- %餘數用法解析
/*
%是用來傳回某個數值除以另一個數值的餘數

在SQL SERVER中，取餘數是用%(模數)

在ORACLE SQL中，則是用MOD(分字,分母)
*/

-- WHERE 1 = 1用法解析
/*
假設我們需要開發網頁，當使用者輸入一些條件時，我們利用WHERE去篩選資料，但這時有個問題，若是使用者不想篩選資料，那勢必我們在組WHERE篩選條件字串的時候，會只剩WHERE存在，如下：
SELECT *
FROM table_name
WHERE

那這時我們的查詢式就會出現錯誤，所以我們就可以利用WHERE 1 = 1
這個條件必定為真，以邏輯面來講它絲毫不影響結果
而這個方式也被駭客運用來惡意登入網站

例如，某個網站的登入驗證的SQL查詢程式碼為

strSQL = "SELECT * FROM users WHERE (name = '" + userName + "') and (pw = '"+ passWord +"');"

惡意填入
userName = "1' OR '1'='1";

與

passWord = "1' OR '1'='1";

時，將導致原本的SQL字串被填為
strSQL = "SELECT * FROM users WHERE (name = '1' OR '1'='1') and (pw = '1' OR '1'='1');"

也就是實際上執行的SQL命令會變成下面這樣的
strSQL = "SELECT * FROM users;"

因此達到無帳號密碼，亦可登入網站。所以SQL注入被俗稱為駭客的填空遊戲。
*/