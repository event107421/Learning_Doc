import math

def prepare_factor(max):
    prime = [1] * max
    for i in range(2, int(math.sqrt(max))):
        if prime[i] == 1:
            for j in range(2 * i, max):
                if j % i == 0:
                    prime[j] = 0
    primes = [i for i in range(2, max) if prime[i] == 1] # 質數表
           
    def factor(num):
        list = []
        i = 0
        while primes[i] ** 2 <= num:
            if num % primes[i] == 0:
                list.append(primes[i])
                num //= primes[i]
            else:
                i += 1
        list.append(num)
        f = [0] * len(list)
        for i in range(len(f)):
            f[i] = list[i]
        return f
        
    return factor

factor = prepare_factor(1000)
print(factor(100))  # 顯示 [2, 2, 5, 5]
print(factor(500))  # 顯示 [2, 2, 5, 5, 5]
print(factor(800))  # 顯示 [2, 2, 2, 2, 2, 5, 5]