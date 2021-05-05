graph = [
    [],
    [2,3],
    [5,1],
    [1, 4],
    [5,3],
    [4, 2],
]



n, m, v = 5, 5, 3

arr = [[0]* (n+1)for _ in range(n+1)]
for i in range(m):
    start, end = map(int, input().split())
    arr[start][end] = 1
    arr[end][start] = 1

print(arr)

visited = [False] * (n +1)
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, v, visited) 
print()
from collections import deque

visited2 = [False] * (n + 1)
def bfs(graph, start, visited2):
    dq = deque()
    dq.append(start)
    visited2[start] = True

    while dq:
        v = dq.popleft()
        print(v, end=" ")
        for k in graph[v]:
            if not visited2[k]:
                dq.append(k)
                visited2[k] = True

bfs(graph, v, visited2)            

    