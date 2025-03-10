import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red","blue","pink","green","yellow","white"]
for x in range(6):
    t.pencolor(colors[x%6])
    t.speed(9)
    t.fd(100)
    t.lt(60)
