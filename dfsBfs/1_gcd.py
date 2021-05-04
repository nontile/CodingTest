def factorial(n):

    if n <= 1:
        return 1
    
    return n * factorial(n-1)

print(factorial(5))

def gcd(a, b):
    if a % b ==0:
        return b
    
    return gcd(b, a%b)

print(gcd(162,192))