# 1을 한 번, 2를 두 번, 3을 세 번, 이런 식으로 1 2 2 3 3 3 4 4 4 4 5 .. 
# 이러한 수열을 만들고 어느 일정한 구간을 주면 그 구간의 합을 구하는 것이다.
d = [0] * 1001
d[1] = 1
index = 0
for k in range(2, 200):
    for _ in range(k):
        index += 1
        d[index] = d[index-1] + k
        
rs = d[7] - d[3-1]

print(rs)
