# 개구리가 강을 건넌다.
# 처음위치는 position 0
# postion x +1
# A[K] 초당 측정된 위치
# 최소시간을 찾아라 
# A[0]= 1
# A[1]= 3
# A[2]= 1
# A[3]= 4
# A[4]= 2
# A[5]= 3
# A[6]= 5 => x
# A[7]= 4

A = [1, 3, 1, 4, 2, 3, 5, 4]
X = 5

def sol(A, X):
    new = [0] * X
    new_sum = 0

    for i in range(len(A)):
        if new[A[i] - 1] == 0:
            new[A[i] -1] = 1
            new_sum += 1
            
            # print(new_sum)
            if new_sum == X:
                return i
    return -1

print(sol(A, X))
