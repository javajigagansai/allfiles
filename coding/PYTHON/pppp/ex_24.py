# Factorial
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result
number=int(input('enter the number'))
print(f"The factorial of {number} (using while loop) is: {factorial(number)}")
#to check the year leap or not
