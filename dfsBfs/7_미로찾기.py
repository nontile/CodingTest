# 미로찾기 최단거리 BFS
from collections import deque
n, m = 5, 6

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
graph = [
    [1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
]
def bfs(x, y):

    dq = deque([(x,y)])
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            px = x + dx[i]
            py = y + dy[i]
            if -1 < px < n and -1 < py < m and graph[px][py] == 1:
                dq.append((px, py)) 
                graph[px][py] = graph[x][y] + 1
    graph[n-1][m-1]

bfs(0, 0)

print()