from collections import deque
# n, m = map(int, input().split())
n, m = 5, 5
arr = [
    ['W', 'B', 'W', 'W', 'W'], 
    ['W', 'W', 'W', 'W', 'W'], 
    ['B', 'B', 'B', 'B', 'B'], 
    ['B', 'B', 'B', 'W', 'W'], 
    ['W', 'W', 'W', 'W', 'W']
]
# for i in range(n):
#     arr.append(list(input()))

visited = [[False] * m for _ in range(n)]
dx = [ 1, -1, 0, 0]
dy = [ 0, 0, 1, -1]
# print(arr)
dq = deque()
cnt = 0
def bfs(a, b):
    dq.append((a,b))
    cnt = 1
    visited[a][b] = True
    while dq:
        x, y = dq.popleft()

        for i in range(4):
            px = x + dx[i]
            py = y + dy[i]
            if 0<=px<n and 0<=py<m and not visited[px][py] and arr[x][y] == arr[px][py]:
                dq.append((px,py))
                visited[px][py] = True
                cnt += 1
    return cnt


w = 0
b = 0
for x in range(n):
    for y in range(m):
        if not visited[x][y]:
            cnt = bfs(x, y)
            if arr[x][y] == "W":
                w += cnt**2
            else:
                b += cnt**2
print(w)
print(b)