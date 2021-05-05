# 5 나누기 3나누기 2나누기 -1
# 26 => -1 /5 /5 하면 1 답은 3(번 연산)

x = 26

d = [0] * 1001

for i in range(2, x + 1):

    d[i] = d[i-1] + 1

    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] +1)
    
    if i % 3 == 0:
        d[i] = min(d[i], d[i //3] + 1)
    
    if i % 5 == 0:
        d[i] = min(d[i], d[i //5] +1)

print(d[x])

