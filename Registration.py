from tkinter import *
from PIL import Image,ImageTk

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
        Name = Entry(frame, width=26, borderwidth=5, font=("times new roman",14),bg="#E0E0E0").place(x=50, y=120)
        
        last_name = Label(frame, text="Last Name",font=("times new roman",12,"bold"), bg="white", fg="gray").place(x=500,y=90)
        lName = Entry(frame, width=26, borderwidth=5, font=("times new roman",14),bg="#E0E0E0").place(x=500, y=120)
        
        email = Label(frame, text="Email address",font=("times new roman",12,"bold"), bg="white", fg="gray").place(x=50,y=220)
        Email = Entry(frame,  borderwidth=5, font=("times new roman",14),bg="#E0E0E0").place(x=50, y=250,width=250)

        password = Label(frame, text="Password",font=("times new roman",12,"bold"), bg="white", fg="gray").place(x=500,y=220)
        password = Entry(frame,  borderwidth=5, font=("times new roman",14),bg="#E0E0E0").place(x=500, y=250,width=250)

        cpassword = Label(frame, text="Confirm Password",font=("times new roman",12,"bold"), bg="white", fg="gray").place(x=50,y=360)
        confirmpassword = Entry(frame,  borderwidth=5, font=("times new roman",14),bg="#E0E0E0").place(x=50, y=390,width=250)

        self.tn_image = ImageTk.PhotoImage(file="C:\\Users\\apoor\\Desktop\\Tkinter\\registernow.png")
        btn = Button(frame, image=self.tn_image,bd=0,cursor="hand2").place(x=50,y=460)


root = Tk()
R = Register(root)
root.mainloop()

