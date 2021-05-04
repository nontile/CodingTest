n, m = 4, 5

graph = [
    [0,0,1,1,0],
    [0,0,0,1,1],
    [1,1,1,1,1],
    [0,0,0,0,0]
]


# print(visited)

#    상  하  좌  우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs( x, y):
    if x < 0 or x >= n or y < 0 or y >= m or graph[x][y] == 1: 
        return False

    graph[x][y] = 1

    print(graph)
    
    for i in range(4):
        px = x + dx[i]
        py = y + dy[i]
        
        dfs(px, py)

    return True


cnt = 0
for x in range(n):
    for y in range(m):
        if dfs(x, y):
            cnt +=1

print(cnt)