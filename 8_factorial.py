# # 10 3628800

# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1)

# print(factorial(5))

# 피나보치

def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)

n = int(input())
print(fibonacci(n))
    