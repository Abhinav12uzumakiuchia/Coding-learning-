import turtle
t = turtle.Pen()
number = int(turtle.numinput("total circles","how many circles"))
for x in range(number):
    t.speed(99)
    t.pencolor("red")
    t.circle(100)
    t.lt(360/number)
