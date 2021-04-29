from bisect import bisect_left, bisect_right

a= [1, 2, 4, 4, 8]
x =4

print(bisect_left(a, 4))

print(bisect_right(a,4))


# 특정 범위에 속하는 데이터 개수 구하기

def count_by_range(arr, left, right):
    left_index = bisect_left(arr, left)
    right_index = bisect_right(arr, right)
    return right_index - left_index


arr = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 1번   값이 4인 데이터 개수
print(count_by_range(arr, 4, 4))

# 2번 [-1, 3] 범위에 있는 개수
print(count_by_range(arr, -1, 3))