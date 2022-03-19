"""
Web API 是讓團隊其他成員與使用者分享資料的其中一種方式，並不是唯一方式、也不一定是最佳方式。
如果我們所提供出來的資料較小且不會頻繁隨時間而更動，提供靜態的 JSON、XML 或 CSV 等常見文字格式資料集可能是更好的選擇
然而當資料具備下列特性時，使用 Web API 分享就顯得比使用文字格式資料集提供下載來得更好：
1.資料更新的速度快、頻率高，生成靜態資料集檔案過於緩慢
2.使用者可能只需要龐大資料中的一個子集（subset）
3.資料具備重複運算的特性（例如 rolling stats）
"""

# 先搭建一個簡單的api，如下程式碼：
import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello Flask!</h1>"

app.run()

# 將上面程式碼存成api.py，之後回到命令列，輸入 python api.py 啟動 Web 應用程式，並依照畫面提示打開瀏覽器前往 http://127.0.0.1:5000/


import flask
from flask import jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True
# 如果資料內有中文，會發現中文的資料以 ASCII 編碼的外觀顯示，預設為TRUE，所以需將其改為FALSE，也就是不以ASCII 編碼的外觀顯示
app.config["JSON_AS_ASCII"] = False

# test data
tpe = {
    "id": 0,
    "city_name": "台北",
    "country_name": "台灣",
    "is_capital": True,
    "location": {
        "longitude": 121.569649,
        "latitude": 25.036786
    }
}
nyc = {
    "id": 1,
    "city_name": "紐約",
    "country_name": "美國",
    "is_capital": False,
    "location": {
        "longitude": -74.004364,
        "latitude": 40.710405
    }
}
ldn = {
    "id": 2,
    "city_name": "倫敦",
    "country_name": "英國",
    "is_capital": True,
    "location": {
        "longitude": -0.114089,
        "latitude": 51.507497
    }
}
cities = [tpe, nyc, ldn]

"""
我們試著用 pandas 套件讀入 gapminder.csv 並將它加入 Web API 中
由於 pandas 讀入 .csv 檔案會以資料框結構儲存，傳送給 jsonify() 函數的資料應該要如同手動建立以 list of dictionaries 的形式才是正確輸入格式
於是以迴圈將資料框的每一筆觀測值的變數名稱與資料值分別對應成 dict 的 Key 與 Value 再存入 list 中，最後傳入 jsonify() 函數作為輸入
"""
# 若是輸出pandas dataframe格式資料時，啟動 Web 應用程式後出現 TypeError: Object of type int64 is not JSON serializable
# 這是因為在將觀測值由資料框取出來的時候是 pd.Series 的資料結構，裡頭的整數資料型態並不是 Python 的 int 而是 NumPy 中的 numpy.int64
# 同理浮點數資料型態也不是 float 而是 numpy.float64，因此加入考慮資料型態的轉換來解決
gapminder = pd.read_csv("gapminder.csv")
gapminder_list = []
nrows = gapminder.shape[0]
for i in range(nrows):
    ser = gapminder.loc[i, :]
    row_dict = {}
    for idx, val in zip(ser.index, ser.values):
        if type(val) is str:
            row_dict[idx] = val
        elif type(val) is np.int64:
            row_dict[idx] = int(val)
        elif type(val) is np.float64:
            row_dict[idx] = float(val)
    gapminder_list.append(row_dict)

@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello Flask!</h1>"

# 直接輸出所有cities資料
@app.route('/cities/all', methods=['GET'])
def cities_all():
    return jsonify(cities)

# 另外也可以給使用者指定想要的資料，可以用以下程式碼：
# 使用者就在URL寫出想查詢的資料，http://127.0.0.1:5000/cities?city_name=台北
@app.route('/cities', methods=['GET'])
def city_name():
    if 'city_name' in request.args:
        city_name = request.args['city_name']
    else:
        return "Error: No city_name provided. Please specify a city_name."
    results = []

    for city in cities:
        if city['city_name'] == city_name:
            results.append(city)

    return jsonify(results)

@app.route('/gapminder/all', methods=['GET'])
# 直接輸出所有gapminder_list資料
def gapminder_all():
    return jsonify(gapminder_list)

# 另外也可以給使用者指定想要的資料，可以改為以下程式碼：
# 使用者就在URL寫出想查詢的資料，http://127.0.0.1:5000/gapminder?country=Taiwan
@app.route('/gapminder', methods=['GET'])
def country():
    if 'country' in request.args:
        country = request.args['country']
    else:
        return "Error: No country provided. Please specify a country."
    results = []

    for elem in gapminder_list:
        if elem['country'] == country:
            results.append(elem)

    return jsonify(results)

app.run()