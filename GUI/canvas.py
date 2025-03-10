from tkinter import*
r = Tk()
canvas = Canvas(r,bg = "black",height = 480,width = 270)
coord = 10,60,270,250
arc = canvas.create_arc(coord,start = 0,extent =150,fill = "yellow")
canvas.pack()
r.mainloop()
