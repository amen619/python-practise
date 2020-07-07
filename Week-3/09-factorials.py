def factorial(n):
    result = 1
    for i in range(1,n+1):
        result = i * result
    return result

for n in range(1,10):
    print(n, factorial(n))