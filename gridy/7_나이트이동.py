# 수평2 수직1 또는 수직2 수평 1
# 8 X 8 좌표
# row 1-8 / column a-h

# 나이트가 a1 에 있을 때 이동할 수 있는 경우의 수
#    ur ul rr rl dr dl lr ll

# x = ord(input()) - ord('a') + 1
# y = int(input())
# print(x, y)

# cnt = 0
# dy = [1, -1, 2, 2, 1, -1, -2, -2]
# dx = [-2, -2, 1, -1, 2, 2, -1, 1]

# for i in range(8):
#     px = x + int(dx[i])
#     py = y + int(dy[i])

#     if 1 <= px <= 8 and 1 <= py <= 8:
#         cnt += 1

# print(cnt)

# 대문자와 숫자(0-9) 문자열을 오른차순으로
# AJKDLSI412K4JSJ9D

s = "AJKDLSI412K4JSJ9D"
alpa = []
nums = 0
for i in s:
    if i.isalpha():
        alpa.append(i)
    else:
        nums += int(i)
alpa.sort()
alpa.append(str(nums))

print("".join(alpa))