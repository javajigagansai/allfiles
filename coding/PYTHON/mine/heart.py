from turtle import *
import math
bgcolor('light pink')
speed(100)
color("red")
pensize(2)
def heart(n):
    x=15*math.sin(n)**3
    y=12*math.cos(n)-5*\
        math.cos(2*n)-2*\
        math.cos(3*n)-\
        math.cos(4*n)
    return x,y
for i in range(18):
    pendown()
    for j in range(0,100):
        x,y=heart(j/15)
        goto(x*1,y*1)
    penup()
    hideturtle()
done()

