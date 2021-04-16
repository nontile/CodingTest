# 1개 이상의 숫자 배열
# 홀수, 하나빼고 모두 쌍으로 이루워짐 
# [9, 3, 9, 3, 9, 7, 9]
# return 7

# def solution(odd_arr):
#     rs = []
#     for x in array:
#         if len(rs) < 1:
#             rs.append(x)
#         else:
#             if x in rs:
#                 rs.remove(x)
#             else:
#                 rs.append(x)
#     return rs[0]


array = [9, 3, 9, 3, 9, 7, 9]
def solution(odd_arr):
    dict_ = {}
    for i in array:
        try:
            dict_[i] += 1
        except:
            dict_[i] = 1

    for x in dict_:
        print(x, dict_[x])

        if dict_[x] % 2 != 0:
            return x
print(solution(array))