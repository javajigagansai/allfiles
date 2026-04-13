#TO FIND THE AREA OF TRIANGLE
import math
print("enter the values")
a=int(input('enter the values of a:'))
b=int(input('enter the values of b:'))
c=int(input('enter the values of c:'))
s = (a + b + c) / 2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print('area of the triangle', area)