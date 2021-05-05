# 0<=N<=23

# 00시 00분 00초 부터 시 59분 59초 까지 N시각 중에서 3이 하나라도 포함된는 모든 경우의 수

n = int(input())
# n = 1
cnt =0
for h in range(n +1):
    for m in range(60):
        for s in range(60):
            if "3" in "".join([str(h), str(m), str(s)]):
                cnt += 1
    
print(cnt)