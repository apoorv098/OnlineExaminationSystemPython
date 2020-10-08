from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import re,pymysql




root = Tk()
root.title("Your Dashboard")
root.geometry("1350x700+0+0")
root.iconbitmap("C:\\Users\\apoor\\Desktop\\Tkinter\\logo.ico")



frame1 = Frame(root, highlightthickness=2)
frame1.place(x=0,y=0, width=415, relheight=1)
frame1.config(highlightbackground = "black")


name_user = Text(frame1, height=2, width=30)
name_user.pack()


root.mainloop()