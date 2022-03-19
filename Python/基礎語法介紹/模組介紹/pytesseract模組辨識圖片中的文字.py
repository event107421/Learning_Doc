"""
OCR 為光學文字識別的縮寫（Optical Character Recognition，OCR），白話一點就是將圖片翻譯為文字
而 Tesseract 是一個 OCR 模組，目前由 Google 贊助。
Tesseract 已經有 30 年歷史，一開始它是惠普實驗室的一款專利軟體
Tesseract 也是目前公認最優秀、最精準的開源 OCR 系統。
"""
from PIL import Image
import pytesseract

img = Image.open('/Users/bill/Downloads/test.gif')

# mac在輸入以下程式碼時會出現錯誤，所以要在命令列再輸入以下命令：brew install tesseract-lang
# windows則要加上以下程式碼：
# pytesseract.pytesseract.tesseract_cmd = 'C:/OCR/Tesseract-OCR/tesseract.exe'
text = pytesseract.image_to_string(img, lang='chi_sim')
print(text)