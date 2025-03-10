import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red","blue","pink","green","yellow","white"]
for x in range(100):
    fillcolor = ("green")
    t.pencolor(colors[x%6])
    t.speed(60)
    t.fd(x)
    t.lt(60)
