# 지금당장 좋은 것만 고르는 알고리즘
# 최적의 해를 보장할 수 없을때가 많습니다.

# 500, 100, 50, 10   동전최소갯수
# 큰단위가 작은단위의 배수가 되니까 가능

N = 1260
count = 0

array = [500, 100, 50, 10]

for coin in array:
    count += N // coin
    N %= coin

print(count)