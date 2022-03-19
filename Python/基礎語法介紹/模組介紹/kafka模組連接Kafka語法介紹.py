# 有時間讀一下，下面網址，把相關重點整理進來
"""
https://blog.csdn.net/fenglepeng/article/details/109454576
https://blog.csdn.net/u013256816/article/details/79996056
"""

# Kafka介紹
"""
參考網址：https://www.cnblogs.com/flaming/p/11304278.html

Kafka中的相關概念：
一般的來說，一個Kafka集群包含一個或多個的Producer，一個或多個的Broker，一個或多個的Consumer Group，和一個Zookeeper集群
Kafka通過Zookeeper管理集群配置，管理集群在運行過程中負責均衡、故障轉移和恢復什麼的。 Producer使用Push（推送）的方式將消息發佈到Broker，Consumer使用Pull（拉取）的方式從Broker獲取消息，兩者都是主動操作的

對於傳統的MQ而言，一般經過消費後的消息都會被刪除，而Kafka卻不會被刪除，始終保留著所有的消息，只記錄一個消費者消費消息的offset（偏移量）作為標記，可以允許消費者可以自己設置這個offset，從而可以重複消費一些消息。
但不刪除肯定不行，日積月累，消息勢必會越來越多，佔用空間也越來越大。 Kafka提供了兩種策略來刪除消息：一是基於時間，二是基於Partition文件的大小，可以通過配置來決定用那種方式。不過現在磁盤那麼廉價，空間也很大，隔個一年半載刪除一次也不為過。

以下來解釋一下kafka各個結構：
https://img2018.cnblogs.com/blog/815062/201908/815062-20190806095835453-1698523557.png

Producer（生產者）：
生產者，顧名思義，就是生產東西的，也就是發送消息的，生產者每發送一個條消息必須有一個Topic（主題），也可以說是消息的類別，生產者源源不斷的向kafka服務器發送消息。
生產者發送消息時，會根據Partition的策略來決定存到那個Partition中，一般的默認的策略是Kafka提供的均衡分佈的策略，即實現了我們所要的負載均衡。
當我們的消息對順序沒有要求的話那就多設置幾個分區，這樣就能很好地負載均衡增加吞吐量了。分區的個數可以手動配置，也可以在創建Topic的時候就事先指定。
發送消息的時候，需要指定消息的key值，Producer會根據這個key值和Partition的數量來決定這個消息發到哪個分區，可能裡邊就是一個hash算法。

Topic（主題）：
每一個發送到Kafka的消息都有一個主題，也可叫做一個類別，類似我們傳統數據庫中的表名一樣，比如說發送一個主題為order的消息，那麼這個order下邊就會有多條關於訂單的消息，只不過kafka稱之為主題，都是一樣的道理。

Partition（分區）：
生產者發送的消息數據Topic會被存儲在分區中，這個分區的概念和ElasticSearch中分片的概念是一致的，都是想把數據分成多個塊，好達到我們的負載均衡，合理的把消息分佈在不同的分區上，分區是被分在不同的Broker上也就是服務器上，這樣我們大量的消息就實現了負載均衡。
每個Topic可以指定多個分區，但是至少指定一個分區。每個分區存儲的數據都是有序的，不同分區間的數據不保證有序性。因為如果有了多個分區，消費數據的時候肯定是各個分區獨立開始的，有的消費得慢，有的消費得快肯定就不能保證順序了。
那麼當需要保證消息的順序消費時，我們可以設置為一個分區，只要一個分區的時候就只能消費這個一個分區，那自然就保證有序了。

Topic（主題）、Partition（分區）：
Kafka最初設計初衷就是高吞吐率、速度快。所以在對Topic和Partition的設計中，把Topic分成一個或者多個分區，每個Partition在物理磁盤上對應一個文件夾，該文件夾下存儲這個Partition的所有消息和索引文件。
當我們創建一個Topic是，同時可以指定分區數據，數目越多，吞吐量越大，但是消耗的資源也越多，當我們向Kafka發送消息時，會均衡的將消息分散存儲在不同的分區中。
在存儲的過程中，每條消息都是被順序寫到磁盤上的。 （順序寫磁盤的時候比隨機寫內存的想效率還高，這也是Kafka快的一個原因之一）。
https://img2018.cnblogs.com/blog/815062/201908/815062-20190806155549641-383964701.png

Replica（副本）：
副本就是分區中數據的備份，是Kafka為了防止數據丟失或者服務器宕機採取的保護數據完整性的措施，一般的數據存儲軟件都應該會有這個功能。假如我們有3個分區，由於不同分區中存放的是部分數據，所以為了全部數據的完整性，我們就必須備份所有分區。
這時候我們的一份副本就包括3個分區，每個分區中有一個副本，兩份副本就包含6個分區，一個分區兩份副本。 Kafka做了副本之後同樣的會把副本分區放到不同的服務器上，保證負載均衡。
講到這我們就可以看見，這根本就是傳統數據庫中的主從復制的功能，Kafka會找一個分區作為主分區（leader）來控制消息的讀寫，其他的（副本）都是從分區（follower），這樣的話讀寫可以通過leader來控制，然後同步到副本上去，保證的數據的完整性。
如果有某些服務器宕機，我們可以通過副本恢復數據，也可以暫時用副本中的數據來使用。
PS：這個東西實際跟ElasticSearch中的副本是完全一致的

Broker（實例或節點）：
這個意思就是Kafka的實例，啟動一個Kafka就是一個Broker，多個Brokder構成一個Kafka集群，這就是分佈式的體現，服務器多了自然吞吐率效率啥的都上來了。

Consumer Group（消費者組）和 Consumer（消費者）：
Consume消費者來讀取Kafka中的消息，可以消費任何Topic的數據，多個Consume組成一個消費者組，一般的一個消費者必須有一個組（Group）名，如果沒有的話會被分一個默認的組名。
傳統的消息隊列有兩種傳播消息的方式，一種是單播，類似隊列的方式，一個消息只被消費一次，消費過了，其他消費者就不能消費了；另一種是多播，類似發布-訂閱的模式，一個消息可以被多個消費者同時消費。
Kafka通過消費者組的方式來實現這兩種方式，在一個Consumer Group中，每一個Topic中的消息只能被這個組中的一個Consumer消費，所以對於設置了多分區的Topic來說，分區的個數和消費者的個數應該是一樣的，一個消費者消費一個分區，這樣每個消費者就成了單播形式，類似隊列的消費形式。
所以說，一個消費者組裡邊的消費者不能多於Topic的分區數，一旦多於，多出來的消費者就不能消費到消息。另外，不同的消費者組可以同時消費一個消息，這樣就實現了多播，類似發布-訂閱的模式。我們可以設置每個組中一個消費者的方式來實現發布-訂閱的模式。
當我們有多個程序都要對消息進行處理時，我們就可以把他們設置到不同的消費者組中，來實現不同的功能。
"""

