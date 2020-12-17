from tkinter import *

#this is a small gui with hello world
"""
widget = Label(None,text = "Hello World")
widget.pack_configure()
widget.mainloop()
"""

window = Tk()
#the breadth and length ie the size of the gui
window.geometry("300x300")
#the title
window.title("what are you looking for")
#this label contains text font which is the type of the font
label1 = Label(window,text = "welcome to tkinter",fg="red",bg= "black",relief="solid", font=("arial",16,"bold")).pack()
label2 = Label(window,text = "wlecome to GIIT",fg= "blue",bg = "red",relief="solid",font=("italic",16,"bold")).pack()
window.mainloop()

