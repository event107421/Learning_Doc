"""
面向對象
python使用對象模型來存儲數據，也就是說構造任何類型的值都是一個對象。
所有的python對象都擁有三個特性：身份id、類型、值。
"""

# 身分id ================================
a = 1
b = 1
c = 1000
d = 1000
a is b # 輸出是True
c is d # 輸出是False

id(a), id(b), id(c), id(d) # 輸出是(11258984, 11258984, 12386056, 11594792)

"""
可以看出上面例子，a和b指向同一個對象，但c和d卻不同，這是為什麼呢？
這是因為，整數對象和字符串對象是不可變對象，python會很高效的緩存它們，不過整數對象僅緩存簡單整數
如上面例子中的1就是簡單整數，而1000不是簡單整數就不會緩存，id自然就也不一樣
所以例子中，a is b等價於id(a) == id(b)
"""

# 類型 ===================================
"""
對象的類型決定了該對象可以保存什麼類型的值，可以進行什麼樣的操作，以及遵循什麼樣的規則
可以用內建函數type()查看python對象的類型
例如python有一系列的基本（內建）數據類型，其標準類型（基本數據類型）
包括數字、整型、布爾型、長整型、浮點型、複數型、字符串、列表、元組和字典，還有一些其它的內建類型
"""

# 值 =====================================
"""
對象表示的數據項。布爾邏輯運算符包括and、or、not
對象值的比較除了一些常見的運算符（< > <= >= == !=）之外，還可以使用cmp()內建函數
"""