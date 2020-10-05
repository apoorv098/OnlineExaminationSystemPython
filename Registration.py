from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import re


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Form")
        self.root.geometry("1350x700+0+0")
        self.root.iconbitmap("C:\\Users\\apoor\\Desktop\\Tkinter\\logo.ico")
    

   

        # Frame
        frame = Frame(self.root, bg="white")
        frame.place(x=80,y=100,width=1000, height=800)


        title = Label(frame, text="REGISTER HERE",font=("times new roman",16,"bold"), bg="white", fg="green").place(x=50,y=30)

        first_name = Label(frame, text="First Name",font=("times new roman",12,"bold"), bg="white", fg="gray").place(x=50,y=90)
        self.Name = Entry(frame, width=26, borderwidth=5, font=("times new roman",14),bg="#E0E0E0")
        self.Name.place(x=50, y=120)



        last_name = Label(frame, text="Last Name",font=("times new roman",12,"bold"), bg="white", fg="gray").place(x=500,y=90)
        self.lName = Entry(frame, width=26, borderwidth=5, font=("times new roman",14),bg="#E0E0E0")
        self.lName.place(x=500, y=120)

        email = Label(frame, text="Email address",font=("times new roman",12,"bold"), bg="white", fg="gray").place(x=50,y=220)
        self.Email = Entry(frame,  borderwidth=5, font=("times new roman",14),bg="#E0E0E0")
        self.Email.place(x=50, y=250,width=250)


        password = Label(frame, text="Password",font=("times new roman",12,"bold"), bg="white", fg="gray").place(x=500,y=220)
        self.password = Entry(frame,  borderwidth=5, font=("times new roman",14),bg="#E0E0E0")
        self.password.place(x=500, y=250,width=250)


        cpassword = Label(frame, text="Confirm Password",font=("times new roman",12,"bold"), bg="white", fg="gray").place(x=50,y=360)
        self.confirmpassword = Entry(frame,  borderwidth=5, font=("times new roman",14),bg="#E0E0E0")
        self.confirmpassword.place(x=50, y=390,width=250)

        contact = Label(frame, text="Contact Number",font=("times new roman",12,"bold"), bg="white", fg="gray").place(x=500,y=360)
        self.contact = Entry(frame,  borderwidth=5, font=("times new roman",14),bg="#E0E0E0")
        self.contact.place(x=500, y=390,width=250)

        self.tn_image = ImageTk.PhotoImage(file="C:\\Users\\apoor\\Desktop\\Tkinter\\registernow.png")
        btn = Button(frame, image=self.tn_image,bd=0,cursor="hand2", command=self.registerData).place(x=50,y=460)



    def checkValidEmailorNot(self,email):
            regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
            if(re.search(regex, email)):  
                return(1)  
            else:  
                return(0) 
    
    def isValidPhone(self, number):
        pattern = '^[7-9][0-9]{9}$'
        if(re.search(pattern, number)):  
            return(1)  
        else:  
            return(0) 

    def registerData(self):
        if(self.Name.get() == "" or self.lName.get() == ""
           or self.Email.get() == "" or self.password.get() == "" or self.confirmpassword.get() == "" or self.contact.get() == ""):
           messagebox.showerror("Error","All fields are required!", parent=self.root)
        elif(self.checkValidEmailorNot(self.Email.get()) == 0):
           messagebox.showerror("Error","Invalid email address", parent=self.root)
        elif(self.password.get() != self.confirmpassword.get()):
            messagebox.showerror("Error","Passwords don't match!", parent=self.root)
        elif(self.isValidPhone(self.contact.get()) == 0):
            messagebox.showerror("Error","Invalid contact number", parent=self.root)

    

    





root = Tk()
R = Register(root)
root.mainloop()

