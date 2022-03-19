# 利用BeautifulSoup解析網頁資料
# BeautifulSoup 是一個 Python 的函式庫模組，可以讓開發者僅須撰寫非常少量的程式碼，就可以快速解析網頁 HTML 碼，從中萃取出使用者有興趣的資料
# 安裝套件語法：pip3 install beautifulsoup4
# 引入 Beautiful Soup 模組
from bs4 import BeautifulSoup

# 原始 HTML 程式碼
html_doc = """
<html><head><title>Hello World</title></head>
<body><h2>Test Header</h2>
<p>This is a test.</p>
<a id="link1" href="/my_link1">Link 1</a>
<a id="link2" href="/my_link2">Link 2</a>
<p>Hello, <b class="boldtext">Bold Text</b></p>
</body></html>
"""

# 以 Beautiful Soup 解析 HTML 程式碼，這裡的 soup 就是解析完成後，所產生的結構樹物件，接下來所有資料的搜尋、萃取等操作都會透過這個物件來進行
soup = BeautifulSoup(html_doc, 'html.parser')

# 輸出排版後的 HTML 程式碼
print(soup.prettify())

# 取得節點文字內容的相關語法 ======================================
# 取得網頁標題 HTML 標籤
title_tag = soup.title
print(title_tag)

# HTML 標籤節點的文字內容，可以透過 string 屬性存取
print(title_tag.string)

# 搜尋節點的相關語法 =============================================
# 取得所有的超連結
a_tags = soup.find_all('a')
for tag in a_tags:
  # 輸出超連結的文字
  print(tag.string)

# 取出節點屬性的相關語法 ==========================================
# 若要取出 HTML 節點的各種屬性，可以使用 get，例如輸出每個超連結的網址（href 屬性）
for tag in a_tags:
  # 輸出超連結網址
  print(tag.get('href'))

# 同時搜尋多種標籤的相關語法 =======================================
# 若要同時搜尋多種 HTML 標籤，可以使用 list 來指定所有的要列出的 HTML 標籤名稱，例如搜尋所有超連結與粗體字
tags = soup.find_all(["a", "b"])
print(tags)

# 限制搜尋節點數量的相關語法 =======================================
# find_all 預設會輸出所有符合條件的節點，但若是遇到節點數量很多的時候，就會需要比較久的計算時間，如果我們不需要所有符合條件的節點，可以用 limit 參數指定搜尋節點數量的上限值，這樣它就只會找出前幾個符合條件的節點
tags = soup.find_all(["a", "b"], limit=2)
print(tags)

# 如果只需要抓出第一個符合條件的節點，可以直接使用 find
a_tag = soup.find("a")
print(a_tag)

# 遞迴搜尋的相關語法 ==============================================
# 預設的狀況下， find_all 會以遞迴的方式尋找所有的子節點
soup.html.find_all("title")

# 如果想要限制 find_all 只找尋次一層的子節點，可以加上 recursive=False 關閉遞迴搜尋功能
soup.html.find_all("title", recursive=False)

# 以 HTML 屬性搜尋的相關語法 =============================================
# 我們也可以根據網頁 HTML 元素的屬性來萃取指定的 HTML 節點，例如搜尋 id 屬性為 link2 的節點
link2_tag = soup.find(id='link2')
print(link2_tag)

# 也可以結合 HTML 節點的名稱與屬性進行更精確的搜尋，例如搜尋 href 屬性為 /my_link1 的 a 節點
a_tag = soup.find_all("a", href="/my_link1")
print(a_tag)

# 搜尋屬性時，也可以使用正規表示法，例如以正規表示法比對超連結網址
import re
links = soup.find_all(href=re.compile("^/my_linkd"))
print(links)

# 也可以同時使用多個屬性的條件進行篩選
link = soup.find_all(href=re.compile("^/my_linkd"), id="link1")
print(link)

# 但在 HTML5 中有一些屬性名稱若直接寫在 Python 的參數中會有一些問題，例如 data-* 這類的屬性直接寫的話，就會產生錯誤訊息，如下
data_soup = BeautifulSoup('<div data-foo="value">foo!</div>', 'html.parser')
# 錯誤的用法：data_soup.find_all(data-foo="value")
# 遇到這種狀況，可以把屬性的名稱與值放進一個 dictionary 中，再將此 dictionary 指定給 attrs 參數即可，如下
data_soup.find_all(attrs={"data-foo": "value"})

# 以 CSS 搜尋的相關語法 =================================================
# 由於 class 是 Python 程式語言的保留字，所以 Beautiful Soup 改以 class_ 這個名稱代表 HTML 節點的 class 屬性，例如搜尋 class 為 boldtext 的 b 節點
b_tag = soup.find_all("b", class_="boldtext")
print(b_tag)

# CSS 的 class 屬性也可以使用正規表示法搜尋，如下
b_tag = soup.find_all(class_=re.compile("^bold"))
print(b_tag)

# 一個 HTML 標籤元素可以同時有多個 CSS 的 class 屬性值，而我們在以 class_ 比對時，只要其中一個 class 符合就算比對成功，例如
css_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser')
# 只要其中一個 class 符合就算比對成功
p_tag = css_soup.find_all("p", class_="strikeout")
print(p_tag)
# 也可以拿完整的 class 字串來進行比對
p_tag = css_soup.find_all("p", class_="body strikeout")
print(p_tag)
# 不過如果多個 class 名稱排列順序不同時，就會失敗
p_tag = css_soup.find_all("p", class_="strikeout body")
print(p_tag)
# 遇到多個 CSS class 的狀況，建議改用 CSS 選擇器來篩選
p_tag = css_soup.select("p.strikeout.body")
print(p_tag)

