from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import re,pymysql
from loginWindow import Email_pass,pass_pass



root = Tk()
root.title("Your Dashboard")
root.geometry("1350x700+0+0")
root.iconbitmap("C:\\Users\\apoor\\Desktop\\Tkinter\\logo.ico")



def getData():
        global row
        try:
            conn = pymysql.connect(host="localhost", user="root", password="",database="students")
            cursor = conn.cursor()

            cursor.execute("SELECT * from studentregistration \
                            WHERE email = %s and password= %s", (Email_pass, pass_pass))
            row = cursor.fetchone()
                
            conn.close()

        except Exception as E:
            messagebox.showerror("Error", "There is some error connecting!!", parent=root)


def fees():
  print("fees System")

   

frame1 = Frame(root, highlightthickness=2)
frame1.place(x=0,y=0, width=415, relheight=1)
frame1.config(highlightbackground = "black")

frame2 = Frame(root, highlightthickness=2)
frame2.place(x = 440,y=0,width=900,relheight=1)
frame2.config(highlightbackground = "black")

getData()


user_details = list(row)
Label_details= Label(frame1, text="Your Details with us", font=("times new roman",16,"bold"), bg="white", fg="green").place(x=70,y=10)
st = "selected"
Label_name = Label(frame1, text=user_details[1] + " " + user_details[2], font=("times new roman",16,"bold"), bg="white", fg="green").place(x=10,y=50)
Label_email = Label(frame1, text=user_details[3], font=("times new roman",16,"bold"), bg="white", fg="green").place(x=10,y=90)
Label_contact = Label(frame1, text=user_details[5], font=("times new roman",16,"bold"), bg="white", fg="green").place(x=10,y=120)


check_merit_status = Label(frame2, text="Exam Status", font=("times new roman",16,"bold"), bg="white", fg="green").place(x = 400, y = 20)
merit_status_answer = Label(frame2, text="passed", font=("times new roman",16,"bold"), bg="white", fg="green").place(x = 600, y = 20)

Interview_status =   Label(frame2, text="Interview Status", font=("times new roman",16,"bold"), bg="white", fg="green").place(x = 400, y = 60)
Interview_status_answer = Label(frame2, text="selected", font=("times new roman",16,"bold"), bg="white", fg="green").place(x = 600, y = 60)


seat_status = Label(frame2, text="Seat Status", font=("times new roman",16,"bold"), bg="white", fg="green").place(x = 400, y = 90)
seat_status_answer = Label(frame2, text="Available", font=("times new roman",16,"bold"), bg="white", fg="green").place(x = 600, y = 90)


button_pay_fees = Button(frame2, text="Pay fees", font=("times new roman", 16, "bold"),cursor="hand2",bg="#00FF00",fg="white",command=fees)
button_pay_fees.place(x = 400, y = 150)

if(Interview_status_answer['text'] == "selected"):
    button_pay_fees.config(state=NORMAL, command=fees)
else:
    button_pay_fees.config(state=DISABLED)



root.mainloop()