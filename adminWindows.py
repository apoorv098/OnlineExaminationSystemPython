from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import re,pymysql


root2 = Tk()
root2.title("Admin Login")
root2.geometry("1350x700+0+0")
root2.iconbitmap("C:\\Users\\apoor\\Desktop\\Tkinter\\logo.ico")


# Frame
frame = Frame(root2, bg="white")
frame.place(x=80,y=100,width=1000, height=800)


def getDataAdmin():
    global Email_Admin
    global pass_Admin
    Email_Admin = Email.get()
    pass_Admin = password.get()
    if(Email.get() == "" or password.get() == ""):
        messagebox.showerror("Error","Fields cannot be empty", parent=root2)
    else:
        try:
            conn = pymysql.connect(host="localhost", user="root", password="",database="students")
            cursor = conn.cursor()
            cursor.execute("SELECT * from studentregistration \
                            WHERE email = %s and password= %s", (Email.get(), password.get()))
            row = cursor.fetchone()
            if(row == None):
                messagebox.showerror("Error", "This user don't exists!", parent=root2)
            else:
                root2.destroy()
                import adminDashboard
            conn.close()

        except Exception as E:
            messagebox.showerror("Error", "There is some error connecting!!", parent=root2)


  
    
    

title = Label(frame, text="ADMIN LOGIN HERE",font=("times new roman",16,"bold"), bg="white", fg="green").place(x=360,y=30)
admin_image = ImageTk.PhotoImage(file="C:\\Users\\apoor\\Desktop\\Tkinter\\admin.jpg")
admin_label = Label(image=admin_image, width=100,height=100).place(x=490, y = 160)



email = Label(frame, text="Email address",font=("times new roman",12,"bold"), bg="white", fg="gray").place(x=350,y=170)
Email = Entry(frame,  borderwidth=5, font=("times new roman",14),bg="#E0E0E0")
Email.place(x=350, y=190,width=250)



password = Label(frame, text="Password",font=("times new roman",12,"bold"), bg="white", fg="gray").place(x=350,y=250)
password = Entry(frame,  borderwidth=5, font=("times new roman",14),bg="#E0E0E0")
password.place(x=350, y=280,width=250)



btn_login = Button(frame, text="Login", font=("times new roman", 16, "bold"),cursor="hand2",bg="#00FF00",fg="white", command=getDataAdmin).place(x = 430, y = 340)

root2.mainloop()


