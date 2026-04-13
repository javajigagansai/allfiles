import turtle
t =turtle.Turtle()
turtle.bgcolor("red")
t.speed(0)
colors =["white","yellow","blue","green","gray","orange"]
for i in range(800):
    t.pencolor(colors[i % 6])
    t.forward(i * 1)
    t.right(61)
turtle.done()