# 建立生產者
"""
首先使用KafkaProducer類連線 Kafka，獲得一個生產者物件，然後往裡面寫資料
bootstrap_servers用於指定 Kafka 的伺服器連線地址
value_serializer用來指定序列化的方式。這裡我使用 json 來序列化資料，從而實現我向 Kafka 傳入一個字典，Kafka 自動把它轉成 JSON 字串的效果。

producer.send函數為發送消息
第1個參數為 topic名稱，必須指定
key：鍵，必須是字節字符串，可以不指定（但key和value必須指定1個），默認為None
value：值，必須是字節字符串，可以不指定（但key和value必須指定1個），默認為None
partition：指定發送的partition，由於kafka默認配置1個partition，固為0

future.get函數等待單條消息發送完成或超時，經測試，必須有這個函數，不然發送不出去，可用time.sleep代替
"""
import json
import time
import datetime
import config
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=config.SERVER,
                         value_serializer=lambda m: json.dumps(m).encode(),
                         security_protocol="SASL_PLAINTEXT",
                         sasl_mechanism="PLAIN",
                         sasl_plain_username=config.USERNAME,
                         sasl_plain_password=config.PASSWORD)

for i in range(100):
    data = {'num': i, 'ts': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    producer.send(config.TOPIC, data)
    time.sleep(1)


# 建立消費者
"""
Kafka 消費者也需要連線 Kafka，首先使用KafkaConsumer類初始化一個消費者物件，然後迴圈讀取資料
KafkaConsumer()函數參數介紹：
Topic：你可以把這個 Topic 理解成 Redis 的 Key
bootstrap_servers：用於指定 Kafka 伺服器連線地址
group_id：這個引數後面的字串可以任意填寫。如果兩個程式的Topic與group_id相同，那麼他們讀取的資料不會重複，兩個程式的Topic相同，但是group_id不同，那麼他們各自消費全部資料，互不影響。
"""
import config
from kafka import KafkaConsumer

consumer = KafkaConsumer(config.TOPIC,
                         bootstrap_servers=config.SERVER,
                         group_id='test',
                         auto_offset_reset='earliest')
for msg in consumer:
    print(msg.value)

"""
利用subscribe()函數訂閱多個topic，可同時接收多個topic消息
"""
from kafka import KafkaConsumer

consumer = KafkaConsumer(group_id='group2', bootstrap_servers=['localhost:9092'])
consumer.subscribe(topics=['my_topic', 'topic_1'])
for msg in consumer:
    print(msg)

# 也可用正則訂閱一類topic
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(group_id='group2', bootstrap_servers= ['localhost:9092'], value_deserializer=lambda m: json.loads(m.decode('ascii')))
consumer.subscribe(pattern='^my.*')
for msg in consumer:
    print(msg)

"""
消費者端接收消息如下：
ConsumerRecord(topic='my_topic', partition=0, offset=4, timestamp=1529569531392, timestamp_type=0, key=b'my_value', value=None, checksum=None, serialized_key_size=8, serialized_value_size=-1)

我們接收到的每筆資料都會長得像上面的形式，其中各個參數代表的意思如下：
topic：
partition：
offset：這條消息的偏移量
timestamp：時間戳
timestamp_type：時間戳類型
key：key值，字節類型
value：value值，字節類型
checksum：消息的校驗
serialized_key_size：序列化key的大小
serialized_value_size：序列化value的大小，可以看到value=None時，大小為-1
"""

"""
超時處理
若不指定 consumer_timeout_ms，默認一直循環等待接收，若指定，則超時返回，不再等待

consumer_timeout_ms ： 毫秒數
"""
from kafka import KafkaConsumer
consumer = KafkaConsumer('my_topic', group_id='group2', bootstrap_servers=['localhost:9092'], consumer_timeout_ms=1000)
for msg in consumer:
    print(msg)

"""
手動分配partition
"""
from kafka import KafkaConsumer
from kafka import TopicPartition

consumer = KafkaConsumer(group_id='group2', bootstrap_servers=['localhost:9092'])
consumer.assign([TopicPartition(topic='my_topic', partition=0)])
for msg in consumer:
    print(msg)

"""
解碼json數據：
編碼（生產者）：value_serializer
解碼（消費者）：value_deserializer
"""

# 生產者存入json格式的數據
from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda m: json.dumps(m).encode('ascii'))
future = producer.send('my_topic',  value={'value_1': 'value_2'}, partition=0)
future.get(timeout=10)

