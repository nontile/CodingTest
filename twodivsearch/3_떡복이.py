# 절단기 높이 h
# 높이가 H 보다 높으면 잘리고 낮으면 잘리지 않는다

# 높이 15
# 떡길이 19, 14, 10, 17 
# 잘린것의 합 4 +0 + 0 + 2 = 6

# 떡 갯수
n = 4

# 요청한 떡의 길이 6


# m(6) 만큼가져갈 수 있는 절단기 높이의 최대값

# 조건 범위가 클때 이진탐색 생각

# 시작 0 끝 19 중간 9
# 요청한 떠길이 m 을 만족하면 리스트에 
# 리스트중 최고의 중간 값을 찾으면

target =6

arr = [19, 15, 10, 17]

start=0
end=max(arr)
rs = 0
while True:
    
    sum_ = 0
    if start > end: break

    mid = (start + end) //2

    for val in arr:
        if val > mid:
            sum_ += val - mid

    if sum_ >= target:
        rs = mid
        start = mid + 1
    else:
        end = mid - 1

    print(rs)




# def binary_search(arr, target, start, end, rs):
#     if start > end:
#         return rs

#     sum_ = 0
#     mid = (start + end) // 2

#     for i in arr:
#         r = i - mid
#         if r > 0:
#             sum_ += r
    
#     # print(start, end, rs, mid)
#     if sum_ >= target:
#         return binary_search(arr, target, mid +1 , end, mid)
#     else:
#         return binary_search(arr, target, start, mid - 1, rs)

# print(binary_search(arr, target, 0 ,max(arr), -1))



