from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import re,pymysql


root = Tk()
root.title("Login")
root.geometry("1350x700+0+0")
root.iconbitmap("C:\\Users\\apoor\\Desktop\\Tkinter\\logo.ico")
    
# Frame
frame = Frame(root, bg="white")
frame.place(x=80,y=100,width=1000, height=800)

title = Label(frame, text="LOGIN HERE",font=("times new roman",16,"bold"), bg="white", fg="green").place(x=360,y=30)
        
email = Label(frame, text="Email address",font=("times new roman",12,"bold"), bg="white", fg="gray").place(x=320,y=150)
Email = Entry(frame,  borderwidth=5, font=("times new roman",14),bg="#E0E0E0")
Email.place(x=320, y=170,width=250)

password = Label(frame, text="Password",font=("times new roman",12,"bold"), bg="white", fg="gray").place(x=320,y=250)
password = Entry(frame,  borderwidth=5, font=("times new roman",14),bg="#E0E0E0")
password.place(x=320, y=280,width=250)

btn_reg = Button(frame, text="New user?", font=("times new roman", 12), bg="white", bd=0, fg="#B00857").place(x = 320, y = 320)
btn_login = Button(frame, text="Login", font=("times new roman", 16, "bold"),cursor="hand2",bg="#00FF00",fg="white").place(x = 400, y = 360)


root.mainloop()
