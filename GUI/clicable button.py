from tkinter import*
r = Tk()
r.title ("MY friends")
myButton1 = Button(r,text ="Ram",padx  = 50,pady = 50)
myButton2 = Button(r,text ="om",padx = 50,pady = 50)
myButton1.grid(row = 0,column = 0)
myButton2.grid(row = 0,column = 1)
r.mainloop()
