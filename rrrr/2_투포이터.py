n = 6
m =6

arr = [1,2,3,2,1, 5]

start , end = 0, 0
# 부분합이 m 보다 작으면 start 1 증가 부분합 초기
# 부분합이 m 보다 크면 end 1증가 
cnt = 0
sum_ = 0
for start in range(n):
    
    while end <= n:
        sum_ =0 
        for i in range(start, end):
            sum_ += arr[i]    

        
        if sum_ == m:
            cnt += 1
            break    
        elif sum_ < m:
            end += 1
        else:       
            break

print(cnt)
