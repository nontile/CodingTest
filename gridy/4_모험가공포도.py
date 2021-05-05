# n = 5
# 공포도 2 3 1 2 2
# 한그룹은 공포도 만큼 사람이 있어야 함 , 몇명은 남아도 됨
# 최대 모험그룹수는

n =5
l = [2, 3, 1, 2, 2]
l.sort()

group = 0
cnt = 0
for i in l:
    group += 1
    if group >= i:
        cnt += 1
        group = 0

print(cnt)
