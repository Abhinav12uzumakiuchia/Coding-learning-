import turtle
t = turtle.Pen()
a = turtle.textinput("please choose","choose yes to run or no to cancel")
if a == "yes":
    y = turtle.numinput("please confirm","choose the pensize")
    b = turtle.textinput("please confirm","choose the pencolor")
    c = turtle.textinput("please confirm","choose the background")
    turtle.bgcolor(c)
    t.pensize(y)
    t.pencolor(b)
    t.circle(90)
elif a == "no":
    print("ok no problem boss")
else:
    print("invalid enter")
    
