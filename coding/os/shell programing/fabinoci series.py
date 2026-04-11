n=int(input("Enter the number of terms: "))
a,b=0,1
print("Fibonacci Series:")
for _ in range(n):
    print(a)
    a,b=b,a+b