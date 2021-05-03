from collections import deque
# miro = [
#     [1, 0, 0],
#     [1, 0, 0],
#     [1, 1, 1]
# ]

n, m = map(int, input().split(" "))

visited = [ [0] * m for _ in range(n)]

miro = [list(map(int,input())) for _ in range(n)]
print(miro)
dq = deque()
dq.append((0, 0))
visited[0][0] = 1

while dq:
    x, y = dq.popleft()
    
    
    # up
    if y +1 < m and visited[x][y+1] == 0 and miro[x][y+1] == 1 :
        dq.append((x,y+1))
        visited[x][y+1] = visited[x][y] + 1
        print(1, visited)
    # down
    if y -1 >= 0 and visited[x][y-1] == 0 and miro[x][y-1] == 1:
        dq.append((x, y-1))
        visited[x][y-1] = visited[x][y] + 1
        print(2, visited)
    # left
    if x -1 >= 0 and visited[x-1][y] == 0 and miro[x-1][y] == 1:
        dq.append((x-1,y))
        visited[x-1][y] = visited[x][y] + 1
        print(3, visited)
    # right
    if x + 1 < n and visited[x+1][y] == 0 and miro[x+1][y] == 1:
        dq.append((x+1,y))
        visited[x+1][y] = visited[x][y] + 1
        print(4, visited)
    
print(visited[n-1][m-1])
