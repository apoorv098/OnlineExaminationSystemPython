from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import re,pymysql



root = Tk()
root.title("Registration Form")
root.geometry("1350x700+0+0")
root.iconbitmap("C:\\Users\\apoor\\Desktop\\Tkinter\\logo.ico")



def registerData():
        if(Name.get() == "" or lName.get() == ""
           or Email.get() == "" or password.get() == "" or confirmpassword.get() == "" or contact.get() == ""):
           messagebox.showerror("Error","All fields are required!", parent=root)
        elif(checkValidEmailorNot(Email.get()) == 0):
           messagebox.showerror("Error","Invalid email address", parent=root)
        elif(password.get() != confirmpassword.get()):
            messagebox.showerror("Error","Passwords don't match!", parent=root)
        elif(isValidPhone(contact.get()) == 0):
            messagebox.showerror("Error","Invalid contact number", parent=root)
        else:
            try:
                conn = pymysql.connect(host="localhost", user="root", password="",database="students")
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM studentregistration where email=%s", Email.get())
                row = cursor.fetchone()
                if(row != None):
                    messagebox.showerror("Error","User already exists!", parent=root)
                else:
                    cursor.execute("INSERT INTO studentregistration (fname, lname, contact,email,password) values(%s, %s, %s, %s, %s)",
                                    (Name.get(),
                                     lName.get(),
                                     contact.get(),
                                     Email.get(),
                                     password.get()
                                    ))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","Registration Successfull!", parent=root)
                    clearFields()                 
                                
                                
                                
             
            except Exception as E:
                messagebox.showerror("Error",f"Due to {str(E)}", parent=root)



def checkValidEmailorNot(email):
            regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
            if(re.search(regex, email)):  
                return(1)  
            else:  
                return(0) 
    
def isValidPhone(number):
        pattern = '^[7-9][0-9]{9}$'
        if(re.search(pattern, number)):  
            return(1)  
        else:  
            return(0) 


def clearFields():
        Name.delete(0, END)
        lName.delete(0, END)
        Email.delete(0, END)
        contact.delete(0, END)
        password.delete(0 ,END)
        confirmpassword.delete(0, END)




# Frame
frame = Frame(root, bg="white")
frame.place(x=80,y=100,width=1000, height=800)

title = Label(frame, text="REGISTER HERE",font=("times new roman",16,"bold"), bg="white", fg="green").place(x=50,y=30)

first_name = Label(frame, text="First Name",font=("times new roman",12,"bold"), bg="white", fg="gray").place(x=50,y=90)
Name = Entry(frame, width=26, borderwidth=5, font=("times new roman",14),bg="#E0E0E0")
Name.place(x=50, y=120)


last_name = Label(frame, text="Last Name",font=("times new roman",12,"bold"), bg="white", fg="gray").place(x=500,y=90)
lName = Entry(frame, width=26, borderwidth=5, font=("times new roman",14),bg="#E0E0E0")
lName.place(x=500, y=120)

email = Label(frame, text="Email address",font=("times new roman",12,"bold"), bg="white", fg="gray").place(x=50,y=220)
Email = Entry(frame,  borderwidth=5, font=("times new roman",14),bg="#E0E0E0")
Email.place(x=50, y=250,width=250)


password = Label(frame, text="Password",font=("times new roman",12,"bold"), bg="white", fg="gray").place(x=500,y=220)
password = Entry(frame,  borderwidth=5, font=("times new roman",14),bg="#E0E0E0")
password.place(x=500, y=250,width=250)

cpassword = Label(frame, text="Confirm Password",font=("times new roman",12,"bold"), bg="white", fg="gray").place(x=50,y=360)
confirmpassword = Entry(frame,  borderwidth=5, font=("times new roman",14),bg="#E0E0E0")
confirmpassword.place(x=50, y=390,width=250)

contact = Label(frame, text="Contact Number",font=("times new roman",12,"bold"), bg="white", fg="gray").place(x=500,y=360)
contact = Entry(frame,  borderwidth=5, font=("times new roman",14),bg="#E0E0E0")
contact.place(x=500, y=390,width=250)

tn_image = ImageTk.PhotoImage(file="C:\\Users\\apoor\\Desktop\\Tkinter\\registernow.png")
btn = Button(frame, image=tn_image,bd=0,cursor="hand2", command=registerData).place(x=50,y=460)




    


root.mainloop()

