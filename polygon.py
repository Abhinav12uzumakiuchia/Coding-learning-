import turtle
t = turtle.Pen()
t.pencolor("red")
side = int(turtle.numinput("please confirm","enter side"))
l =  int(turtle.numinput("please confirm","enter length"))
angle = 360/side
for x in range(side):
    t.fd(l)
    t.lt(angle)
