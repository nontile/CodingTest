"""
  배열의 최대값, 최소값, 중간값을 구하라  
"""

arr = [8, 5, 9, 21, 2]
arr.sort()
# print(arr)

print("Max: " + str(arr[len(arr)-1]), end="\n")
print("Min: " + str(arr[0]), end="\n")
print("Mid: " + str(arr[len(arr)//2]) , end="")