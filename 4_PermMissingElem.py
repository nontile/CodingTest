# N개의 다른 숫자로 구성된 배열
# 중복없다
# 범위 1...(N+1) 요소하나가 빠졌다
# 빠진 요소는?
# [2, 3, 1, 5] => 4

# 요소 Max, Min 을 찾고 그 그의 ioop에서 포함여부 찾기

arr = [2, 3, 1, 5]

# def solution(arr):
#     for i in range(min(arr), max(arr) + 1):
#         if i not in arr:
#             return i


def solution(arr):
    if len(arr) == 0:
        return 1
    arr = sorted(arr)
    for i in range(len(arr)):
        if i + 1 != arr[i]:
            return i + 1
print(solution(arr))