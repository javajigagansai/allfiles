# Factorial
n = int(input("Enter number: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print("Factorial:", fact)

# FIFO
queue = []
queue.append(10)
queue.append(20)
queue.append(30)
print("FIFO Output:", queue.pop(0))
