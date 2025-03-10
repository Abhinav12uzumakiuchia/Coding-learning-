from tkinter import*
r = Tk()
r. title("attendence")
var1 = BooleanVar()
Checkbutton(r,text = "present",variable = var1).grid(row = 1,column = 0)
var2 = BooleanVar()
Checkbutton(r,text = "absent",variable = var2).grid(row = 0,column = 0)
r.mainloop()
