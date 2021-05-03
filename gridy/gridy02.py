# 지금당장 좋은 것만 고르는 알고리즘
# 최적의 해를 보장할 수 없을때가 많습니다.

# N, K 숫자에서  N이 1이 될때 까지의 최소 연산수
# N-1, N/K 사용
# -1, /4, /4 => 3회
N = 8
K = 3
cnt = 0

div_cnt = N % K

N = N - div_cnt

cnt = div_cnt

while True:

    if N == 1:
        break

    if N % K == 0:
        N //= K
    else:
        N -= 1
    
    cnt += 1

print(cnt)

