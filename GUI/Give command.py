from tkinter import*
r = Tk()
r.title("my")
def clickRam():
    mylabel1 = Label(r,text ="I am Ram.\n I am doctor")
    mylabel1.pack()
def clickOm():
    mylabel2 = Label(r,text = "I am Om.\n I am teacher")
    mylabel2.pack()
myButton1 = Button(r,text = "Ram",padx = 40,pady = 40,command = clickRam)
myButton1.pack()
myButton2 = Button(r,text = "Om",padx = 40,pady = 40,command = clickOm)
myButton2.pack()
r.mainloop()
