import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red","blue","green","yellow","pink"]
for x in range(5):
    t.pencolor(colors[x%5])
    t.fd(100)
    t.lt(72)
