arr = [4, 2, 5, 8, 4, 11, 15]

dp = [0] * len(arr)

dp[0] = arr[0]

cnt = 0
for i in range(1, len(arr)):
    if dp[i-1] > arr[i]:
        dp[i] = dp[i-1]
        cnt += 1
    else:
        dp[i] = arr[i]

print(cnt)
