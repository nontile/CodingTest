n = 5
k = 3

a = [1,2,5,4,3]
b = [5,5,6,6,5]

# 오름차순
a.sort()

# 내림차순
b.sort(reverse=True)

for i in range(k):
    if a[i] >= b[i]:
        break
    else:
        a[i], b[i] = b[i], a[i]

print(a, b)

print(sum(a))