arr = [0] * 101

def pana(n):

    if n == 0 or n == 1:
        return 1
    
    if arr[n]:
        return arr[n]

    arr[n] = pana(n-1) + pana(n-2)
    return arr[n]

print(pana(100))