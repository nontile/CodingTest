def is_prime_number(x):

    for i in range(2, x):
        if x % i ==0:
            return False
    return True

print(is_prime_number(4))
print(is_prime_number(7))

import math
n = 1000

arr = [True for _ in range(n + 1)]

for i in range(2, int(math.sqrt(n)) + 1):

    if arr[i] == True:

        j=2
        while i *j <= n:
            arr[i*j] = False
            j += 1

for i in range(2, n +1):
    if arr[i]:
        print(i, end=" ")
