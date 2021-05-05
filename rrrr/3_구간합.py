n = 5
data = [10, 20, 30, 40, 50]

sum_ = 0
prefix_sum = [0]

for i in data:
    sum_ += i
    prefix_sum.append(sum_)

left=3
right=4

print(prefix_sum[right] - prefix_sum[left-1])