# N x M  얼음 틀

# 0은 구멍
# 1은 칸막

# 구멍이 상하좌우로 붙어 있는 경우 아이스크림됨
# 3개
# 00110
# 00011
# 11111
# 00000
# n = 4
# m = 5

#  입력 받는 법
# n, m = map(int, input().split())
# print(n, m)

# graph = []

# for i in range(n):
#     graph.append(list(map(int, input())))

def dfs(x, y):

    if x < 0 or y < 0 or x >= n or y >= m:
        return False

    if graph[x][y] == 0:
        
        # 방문처리
        graph[x][y] = 1

        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True


n = 3
m = 3
graph = [
    [0, 0, 1], 
    [0, 1, 0], 
    [1, 0, 1]
]
print(graph)

result = 0

if __name__ == "__main__":

    for i in range(n):
        for j in range(m):
            if dfs(i, j):
                result += 1
    print(result)



