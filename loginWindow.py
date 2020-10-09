from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import re,pymysql


root1 = Tk()
root1.title("Login")
root1.geometry("1350x700+0+0")
root1.iconbitmap("C:\\Users\\apoor\\Desktop\\Tkinter\\logo.ico")


def registerWindow():
         root1.destroy()
         import RegistrationWindow


def getData():
    global Email_pass
    global pass_pass
    Email_pass = Email.get()
    pass_pass = password.get()

    
    if(Email.get() == "" or password.get() == ""):
        messagebox.showerror("Error","Fields cannot be empty", parent=root)
    else:
        try:
            conn = pymysql.connect(host="localhost", user="root", password="",database="students")
            cursor = conn.cursor()
            cursor.execute("SELECT * from studentregistration \
                            WHERE email = %s and password= %s", (Email.get(), password.get()))
            row = cursor.fetchone()
            if(row == None):
                messagebox.showerror("Error", "This user don't exists!", parent=root1)
            else:
                root1.destroy()
                import Dashboard
            conn.close()

        except Exception as E:
            messagebox.showerror("Error", "There is some error connecting!!", parent=root1)




        
# Frame
frame = Frame(root1, bg="white")
frame.place(x=80,y=100,width=1000, height=800)


title = Label(frame, text="LOGIN HERE",font=("times new roman",16,"bold"), bg="white", fg="green").place(x=360,y=30)
        
email = Label(frame, text="Email address",font=("times new roman",12,"bold"), bg="white", fg="gray").place(x=320,y=150)
Email = Entry(frame,  borderwidth=5, font=("times new roman",14),bg="#E0E0E0")
Email.place(x=320, y=170,width=250)

password = Label(frame, text="Password",font=("times new roman",12,"bold"), bg="white", fg="gray").place(x=320,y=250)
password = Entry(frame,  borderwidth=5, font=("times new roman",14),bg="#E0E0E0")
password.place(x=320, y=280,width=250)

forget_pass = Button(frame, text="New user?", font=("times new roman",12,"bold"), cursor="hand2", fg = "red",command=registerWindow).place(x=320, y=320)


btn_login = Button(frame, text="Login", font=("times new roman", 16, "bold"),cursor="hand2",bg="#00FF00",fg="white", command=getData).place(x = 400, y = 360)

root1.mainloop()





