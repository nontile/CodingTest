from collections import deque

n, m = map(int, input().split(" "))
print(n, m)

visited = [[0] * n] * m
graph = [
    [1, 0, 0],
    [1, 0, 0],
    [1, 1, 1],
]
print(graph)

def check(x, y):
    # print(x, y)
    if x <= 0 or x >= n or y <= 0 or y >= m: 
        return False
    if graph[x][y] == 0: 
        return False
    

    return True


dq = deque()
def bfs(x, y, visited):

    count_ = 0
    dq.append((x, y))
    
    while dq:
        x, y = dq.popleft()
        
        visited[x][y] = 1
        print(x, y, count_)

        # up
        if check(x, y+1):
            # bfs(x, y+1, count_)
            dq.append(x, y+1)
            count_ += 1
        
        # down
        if check(x, y-1):
            # bfs(x, y-1, count_)
            count_ += 1
            dq.append(x, y+1)
        
        # left
        if check(x-1, y):
            # bfs(x -1, y, count_)
            count_ += 1
            dq.append(x, y+1)
        
        # right
        if check(x+1, y):   
            # bfs(x+1, y, count_)
            count_ += 1
            dq.append(x, y+1)
    return count_
count_ = 0
# for i in range(n):
#     for j in range(m):
#         print(count_)
        

print(bfs(0, 0))
