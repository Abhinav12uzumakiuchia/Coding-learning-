from tkinter import*
r = Tk()
r.title("personal details")
Label(r,text = "first name").grid(row = 0,column = 0)
Label(r,text = "last name").grid(row = 1,column = 0)
entry1 = Entry(r)
entry1.grid(row = 0,column = 1)
entry2 = Entry(r)
entry2.grid(row = 1,column = 1)
r.mainloop()