# consumer沒有解碼收到的數據，顯示如下：
# ConsumerRecord(topic='my_topic', partition=0, offset=22, timestamp=1529575016310, timestamp_type=0, key=None, value=b'{"value_1": "value_2"}', checksum=None, serialized_key_size=-1, serialized_value_size=22)
# 可以看到value為原始的json字節數據，接下來可以再做一步解碼操作

# 消費者加上value_deserializer參數進行解碼
consumer = KafkaConsumer(group_id='group2', bootstrap_servers=['localhost:9092'], value_deserializer=lambda m: json.loads(m.decode('ascii')))
consumer.subscribe(topics=['my_topic', 'topic_1'])
for msg in consumer:
    print(msg)

# 發送字符串類型的key和value
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], key_serializer=str.encode, value_serializer=str.encode)
future = producer.send('my_topic', key='key_3', value='value_3', partition=0)
future.get(timeout=10)

# 指定 key_serializer 和 value_serializer 為 str.encode,但消費者收到的還是字節字符串，若想要消費者收到的為字符串類型，就需要解碼操作，key_deserializer= bytes.decode
consumer = KafkaConsumer(group_id='group2', bootstrap_servers=['localhost:9092'], key_deserializer=bytes.decode, value_deserializer=bytes.decode)
consumer.subscribe(pattern='^my.*')
for msg in consumer:
    print(msg)

"""
可壓縮消息發送

compression_type='gzip'

若消息過大，還可壓縮消息發送，可選值為 'gzip', 'snappy', 'lz4', or None
"""
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], compression_type='gzip')
future = producer.send('my_topic', key=b'key_3', value=b'value_3', partition=0)
future.get(timeout=10)

# KafkaAdminClient：利用客戶端操作 ================================
# 取得kafka內所有的主題
client = KafkaAdminClient(bootstrap_servers=['localhost:9092'])
client.list_topics()


# 應用實例 =======================================================
bootstrap_servers = '設定host:port'
topic = [u'topic_1', u'topic_2', ..., ]

# 執行下列語法時，若是出現此錯誤：check_version raise Errors.NoBrokersAvailable()，代表應是api_version的問題
# consumer = KafkaConsumer(bootstrap_servers=bootstrap_servers, group_id='test')
# 此時我們要加上api_version參數，若kafka版本為0.10，則 api_version=(0, 10)，若kafka版本為0.10.2，則 api_version=(0, 10, 2)
consumer = KafkaConsumer(bootstrap_servers=bootstrap_servers, group_id='test', api_version=(0, 10))
# 若是還有問題，可以參考以下解決方法
# 修改Kafka配置文件server.properties，將listeners=PLAINTEXT://x.x.x.x:port修改為以下配置 （x.x.x.x為服務器對外的IP）
# listeners = PLAINTEXT://x.x.x.x:port，將此行改為下面語法
# advertised.listeners=PLAINTEXT://x.x.x.x:port

# 訂閱多個topic
consumer.subscribe(topics=topic)

for msg in consumer:
    message = msg.value.decode('utf-8')
    print(message)