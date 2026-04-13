# Fibonacci series using Function
def fibonacci_series(n):
    a, b = 0, 1
    print("Fibonacci Series:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
num_terms = int(input("Enter the number of terms: "))
fibonacci_series(num_terms)
