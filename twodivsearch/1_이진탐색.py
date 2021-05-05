n = 10
target = 7

# arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19] # 4
arr = [1, 3, 5, 6, 9, 11, 13, 15, 17, 19] # None


def binary_search(arr, target, start, end):
    while True:
        if start > end: break

        mid = (start + end) //2

        if arr[mid] == target:
            return mid
        
        elif arr[mid] > target:
            end = mid -1

        else:
            start = mid + 1
    
    return None



# def binary_search(arr, target, start, end):
#     # 탐색범위에 데이터가 없는 경우임
#     if start >  end:
        
#         return None

#     mid = (start + end) // 2

#     if arr[mid] == target:
#         return mid
    
#     elif arr[mid] > target:
#         return binary_search(arr, target, start, mid -1)
    
#     else:
#         return binary_search(arr, target, mid +1, end)


rs = binary_search(arr, target, 0, n-1)
if rs == None:
    print("not exist")
else:
    print(rs + 1)