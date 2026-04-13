def fibonacci(n):
    return n-1 if n < 3 else fibonacci(n-1) + fibonacci(n-2)

print("Fibonacci series:")
print(*(fibonacci(i) for i in range(1, 11)))
