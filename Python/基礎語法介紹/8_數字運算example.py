# 變量賦值時 Number 對象將被創建
var1 = 1
var2 = 10

# 可以通過使用del語句刪除單個或多個對象的引用
del var
del var_a, var_b

# Python 支持三種不同的數值類型
# 整數(Int)
# 浮點數(float)
# 複數(complex)，complex(a,b)表示， 複數的實部a和虛部b都是浮點型

# 十六進制
number = 0xA0F
# 八進制
number = 0o37

# 數字類型轉換
int(x) # 將x轉換為一個整數

float(x) # 將x轉換到一個浮點數

complex(x) # 將x轉換到一個複數，實數部分為 x，虛數部分為 0

complex(x, y) # 將 x 和 y 轉換到一個複數，實數部分為 x，虛數部分為 y ， x 和 y 是數字表達式

# 可以使用 ** 操作來進行冪運算
5 ** 2  # 5 的平方

# 返回數字的絕對值，如abs(-10) 返回 10
abs(x)

# 返回數字的上入整數，如math.ceil(4.1) 返回 5
ceil(x)

# 返回數字的下舍整數，如math.floor(4.9)返回 4
floor(x)

# 返回e的x次冪(e^x)
exp(x)

# 返回數字的絕對值，如math.fabs(-10) 返回10.0
fabs(x)

# math.log(math.e)返回1.0，math.log(100,10)返回2.0
log(x)

# 返回以10為基數的x的對數，如math.log10(100)返回 2.0
log10(x)

# 返回給定參數的最大值，參數可以為序列
max(x1, x2,...)

# 返回給定參數的最小值，參數可以為序列
min(x1, x2,...)

# 返回x的整數部分與小數部分，兩部分的數值符號與x相同，整數部分以浮點型表示
modf(x)

# x**y 運算後的值
pow(x, y)

# 返回浮點數x的四捨五入值，如給出n值，則代表舍入到小數點後的位數
round(x [,n])

# 返回數字x的平方根
sqrt(x)

# 從序列的元素中隨機挑選一個元素，比如random.choice(range(10))，從0到9中隨機挑選一個整數
choice(seq)	

# 從指定範圍內，按指定基數遞增的集合中獲取一個隨機數，基數缺省值為1
randrange ([start,] stop [,step])

# 隨機生成下一個實數，它在[0,1)範圍內
random()

# 改變隨機數生成器的種子seed。如果不了解其原理，不必特別去設定seed，Python會幫你選擇seed
seed([x])

# 將序列的所有元素隨機排序
shuffle(lst)

# 隨機生成下一個實數，它在[x,y]範圍內
uniform(x, y)

# 返回x的反餘弦弧度值
acos(x)

# 返回x的反正弦弧度值
asin(x)

# 返回x的反正切弧度值
atan(x)

# 返回給定的 X 及 Y 坐標值的反正切值
atan2(y, x)	

# 返回x的弧度的餘弦值
cos(x)

# 返回歐幾里德範數 sqrt(x*x + y*y)
hypot(x, y)

# 返回的x弧度的正弦值
sin(x)

# 返回x弧度的正切值
tan(x)

# 將弧度轉換為角度，如degrees(math.pi/2)，返回90.0
degrees(x)

# 將角度轉換為弧度
radians(x)
