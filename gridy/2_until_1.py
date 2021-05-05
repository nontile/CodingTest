# n 를 k로 나누든지 n -1 를 하든지 해서 n이 1이 될때까지 수행 횟수
# n =25 k =5 cnt =2

n = 25
k =3
n, k = map(int, input().split())
cnt = 0
while n != 1:
    if n % k != 0:
        n -= 1
        cnt += 1
    else:
        n //= k
        cnt += 1

print(cnt)