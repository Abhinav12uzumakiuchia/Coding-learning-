import turtle
t = turtle.Pen()
a = turtle.textinput("please choose","choose yes to run or no to cancel")
if a == "yes":
    y = turtle.numinput("please confirm","choose the pensize")
    b = turtle.textinput("please confirm","choose the pencolor")
    c = turtle.textinput("please confirm","choose the background")
    r = turtle.numinput("please confirm","choose the radius")
    turtle.bgcolor(c)
    t.pensize(y)
    t.pencolor(b)
    t.circle(r)
elif a == "no":
    print("ok no problem boss")
else:
    print("invalid enter")
