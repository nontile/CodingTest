# 2, 15

# n = 2 # 100
# m = 15 # 10000
# oper = [2,3]
n, m = map(int, input().split())
oper = []
for i in range(n):
    oper.append(int(input()))
d = [99999] * (m +1)
d[0] =0
for k in range(n):    
    for i in range(oper[k], m + 1): 
        if d[i - oper[k]] < 99999:
            d[i] = min(d[i], d[i - oper[k]] + 1)

rs = d[m]
if rs < 99999:
    print(rs)
else:
    print(-1)
