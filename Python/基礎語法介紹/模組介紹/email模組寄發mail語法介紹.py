# 引用smtplib模組(Module)，主要負責傳送郵件，即一個傳送郵件的動作，如連線郵箱伺服器、登入郵箱、傳送郵件，接著根據使用的SMTP伺服器，透過關鍵字參數(Keyword Argument)指定伺服器位置及埠號
import smtplib

"""
在email套件(Package)下的mime(Multipurpose Internet Mail Extensions)子套件
為網際網路媒體類型，定義了在網路上傳輸電子郵件的格式標準
在其底下的multipart子套件中，MIMEMultipart類別能夠讓電子郵件的格式包含純文字或HTML的內容
email套件主要負責構造郵件，指的是郵箱頁面顯示的一些構造，如發件人，收件人，主題，正文，附件等
"""
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# 建立附件內容
from email.mime.application import MIMEApplication

# 若是需要在email內傳送圖片，則需在Python專案中引用MIMEImage類別，並且引用pathlib函式庫來讀取圖片
from email.mime.image import MIMEImage
from pathlib import Path

# 引用string模組(Module)的Template類別，用來替換郵件樣版中的參數值
from string import Template


username = 'test@gmail.com'
# 應用程式密碼，不是登入gmail的密碼
# 申請應用程式密碼可以看以下網址教學：https://www.learncodewithmike.com/2020/02/python-email.html
password = 'test'

send_list = [
'test@gmail.com',
]

# 建立MIMEMultipart物件，一封基本的電子郵件，分別有標題、寄件者、收件者及內容，透過MIMEMultipart物件即可進行各欄位的資料設定
content = MIMEMultipart()
# 郵件內容（這個部分可以利用html語法客製化郵件樣版），_subtype（次型態）預設格式為'plain'，也可以等客製化樣板後設定為html，另外也可以
content.attach(MIMEText("Demo python send email"), _subtype='plain', _charset='utf-8')

# 另外如上述所說，郵件內容除了文字外，也可以利用html來客製化郵件內容的樣板，以下建立一個success_template.html檔案，內容如下
"""
/* 電子郵件樣版不需要<head>標籤中的內容 */
<!DOCTYPE html>
<html>
    <head>
    </head>
    <body>
      Hello <strong>$user</strong>, your test is success!
    </body>
</html>
"""
# 建立Template物件，傳入郵件樣版內容，可以透過Path物件的read_text()方法來達成
template = Template(Path("success_template.html").read_text())
# 如果郵件樣版中，設定了一個前面加了 $ 符號的變數，如上面html檔案中的user變數，這用來表示此參數為Python程式碼動態傳入，此時就可以呼叫Template物件的substitute()方法來設定郵件樣版中的參數值，其參數可傳入Python的字典(Dictionary)或關鍵字參數(Keyword Argument)
body = template.substitute({ "user": "Mike" })
# 在MIMEMultipart物件的指定郵件內容地方傳入body，並且設定為HTML的格式
content.attach(MIMEText(body, _subtype="html"))

# 也可以在郵件附加圖片內容
content.attach(MIMEImage(Path("koala.jpg").read_bytes()))

# 也可以利用MIMEApplication方法構建郵件附件
# 獲取檔案路徑
file = '/Users/bill/Downloads/RD联盟相关数据.xlsx'
# 開啟附件
part_attach1 = MIMEApplication(open(file, 'rb').read())
# 為附件命名
part_attach1.add_header('Content-Disposition', 'attachment', filename='RD联盟相关数据.xlsx')
# 新增附件進要寄發的mail內
content.attach(part_attach1)

# 郵件標題
content["subject"] = "Learn Code With Mike"
# 寄件者
content["from"] = username  
# 收件者，假設有很多位收件者，可以利用字串組合join的方式來合併，產生一串收件者的字串
content["to"] = ','.join(receiver) 

# 這邊利用Python的with陳述式，當郵件寄送完成後，自動釋放資源。
with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
    try:
        # 利用ehlo()方法來驗證SMTP伺服器及埠號是否正確
        smtp.ehlo()
        # starttls()方法建立TLS(Transport Layer Security)加密傳輸，為一種網路傳輸安全協定，用來保護資料的安全及完整性
        smtp.starttls()
        # 登入寄件者的Gmail帳戶
        smtp.login(username, password)
        # 寄送郵件
        smtp.send_message(content)
        print("Complete!")
    except Exception as e:
        print("Error message: ", e)

