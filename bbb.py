# 오름차순

# 둘다 작은데 다음것이 이전것들보다 커

A = [2, 1, 6, 4, 3, 7]

B =[]
for i in range(len(A)):
    if i != 0 and i < len(A) -1:
        
        if A[i - 1] < A[i]:
            
            if A[i - 1] < A[i + 1]:
                print( A[i - 1] , A[i], A[i + 1])
                B.append(i)
    elif i == len(A ) -1:
        if A[i - 1] < A[i]:
            print( A[i - 1] , A[i])
            B.append(i)

print(len(B))
