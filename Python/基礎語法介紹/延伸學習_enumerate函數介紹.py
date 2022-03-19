# enumerate()函數用於將一個可遍歷的數據對象(如列表、元組或字符串)組合為一個索引序列，同時列出數據和數據下標，一般用在 for 循環當中

# 參數
# sequence：一個序列、迭代器或其他支持迭代對象
# start：下標起始位置
enumerate(sequence, [start=0])

# 範例
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# 下標預設從0開始
list(enumerate(seasons))
# 下標從1開始
list(enumerate(seasons, start = 1))


# 一般for迴圈
i = 0
seq = ['one', 'two', 'three']
for element in seq:
    print(i, seq[i])
    i +=1

#  使用enumerate函數
i = 0
seq = ['one', 'two', 'three']
for i, element in enumerate(seq):
    print(i, element)