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


X = 5
A = [1, 3, 1, 4, 2, 3, 5, 4]

check = [0] * 5
check_sum = 0

for i in range(len(A)):
    print(A[i] -1, end= ",")
    print(check_sum, end= "  ")
    print(check)
    if check[A[i] -1] == 0:
        check[A[i]-1] = 1
        check_sum += 1
    
        if check_sum == X:
            print(" 값 = " + str(i))
    


# 5, [1, 3, 1, 4, 2, 3, 5, 4]