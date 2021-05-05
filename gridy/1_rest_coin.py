# 1260 원 500원, 100원, 50원, 10원 
# 거스름돈 동전 가장작은 갯수

n = 1260
cnt = 0

arr = [500, 100, 50, 10]

for coin in arr:
    cnt += n // coin
    n %= coin

print(cnt)
