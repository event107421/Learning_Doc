# 繼承類別 (Inheritance) =================================================================
# 在類別名稱後加小括號，內含所繼承類別的名稱 (稱為「父類別」，Parent class)
# 例如有一個Circle類別
class Circle:
    cx = 0
    cy = 0
    radius = 0

    def setColor(self, color):
        self.color = color

# Ball 類別繼承 Circle 類別 ===============================================================
class Ball(Circle):
    cz = 0
# 類別名稱為 Ball，繼承自 Circle 類別， 因此擁有該類別裡的所有屬性與方法：cx, cy, radius, setColor()
# 本類別另外再定義一個屬性：球心第三維座標 cz


