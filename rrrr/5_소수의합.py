# M, N = 60, 100
M = int(input())
N = int(input())
arr = []
for x in range(M, N+1):
    
    if x < 2:
        continue

    is_num = True
    for i in range(2, x):
        if x % i == 0:
            is_num = False
            break

    if is_num:
        arr.append(x)

if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))

print(arr)