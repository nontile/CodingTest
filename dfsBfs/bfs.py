from collections import deque

tickets = [ 
    [], 
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
] 
visited = [False] * 9

def bfs(graph, start):

    dq = deque([start])

    visited[start] = True
    print("start")
    while dq:
        v= dq.popleft()
        print(v, end=" ")

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                dq.append(i)

bfs(tickets, 1)
# //12387456