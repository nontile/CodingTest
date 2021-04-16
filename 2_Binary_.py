# 대략 정수를 받아서 2진수로 변경한다음 1과 1 사이의 0이 가장 긴 값을 반환하는 문제이다. 

# 예를 들면 어떠한 정수를 이진수로 변환했을 때 10001001이 나온다고 가정했을 때, 
# 반환되어야 할 것은 첫번째 1과 다섯번째 1사이의  000, 즉 3을 반환해야 한다. 

# 내가 참고한 영상을 촬영해주신 분은 항상 '분할정복법'에 의거하여 문제를 푸신다. 

# 1) 입력받은 정수를 이진수로 고친다.

# 2) 변환된 이진수의 1의 위치를 찾아낸다. 

# 3) 1의 위치를 그 다음 1의 위치에서 빼주어 그 사이 공간(0이 들어가 있는)을 찾아낸다.

# 4) 0이 없을 경우 0을 return, 0이 있다면 가장 높은 값을 가지는 0의 길이를 return



# 529 1000010001 4

# bi = bin(529)
# print(bi[2:])
from collections import deque
def solution(num):
    bi = format(num, 'b')
    dq = deque(maxlen=2)
    rs = [0]
    for i, b in enumerate(bi):
        if b == '1':
            dq.append(i)
        if len(dq) == 2:
            rs.append(dq[1] - dq[0] -1)
            
    return max(rs)

print(solution(529))
