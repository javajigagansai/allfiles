#TO SWAP THE NUMBERS
def swap_numbers(a,b):
    a,b=b,a
    return a,b
a = (int(input('enter the first number(a):')))
b = (int(input('enter the first number(b):')))
a,b=swap_numbers(a,b)
print(f"after swapping:a={h},b={b}")
