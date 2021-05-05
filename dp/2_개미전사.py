# n = 4
# cago = (1, 3, 1, 5)

n = int(input())

cago = list(map(int, input().split()))

arr = [0] * n

arr[0] = cago[0]
arr[1] = max(cago[0], cago[1])

for i in range(2, n):
    cur = cago[i] + arr[i-2]
    if cur > arr[i -1]:
        arr[i] = cur
    else:
        arr[i] = arr[i-1]

print(arr[n-1])