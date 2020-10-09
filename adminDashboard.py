from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import re,pymysql
from adminWindows import Email_Admin,pass_Admin

root = Tk()
root.title("Admin Dashboard")
root.geometry("1350x700+0+0")
root.iconbitmap("C:\\Users\\apoor\\Desktop\\Tkinter\\logo.ico")


def getData():
        global row
        try:
            conn = pymysql.connect(host="localhost", user="root", password="",database="students")
            cursor = conn.cursor()

            cursor.execute("SELECT * from studentregistration \
                            WHERE email = %s and password= %s", (Email_Admin, pass_Admin))
            row = cursor.fetchone()

            L  = list(row)
            if(L[1] == "Admin" and L[5] == "098"):
                cursor.execute("SELECT id AS ID,fname,lname,contact,email \
                                FROM studentregistration where email != %s", (Email_Admin))
               
                i = 0
                for student in cursor:
                    for j in range(len(student)):
                        e = Label(root, text=student[j],width=20, fg='blue')
                        CheckVar1 = IntVar()
                        C1 = Checkbutton(root, text = "Accept application", variable = CheckVar1, \
                                         onvalue = 1, offvalue = 0, height=5, \
                                         width = 20)
                        e.grid(row=i, column=j)   
                        C1.grid(row=i, column=j+1) 
                    i = i + 1
                    
               
                
            conn.close()

        except Exception as E:
            messagebox.showerror("Error", "There is some error connecting!!", parent=root)

frame1 = Frame(root, highlightthickness=2)
frame1.place(x=0,y=0, relwidth=1, relheight=1)
frame1.config(highlightbackground = "black")

getData()
root.mainloop()