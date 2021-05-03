# 양의 정수 n이 주어졌을 때, 이를 이진수로 나타냈을 때 1의 위치를 모두 찾는 프로그램을 작성하시오. 
# 최하위 비트(least significant bit, lsb)의 위치는 0이다.
# 1 13 => 0 2 3

# T, n = 1, 13

T, n = map(int, input().split())
index = 0
while True:
    T -= 1
    while n > 0:
        n, r = divmod(n, 2)
        if r == 1:
            print(index, end=" ")
        
        index += 1
    if T < 1: break

