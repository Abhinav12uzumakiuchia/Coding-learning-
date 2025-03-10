from tkinter import*
r = Tk()
r.title("calculator")
def click1():
    mylabel1 = Label(r,text = "1")
    mylabel1.pack()
def click2():
    mylabel2 = Label(r,text = "2")
    mylabel2.pack()
myButton1 = Button(r,text = "1",padx = 40,command = click1)
myButton1.pack()
myButton2 = Button(r,text = "2",padx = 40,pady = 40,command = click2)
myButton2.pack()
##work is not complete
