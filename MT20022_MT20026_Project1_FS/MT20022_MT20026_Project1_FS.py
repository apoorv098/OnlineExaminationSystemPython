from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox
import re,pymysql

def front_page():
    page1 = Tk()
    page1.geometry("1920x1080")
    page1.title("Welcome Page")
    page1.config(bg="white")

    # BG image
    bgi = ImageTk.PhotoImage(file="institute.jpg")
    Label(image=bgi).place(x=200, y=0, relwidth=1, relheight=1)

    # Left Image
    left = ImageTk.PhotoImage(file="logo.png")
    Label(image=left).place(x=80, y=250, width=693, height=490)

    # Frame
    frame = Frame(bg="white")
    frame.place(x=773, y=220, width=1050, height=550)

    #Welcome
    title = Label(frame, text="REGISTER HERE", font=("times new roman", 30, "bold"), bg="white", fg="green").place(x=100,y=30)

    #entries
    Label(frame, text="First Name", font=("times new roman", 12, "bold"), bg="white", fg="gray").place(x=50, y=90)
    Entry(frame, width=26, borderwidth=5, font=("times new roman", 14), bg="#E0E0E0").place(x=50, y=120)

    last_name = Label(frame, text="Last Name", font=("times new roman", 12, "bold"), bg="white", fg="gray").place(x=500,y=90)
    lName = Entry(frame, width=26, borderwidth=5, font=("times new roman", 14), bg="#E0E0E0").place(x=500, y=120)

    email = Label(frame, text="Email address", font=("times new roman", 12, "bold"), bg="white", fg="gray").place(x=50,y=210)
    Email = Entry(frame, borderwidth=5, font=("times new roman", 14), bg="#E0E0E0").place(x=50, y=240, width=250)

    dob = Label(frame, text="Date of Birth", font=("times new roman", 12, "bold"), bg="white",fg="gray").place(x=500, y=210)
    DOB = Entry(frame, borderwidth=5, font=("times new roman", 14), bg="#E0E0E0").place(x=500, y=240,width=250)

    password = Label(frame, text="Password", font=("times new roman", 12, "bold"), bg="white", fg="gray").place(x=50,y=330)
    password = Entry(frame, borderwidth=5, font=("times new roman", 14), bg="#E0E0E0").place(x=50, y=360, width=250)

    cpassword = Label(frame, text="Confirm Password", font=("times new roman", 12, "bold"), bg="white",fg="gray").place(x=500, y=330)
    confirmpassword = Entry(frame, borderwidth=5, font=("times new roman", 14), bg="#E0E0E0").place(x=500, y=360,width=250)

    contact = Label(frame, text="Contact Number", font=("times new roman", 12, "bold"), bg="white", fg="gray").place(x=50,y=450)
    Entry(frame, borderwidth=5, font=("times new roman", 14), bg="#E0E0E0").place(x=50, y=470, width=250)

    tn_image = ImageTk.PhotoImage(file="register.png")
    btn = Button(frame,image=tn_image, bd=0, cursor="hand2").place(x=520, y=470)
    # btn = Button(frame, image=self.tn_image, bd=0, cursor="hand2", command=self.registerData).place(x=50, y=460)

    log_image = ImageTk.PhotoImage(file="login.png")
    Button(image=log_image, bd=0,bg="white",cursor="hand2").place(x=280, y=660)


    # # Register Frame
    # frame1 = Frame(self.root, bg="gray86")
    # frame1.place(x=773, y=220, width=900, height=550)
    #
    # title = Label(frame1, text="Register Here", font=("times new roman", 30, "bold"), bg="gray92", fg="gray36").place(
    #     x=50, y=30)

    page1.mainloop()


def checkValidEmailorNot(self,email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, email)):
        return (1)
    else:
        return (0)


def isValidPhone(self, number):
    pattern = '^[7-9][0-9]{9}$'
    if (re.search(pattern, number)):
        return (1)
    else:
        return (0)

def registerData(self):
    if (self.Name.get() == "" or self.lName.get() == ""
            or self.Email.get() == "" or self.password.get() == "" or self.confirmpassword.get() == "" or self.contact.get() == ""):
        messagebox.showerror("Error", "All fields are required!", parent=self.root)
    elif (self.checkValidEmailorNot(self.Email.get()) == 0):
        messagebox.showerror("Error", "Invalid email address", parent=self.root)
    elif (self.password.get() != self.confirmpassword.get()):
        messagebox.showerror("Error", "Passwords don't match!", parent=self.root)
    elif (self.isValidPhone(self.contact.get()) == 0):
        messagebox.showerror("Error", "Invalid contact number", parent=self.root)


front_page()