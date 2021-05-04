T = 2

n , m = 3, 4

arr = [
    [1, 3, 3, 2],
    [2, 1, 4, 1],
    [0, 6, 4, 7]
]

dp = [[0] * m for _ in range(n)]
for i in range(n):
    dp[i][0] = arr[i][0]

for j in range(1, m):
    for i in range(n):
        if i == 0:
            dp[i][j] = arr[i][j] +max(dp[i][j-1], dp[i + 1][j-1])
        
        elif i + 1 == n:
            dp[i][j] = arr[i][j] +max(dp[i][j-1], dp[i - 1][j-1])
        else:
            dp[i][j] = arr[i][j] +max(dp[i][j-1], dp[i - 1][j-1], dp[i + 1][j-1])

print(max(dp[i][m-1] for i in range(n) ))
