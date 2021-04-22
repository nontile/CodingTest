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

visited = [False] * 9 # 0인뎃스 안사용

def dfs(tickets, v, visited):
    
     visited[v] = True

     print(v, end=" ")

     for i in tickets[v]:
         if not visited[i]:
             dfs(tickets, i, visited)


dfs(tickets, 1, visited)

# 1 2 7 6 8 3 4 5 