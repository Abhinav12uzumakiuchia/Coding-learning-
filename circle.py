import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors =["green","white","yellow","red"]
for x in range(120):
    t.speed(90)
    t.pencolor(colors[x%4])
    t.circle(x)
    t.lt(92)
               