# 以文字內容搜尋的相關語法 =================================================
# 若要依據文字內容來搜尋特定的節點，可以使用 find_all 配合 string 參數
links_html = """
<a id="link1" href="/my_link1">Link One</a>
<a id="link2" href="/my_link2">Link Two</a>
<a id="link3" href="/my_link3">Link Three</a>
"""
soup = BeautifulSoup(links_html, 'html.parser')
# 搜尋文字為「Link One」的超連結
soup.find_all("a", string="Link One")
# 亦可使用正規表示法批配文字內容，以正規表示法搜尋文字為「Link」開頭的超連結
soup.find_all("a", string=re.compile("^Link"))

# 向上、向前與向後搜尋的相關語法 ============================================
# 前面介紹的 find_all 都是向下搜尋子節點，如果需要向上搜尋父節點的話，可以改用 find_parents 函數（或是 find_parent），它可讓我們以某個特定節點為起始點，向上搜尋父節點
html_doc = """
<body><p class="my_par">
<a id="link1" href="/my_link1">Link 1</a>
<a id="link2" href="/my_link2">Link 2</a>
<a id="link3" href="/my_link3">Link 3</a>
<a id="link3" href="/my_link4">Link 4</a>
</p></body>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
link2_tag = soup.find(id="link2")
# 往上層尋找 p 節點
p_tag = link2_tag.find_parents("p")
print(p_tag)

# 如果想要在在同一層往前尋找特定節點，則可用 find_previous_siblings 函數（或是 find_previous_sibling），例如在同一層往前尋找 a 節點
link_tag = link2_tag.find_previous_siblings("a")
print(link_tag)

# 如果想要在在同一層往後尋找特定節點，則可用 find_next_siblings 函數（或是 find_next_sibling），例如在同一層往後尋找 a 節點
link_tag = link2_tag.find_next_siblings("a")
print(link_tag)

# 解析已下載的網頁檔案語法 =================================================
# 從檔案讀取 HTML 程式碼進行解析
with open("index.html") as f:
    soup = BeautifulSoup(f)

# 利用Beautifulsoup及Requests模組爬取網頁 =================================
import requests
from bs4 import BeautifulSoup

response = requests.get("https://travel.ettoday.net/category/%E6%A1%83%E5%9C%92/")
soup = BeautifulSoup(response.text, "html.parser")
# 輸出排版後的HTML內容
print(soup.prettify())

# 只搜尋第一個符合條件的HTML節點，傳入要搜尋的標籤名稱，如下
result = soup.find("h3")
print(result)
# 搜尋網頁中所有符合條件的HTML節點，傳入要搜尋的HTML標籤名稱。如果要更明確的搜尋，可以利用關鍵字參數(Keyword Argument)指定其屬性值。由於執行結果可能會搜出許多的HTML內容，所以最後也可以利用limit關鍵字參數(Keyword Argument)限制搜尋的節點數量
result = soup.find_all("h3", itemprop="headline", limit=3)
print(result)
# 另外，如果要同時搜尋多個HTML標籤，可以將標籤名稱打包成串列(List)後，傳入find_all()方法(Method)中即可
result = soup.find_all(["h3", "p"], limit=2)
print(result)
# 而如果某一節點下有多個子節點時，則使用select()方法(Method)，選取子節點
result = soup.find("div", itemprop="itemListElement")
print(result.select("a"))

# 要依據HTML的css屬性來進行節點的搜尋，需使用 class_ 關鍵字參數(Keyword Argument)來進行css屬性值的指定
# 搜尋第一個符合指定的HTML標籤及css屬性值的節點
titles = soup.find("p", class_="summary")
print(titles)
# 搜尋網頁中符合指定的HTML標籤及css屬性值的所有節點
titles = soup.find_all("p", class_="summary", limit=3)
print(titles)
# 如果單純只想要透過css屬性值來進行HTML節點的搜尋，則可以使用BeautifulSoup套件(Package)的select()方法(Method)
titles = soup.select(".summary", limit=3)
print(titles)

# 搜尋父節點
# 以上皆為向下的搜尋節點方式，如果想要從某一個節點向上搜尋，則可以使用BeautifulSoup套件(Package)的find_parent()或find_parents()方法(Method)
result = soup.find("a", itemprop="url")
parents = result.find_parents("h3")
print(parents)

# 搜尋前、後節點
# 在同一層級的節點，想要搜尋前一個節點，可以使用BeautifulSoup套件(Package)的find_previous_siblings()方法
result = soup.find("h3", itemprop="headline")
previous_node = result.find_previous_siblings("a")
print(previous_node)

# 取得屬性值
# 在前面範例中，皆為取得所需之HTML節點，而如果想要取得某一個節點中的屬性值，則可以利用BeautifulSoup套件(Package)的get()方法(Method)
# 利用find_all()方法搜尋網頁中所有<h3>標籤且itemprop屬性值為headline的節點，接著，透過for迴圈讀取串列(List)中的節點，由於<h3>標籤底下只有一個<a>標籤，所以可以利用BeautifulSoup套件的select_one()方法進行選取，爬取「ETtoday的旅遊雲」桃園景點首頁的標題連結
titles = soup.find_all("h3", itemprop="headline")
for title in titles:
    print(title.select_one("a").get("href"))

# 如果要取得<a>標籤的連結文字，可以利用BeautifulSoup套件(Package)的getText()方法(Method)
titles = soup.find_all("h3", itemprop="headline")
for title in titles:
    print(title.select_one("a").getText())