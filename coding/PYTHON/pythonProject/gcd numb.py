num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))
while num2 !=0:
    temp=num2
    num2=num1%num2
    num1=temp
print("G.C.D: ",num1)