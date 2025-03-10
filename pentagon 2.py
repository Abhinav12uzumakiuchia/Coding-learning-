import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red","blue","green","yellow","pink"]
for x in range(100):
    t.speed(4)
    t.pencolor(colors[x%5])
    t.pensize (10)
    t.fd(x)
    t.lt(72)
