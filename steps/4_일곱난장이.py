# 7곱난장이의 키합은 100 일곱난장이 키를 오름차순으로
arr = [20, 7, 23, 19, 10, 15, 25, 8, 13]
# import random
# target = 100

# arr = []

# for _ in range(9):
#     arr.append(int(input()))
arr.sort()
sum_ = sum(arr)
target = sum_ - 100
inn = True
for i in range(9):
    if not inn:
        break
    for j in range(9):
        if i == j:
            continue

        if target == arr[i] + arr[j]:
            rs = [i, j]
            inn = False
            break
for i in range(9):
    if i not in rs:
        print(arr[i])
