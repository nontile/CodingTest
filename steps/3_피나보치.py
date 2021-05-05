# n = 20
n = int(input())
rs = [0] * (n +1)

def pina(n):

    if n == 0:
        return 0
    if n== 1:
        return 1
    if rs[n] == 0:
        rs[n] = pina(n-1) + pina(n-2)
    return rs[n]

print(pina(n))