import tensorflow as tf
# constant可以視為tf專用的變數型態
# 其他包括Variable，placeholder
A = tf.constant('Hello World!')

# 使用 with 可以讓Session自動關閉
with tf.Session() as sess:

    # 在 tensorflow內要使用run，才會讓計算圖開始執行
    B = sess.run(A)
# 黑字就是程式碼內的 "Hello World!"，紅字是警告訊息，提醒我們可以加速 TensorFlow 的執行速度之類的
    print(B)

# 可以選擇在程式碼內加兩句話，直接關閉警告訊息
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 接著我們先來看看在 TensorFlow 的架構下，幾個常用的資料型態：constant、Variable、Placeholder

# constant宣告常數
A = tf.constant(10, dtype=tf.int64)

with tf.Session() as sess:
    print(A)
    # Tensor("Const_42:0", shape=(), dtype=int64)

    print(sess.run(A))
    # 10

    # 使用 sess.run() 才能取得 A 的值

# Variable宣告變數
B = tf.Variable(0, dtype=tf.int64)
with tf.Session() as sess:
    # 變數需要初始化
    sess.run(tf.global_variables_initializer())
    # 其中，請特別注意 assign 這個函數，此函數需要經過 sess.run() 之後，才會賦予新值
    # 使用 assign 更改變數值
    for i in range(5):
        print(sess.run(B.assign(i)))
#如果上面for改成下面這樣， B 值是不會改變的，因為 assign 未被執行
for i in range(5):
    B.assign(i)
    print(sess.run(B))

# 宣告占位符
C = tf.placeholder(dtype=tf.int64)
# 下面比較特別的地方是，占位符可以使用 feed_dict 來賦值，這項功能，可以讓我們在訓練模型時能輕鬆地輸入資料
with tf.Session() as sess
    for i in range(5):
        result = sess.run(C, feed_dict={C:i})
        print(result)

# 宣告占位符
C = tf.placeholder(dtype=tf.int64)
D = tf.placeholder(dtype=tf.int64)
E = tf.placeholder(dtype=tf.int64)

F = D + E

with tf.Session() as sess:
    # 可以一次填充所有的占位符
    result = sess.run(F, feed_dict={C: 10, D: 20, E: 30})
    print(result)  # 50

    # 或者只填充計算所需要的
    result = sess.run(F, feed_dict={D: 20, E: 30})
    print(result)  # 50

    # 這段程式會使系統報錯！
    # 計算所需的占位符不能為空，每次執行 sess.run() 都要填充，
    # 占位符不是變數，不會留存上次填充的資料。
    result = sess.run(F, feed_dict={E: 30})
    print(result)

# 可以使用 TensorBoard 來展示自己所設計的架構
# 1.把欲顯示出來的步驟使用 " tf.name_scope " 包起來。
# 2.接著使用 tf.summary.FileWriter 函數輸出到目標資料夾。

# 宣告常數A&B，後面的name參數，是要繪製tensorboard時所使用的名稱。
# 若沒有指定，或是重複名稱，則tensorboard會自動修改。
A = tf.constant(50, name='const_A')
B = tf.constant(100, name='const_B')

with tf.Session() as sess:
    # 就是這邊！
    # 使用 "with tf.name_scope('Run'):" 這句話可以畫出Run這個步驟。
    with tf.name_scope('Run'):
        B = sess.run(A + B)
    print(B)

    # 畫好步驟之後，要使用"tf.summary.FileWriter"把檔案寫到目標資料夾，
    # 第二個參數表示要把整個圖層放到graph參數內，這樣才能用tensorboard畫出來。
    train_writer = tf.summary.FileWriter('/home/shayne/tfboard_Test', sess.graph)
    train_writer.close()

# 這樣子就可以把計算圖畫出來了！
# 最後一步，就是離開Python，回到Linux內，找到剛才輸出的資料夾，會有一個檔案叫做：

# events.out.tfevents.xxxxxxxxxx(一連串的數字).(主機名稱)

# 確認沒問題後，在指令列下命令：
# $ tensorboard --logdir=/home/shayne/tfboard_Test

# 這個指令的格式是：
# $ tensorboard --logdir=(your path)
# 剛才輸出的路徑是"/home/shayne/tfboard_Test"，所以就用他代換(your path)。

# 按下確認後，tensorboard就會把你專屬的計算圖輸出到網頁，網址是：

# "http://(your ip):6006"

# 假設夏恩的主機的IP是192.168.100.100的話，這時候就開啟google瀏覽器，
# 鍵入網址，就可以看到計算圖了！

# 如果網頁打不開，可以懷疑是防火牆的問題。
# 要打開防火牆，請使用以下指令，把防火牆關了：
# firewall-cmd --zone=public --add-port=6006/tcp
# service firewalld restart

# 可以把剛才的程式稍微複雜化
A = tf.constant(50, name='const_A')
B = tf.constant(100, name='const_B')

with tf.name_scope('Add'):
    C = A+B

with tf.Session() as sess:
    with tf.name_scope('Run'):
        D = sess.run(C*3)
    print(D)

    train_writer = tf.summary.FileWriter('/home/shayne/tfboard_Test', sess.graph)
    train_writer.close()