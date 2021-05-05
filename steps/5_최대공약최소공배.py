# n, m = 24, 18
n, m = map(int, input().split())
n_arr = []
m_arr = []
a = 0 # 최대공약수
b = 0 # 최소공배수
for i in range(n, 0, -1):
    if m % i == 0 and n % i == 0:
        a = i
        break

for i in range(1, 10000):
    b = m * i
    if b % n == 0:
        break

print(a)
print(b)