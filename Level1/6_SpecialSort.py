# n개의 정수를 가진 배열이 있다. 이 배열은 양의정수와 음의 정수를 모두 가지고 있다. 
# 이제 당신은 이 배열을 좀 특별한 방법으로 정렬해야 한다.
# 정렬이 되고 난 후, 음의 정수는 앞쪽에 양의정수는 뒷쪽에 있어야 한다. 
# 또한 양의정수와 음의정수의 순서에는 변함이 없어야 한다.

# 예. -1 1 3 -2 2 ans: -1 -2 1 3 2.

numbers = [-1, 1, 3, -2, 2]

# - 확인
# - 이면 왼쪽이 + 면 왼쪽으로 이동
# 이동이 없을때까지 반복

# def minus_left(m):
#     shifted = False
#     for i, n in enumerate(m):
#         if i != 0:
#             if n < 0:
#                 if m[i -1] > 0:
#                     # 빼서 왼쪽으로 이동
#                     mv = m.pop(i)
#                     m.insert(i -1, mv)
#                     shifted = True
#     return (shifted, m)

# run = True
# while run:
#     (run, numbers) = minus_left(numbers)

# print(numbers)


def special_sort(*nums):
    neg = [n for n in nums if n < 0]
    pos = [n for n in nums if n > 0]
    neg.extend(pos)
    return neg
    
rs = special_sort(-1, 1, 3, -2, 2)
print(rs)