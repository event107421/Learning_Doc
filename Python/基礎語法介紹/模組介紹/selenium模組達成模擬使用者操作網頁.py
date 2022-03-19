from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import wget
import time

# 要先安裝ChromeDriver，到下面網址下載，要注意按照自己電腦的chrome瀏覽器來去下載相應版本
# https://chromedriver.chromium.org/
# 輸入chromeDriver的路徑
PATH = "C:/Users/bill/Downloads/chromedriver.exe"

# 選擇瀏覽器
# 這邊要注意，假設出現類似以下的錯誤訊息 This version of ChromeDriver only supports Chrome version，代表可能瀏覽器的版本與下載的chromeDriver不相符，那就要再重新下載與瀏覽器版本相同的chromeDriver
driver = webdriver.Chrome(PATH)

# 接下來輸入要去的網頁，此時就可以對這個網頁的所有標籤做操作
driver.get("https://ani.gamer.com.tw/")
# 棄用警告：不推薦使用 find_element_by_* 命令。請改用 find_element()，find_element_by_*已被廢棄
search_text = driver.find_element(By.ID, "anime-search-sky")
# 若我們要進行搜尋，最後先把搜尋框清理一下，免得留下上次搜尋的文字或是原本網頁上就有預設文字，這樣會造成搜尋錯誤
search_text.clear()
# 再來就在搜尋的框框內輸入動漫名稱
search_text.send_keys('失格紋的最強賢者')
# 因為這個網頁搜尋點Enter沒用，若是有用的網頁我們可以用下面語法來達成搜尋，RETURN的意思就是按下鍵盤的Enter
# search_text.send_keys(Keys.RETURN)
# 然後找網頁上"搜尋"按鈕，做點擊的動作
search = driver.find_element(By.CLASS_NAME, "anime_search-icon").click()
# 接著點擊搜尋到的結果
link = driver.find_element(By.CLASS_NAME, "theme-list-main").click()

# 避免頁面跳轉標籤還沒跳出來，所以加上等待時間
# 下面語法的意思是driver這個瀏覽器會等待某個固定的標籤出現為止，最多等待我們所設定的20秒
element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, "container"))
)

# 如果要回到上一頁可以用下面語法
driver.back()
# 如果要回到下一頁可以用下面語法
driver.forward()
# 做完事情最後要記得把網頁做關掉的動作
driver.quit()