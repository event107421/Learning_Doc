"""
準備條件：
1. 申請註冊AWS的賬號（註冊AWS需要信用卡哦！）

2. 開通ElasticSearch服務（本文後面會詳細介紹這部分），ES服務的中文介紹。
目前ES並不是完全免費的，在前12個月，每月有 750 小時的 t2.small.elasticsearch 或 t3.small.elasticsearch 實例使用時間和每月 10GB 的可選 EBS 存儲量（磁性或通用）。
關於ES服務免費的最新信息，請移步AWS ElasticSearch Free Tier
https://aws.amazon.com/cn/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&all-free-tier.q=elasticsearch&all-free-tier.q_operator=AND&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all
在開通ES服務的過程中，如果你只想使用免費的服務，一定要選對 實例類型，磁盤容量和類型 等限制信息。建議在開通ES服務之前，仔細看看 AWS Free Tier。

3. 熟悉AWS的ElasticSearch開發文檔，文檔目前只有英文版的
https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html
"""

"""
在正式上傳數據之前，我們需要先預告訴ES我們想指定的數據類型，普通的數據類型（比如：String, Integer, Decimal）不需要指定，但像時間類型，坐標類型，和IP類型的數據就需要先告訴ES服務，這樣在後面上傳數據的時候才能正確解析。
這個命令只需要在上傳數據之前執行一次就可以了，這裡用curl來執行這個命令。
curl -XPUT -u 'username:password' 'https://end_point/logs' -H 'Content-Type: application/json' -d '
{
    "mappings": {
          "properties": {
                "location": {
                    "type": "geo_point"
                },
                "datetime": {
                  "type":   "date",
                  "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd HH:mm:ssZ"
                },
                "ip_addr":{
                  "type": "ip"
                }
         }
    }
}'
上面 -u 'username:password' 的為用戶名和密碼，也就是之前啟用精細訪問控制創建的主用戶和密碼。 
'https://end_point/logs' 中end_point為ES服務的終端地址，你可以在控制台中查看，終端地址的後面加上Index的值，這裡使用logs。
文檔中的屬性 location ， datetime ，和  ip_addr  分別指定為 geo_point， geo_point，和 ip類型，下面上傳數據的時候會用這些屬性。
"""

# 在運行前先通過pip安裝elasticsearch, requests-aws4auth,requests
from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
import json

# 服務終端HOST，不含HTTPS頭部分，比如：my-test-domain.us-east-1.es.amazonaws.com
host = 'end_point'
# username和password為之前的啟用精細用戶創建的用戶名和密碼
awsauth = ('username', 'password')
es = Elasticsearch(
    hosts=[{'host': host, 'port': 443}],
    http_auth=awsauth,
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection
)
bulk_file = ''
id = 1

# 打開logs.txt文件，索引數據
file = open("logs.txt", "r")
for line in file:
    ip = line.split("\t")[0]
    datetime = line.split("\t")[1]
    method = line.split("\t")[2]
    responsecode = line.split("\t")[3]
    path = line.split("\t")[4]
    geoloc = line.split("\t")[5].rstrip()
    # ip_addr: ip類型，datetime: date類型，location: geo_point類型
    index = { 'ip_addr': ip, 'datetime': datetime, 'method': method,'responsecode':responsecode,'path':path,'location':geoloc }
    bulk_file += '{ "index" : { "_index" : "logs", "_type" : "_doc", "_id" : "' + str(id) + '" } }\n'
    bulk_file += json.dumps(index) + '\n'
    id += 1

# 批量上傳數據
res = es.bulk(bulk_file)
print(res)
