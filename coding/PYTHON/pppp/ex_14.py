#to check the given year is leap or not
A=int(input("enter the year (yyyy)"))
if A%4==0 & A%100==0:
    print("the given year is leap")
else:
    print("the given year is not leap")