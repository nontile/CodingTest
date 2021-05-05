# 0-9로 된 문자열 S
# 왼쪽에서부터 하나씩 +, X 때 왼쪽부터 순서대로
# 만들수 있는 가장큰수
# 02984 => 0 + 2 *9 * 8 * 4
# 0, 1 은 더하고 나머지는 곱하게

s = "02984"
rs = 0
for i in range(len(s)):
    n = int(s[i])
    if i == 0:
        rs = n
    
    if n <= 1 or rs <= 1:
        rs += n
    else:
        rs *= n

print(rs)