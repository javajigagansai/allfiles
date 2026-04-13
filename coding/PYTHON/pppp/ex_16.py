#to calculate the marks and grade of the student
print("Enter the name of the student ")
a=(input('enter the name '))
b=(input('enter REG.no '))
m1= int(input('enter the marks in m1:'))
m2= int(input('enter the marks in m2:'))
m3= int(input('enter the marks in m3:'))
total=m1+m2+m3
print("total marks:",total)
avg= total/3
print("avg. marks:",avg)
if avg>=95:
    print("s grade")
elif avg>=90:
    print("A grade")
elif avg>=80:
    print("B grade")
elif avg>=70:
    print("C grade")
elif avg>=60:
    print("D grade")
elif avg>=50:
    print("E grade")
elif avg>=45:
    print("f grade")
elif avg<=45:
    print("NO grade FAIL")