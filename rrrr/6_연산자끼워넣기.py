
# + - * /
n = int(input())
nums = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().strip().split())

max_ =0
min_ =0
rs = []
def dfs(num, idx, plus, minus, mul, div):
    
    if n == idx:
        rs.append(num)
        return

    if plus:
        dfs(num+nums[idx], idx+1, plus-1, minus, mul, div)

    if minus:
        dfs(num-nums[idx], idx+1, plus, minus-1, mul, div)

    if mul:
        dfs(num * nums[idx], idx+1, plus, minus, mul-1, div)
    
    if div:
        dfs(int(num/nums[idx]), idx+1, plus, minus, mul, div-1)


dfs(nums[0], 1, plus, minus, mul, div)

print(max(rs))
print(min(rs))