def factorial_large(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    
    return list(map(int, str(result)))

# Example
print(factorial_large(10))
