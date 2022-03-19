# 利用virtualenv工具建立一個乾淨、虛擬開發環境
# 安裝套件
pip3 install virtualenv

# 在terminal輸入以下指令
virtualenv --python=/opt/python-3.6/bin/python venv
"""
這邊的--python是指定虛擬環境中要使用python的版本，可以使用在安裝多個版本的python
而最後的venv則是虛擬環境的名稱。當執行指令後virtualenv會將所需資料複製到venv這資料夾中
"""

# 當成功建立一個虛擬環境後會在你專案的資料夾內產生一個虛擬環境資料夾，例如用venv產生的就會擁有一個venv的資料夾，然後依照以下方式可以啟動虛擬環境模式：
# Linux / macOS
# 這邊要注意如果剛剛 virtualenv venv 有將 venv 替換成其他名稱，這邊的 venv 要改成新名稱
source ./venv/bin/activate

# Windows
.\venv\Scripts\activate.bat

# 關閉環境 venv 包
deactivate