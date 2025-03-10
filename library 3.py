import turtle
t = turtle.Pen()
a = turtle.textinput("please choose","choose yes to run or no to cancel")
if a == "yes":
    y = turtle.numinput("please confirm","choose the pensize")
    b = turtle.textinput("please confirm","choose the pencolor")
    d = turtle.textinput("please confirm","choose the color")
    c = turtle.textinput("please confirm","choose the background")
    r = turtle.numinput("please confirm","choose the radius")
    turtle.bgcolor(c)
    t.pensize(y)
    t.pencolor(b)
    t.fillcolor(d)
    t.begin_fill()
    t.circle(r)
    t.end_fill()
elif a == "no":
    print("ok no problem boss")
else:
    print("invalid enter")
    
