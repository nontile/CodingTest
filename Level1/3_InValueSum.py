"""
10미만의 자연수에서 3과 5의 배수를 구하면 3,5,6,9이다. 이들의 총합은 23이다.
1000미만의 자연수에서 3,5의 배수의 총합을 구하라.
"""
_sum = 0
for x in range(1, 1000):
    if x % 3 ==0 or x % 5 == 0:
        # print(x)
        _sum += x

print(_sum)

total = sum( [x for x in range(1, 1000) if x % 3 ==0 or x % 5 == 0])
print(total)
