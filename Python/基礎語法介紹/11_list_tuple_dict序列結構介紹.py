# 串列與tuple非常類似，唯一的差別在於: 串列可以修改，而tuple不能修改。

# 串列與tuple裡面的成員可以是任何的物件，數字、字串、其他串列或tuple，甚至是辭典、function物件...。它們也可以像字串一樣使用索引、切片來取得其中的成員。

# 串列使用中括號，tuple使用小括號，例如:
# 下例中，串列中包含數字123, 字串abc, 另一個串列[111,222], 與tuple (333,444)
a = [123, 'abc', [111,222], (333,444)]
print(a[0])
print(a[2][1])
print(a[3][1])

# 串列與tuple的索引與切片使用方式與字串完全相同
# 相加，串列或tuple可以相加，前題是串列必須與串列相加，tuple則必須與tuple相加，最後會傳回新的串列或tuple。
a = [111,222] + [333,444] + [555,666]
b = ('aaa','bbb') + ('ccc','ddd')

# 但如果要將串列與tulple相加，則會發生錯誤
c = a + b

# 若有需要將串列與tuple相加，則必須呼叫list函式將資料轉成list，或tuple函式將資料轉成tuple再相加。
c = a + list(b)
c = tuple(a) + b

# 相乘，可以將串列或tuple重複數倍。類似字串的乘法。
a = [111,222]
a * 3

b = ('aaa','bbb')
b * 5

# 修改，適當之處修改只適用於串列，不適用於tuple。
# 將串列裡的'abc'換成另一個字串:
a = [123, 'abc', [111,222], (333,444)]
a[1] = 'xyz'

# 也可以一次置換多個成員，且數量可以不同(更多或更少)
a = [123, 'abc', [111,222], (333,444)]
a[0:2] = ['aaa','bbb','ccc']

# 刪除，刪除成員只適用於串列，不適用於tuple。
a = [123, 'abc', [111,222], (333,444)]
a[1:3] = []

# 另外，刪除也可以用 del 敘述
a = [123, 'abc', [111,222], (333,444)]
del(a[1:3])

# 不用索引的方式刪除，也可以呼叫remove方法依內容來刪除, 但限制一次只能刪除一個成員。
a = [123, 'abc', [111,222], (333,444)]
a.remove('abc')
a.remove([111,222])

# append與pop，新增成員只適用於串列，不適用於tuple。可以呼叫append方法，增加成員到串列。
a = [123,456]
a.append(789)

# 呼叫pop取出串列成員，可以指定索引，若不指定則預設為最後一個，並在取出後從串列刪除該成員。
a = [111,222,333,444,555]
a.pop()
a.pop(0)

# 關於tuple有一個更偷懶的方法，就是不加小括號
a = 111, 222, 333

# 但如果只有一個項目，不管有沒有加小括號都要在後面加逗號
a = 111,
a = (111,)

# 下例b因沒有加逗號，而被誤認為數字111
b = 111
b = (111)

# 有一個用法也很方便，就是要交換2個變數值，以傳統C語言的寫法可能會是:
temp = a
a = b
b = temp

# 在python可以這麼寫:
a = 1
b = 2
a, b = b, a

# Dictionary(字典)介紹 ============================================
# Iterable(可疊代的)：和前面介紹的字串(String)、串列(List)及元組(Tuples)一樣是可疊代的物件，可以透過Python迴圈來進行元素的讀取。
# Modifiable(可修改的)：和串列(List)一樣可以透過Python提供的方法(Method)來對Dictionary(字典)的值進行修改。
# Key-Value pairs(鍵與值)：Dictionary(字典)的每一個元素由鍵(Key)及值(Value)構成。鍵(Key)的資料型態通常我們使用String(字串)或Integer(整數)，而值(Value)可以是任何資料型態。
# 建立dic
hights = {"mike":170, "peter":180}
# 也可以使用dic函數來給值
hights = dict(mike = 170, peter = 180)

# 取出Dictionary元素的方法，使用 [] 符號，傳入鍵(Key)的名稱
hights["mike"]

# 也可以使用get函數
hights.get("mike")

# 新增Dictionary元素的方法，於 [] 符號中輸入要新增的鍵(Key)的名稱，並且指派一個值(Value)給它
hights["john"] = 175

# 修改Dictionary元素的方法，於 [] 符號中輸入鍵(Key)的名稱，並且指派要修改的值(Value)給它
hights["mike"] = 185

# 刪除Dictionary元素的方法，使用del指令，並且於 [] 符號中輸入要刪除的元素鍵(Key)名稱
del hights["mike"]

# 也可以用clear刪除字典(Dictionary)中的所有元素
hights.clear()

# dict多鍵值：多個鍵值對應一個值
dict = {('one1', 'one2'): 'a', ('one3', 'one4'): 'b'}

# dic多個值：一個鍵值對應多個值
dict = {'one1': (1, 4), 'one3': (2, 5)}

# 將兩個列表(list)組成一個字典(dict)
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dictionary = dict(zip(keys, values))
print(dictionary)

# 合併兩個dict，假設有兩個dict x和y，合併成一個新的dict，不改變 x和y的值
# 在python3.5中支援了該語法
z = {**x, **y}
# 也可以用以下方法
z = x.copy()
z.update(y)

# 循環賦值：可以利用此特性，循環賦予某個鍵多個值
dict = {}
dict.setdefault('key1', [])
dict['key1'].append(1)
dict.setdefault('key1', [])
dict['key1'].append(2)

dict['key1'][0]
dict['key1'][1]