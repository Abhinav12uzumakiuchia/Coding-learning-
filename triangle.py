import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors =["red","blue","green"]
for x in range(3):
    t.pencolor(colors[x%3])
    t.fd(100)
    t.lt(120)
