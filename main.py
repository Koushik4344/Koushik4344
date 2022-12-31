from cProfile import label
from email.mime import image
from tkinter import*
from tkinter import ttk
from turtle import width
from PIL import Image,ImageTk
from student import Student
import tkinter
from time import strftime
from datetime import datetime
import datetime as dt
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from devoloper import Devoloper
from help import Help



class Face_recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x970+0+0")
        self.root.title("Face recognition tecnology created by MCA")

        #1stimg
        img=Image.open(r"college_image\image4.gif")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        first_lbl=Label(self.root,image=self.photoimg)
        first_lbl.place(x=0,y=0,width=500,height=130)

        #2nd img
        img1=Image.open(r"college_image\images7.jpeg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        first_lbl=Label(self.root,image=self.photoimg1)
        first_lbl.place(x=500,y=0,width=500,height=130)

        #3rdimg
        img2=Image.open(r"college_image\image3.gif")
        img2=img2.resize((550,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        first_lbl=Label(self.root,image=self.photoimg2)
        first_lbl.place(x=1000,y=0,width=550,height=130)


        #background ima
        img3=Image.open(r"college_image\image11.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        #title
        t_l=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",30,"bold"),bg="white",fg="red")
        t_l.place(x=0,y=0,width=1600,height=45)

        #.........time.............
        def time():
            string = strftime("%H:%M:%S")
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(t_l,font=("times new roman",15,"bold"),bg="white",fg="blue")
        lbl.place(x=0,y=20,width=150,height=20)
        time()

        #.........Date.....
        # def date():
        #     date_now=strftime("%d-%m-%y")
        #     lbl.config(text=date_now)
        #     lbl.after(,date)

        # lbl=Label(t_l,font=("times new roman",14,"bold"),bg="white",fg="blue")
        # lbl.place(x=0,y=0,width=110,height=20)
        # date()

        date = dt.datetime.now()
        # Create Label to display the Date
        label = Label(t_l, text=f"{date:%A, %d %B, %Y}", font=("times new roman",13,"bold"),bg="white",fg="blue")
        label.place(x=0,y=0,width=220,height=20)
        

        #Student butten
        img4=Image.open(r"college_image\butimg13.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Detalis",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)

        #Detect face butten
        img5=Image.open(r"college_image\images1.jpeg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b2=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_recognition)
        b2.place(x=500,y=100,width=220,height=220)

        b2_2=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_recognition,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_2.place(x=500,y=300,width=220,height=40)


        #Attendens butten
        img6=Image.open(r"college_image\atten.webp")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b3=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance)
        b3.place(x=800,y=100,width=220,height=220)

        b3_1=Button(bg_img,text="Attendance",command=self.attendance,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b3_1.place(x=800,y=300,width=220,height=40)

        
        #Help Disk butten
        img7=Image.open(r"college_image\help.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b4=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help)
        b4.place(x=1100,y=100,width=220,height=220)

        b4_1=Button(bg_img,text="Help Disk",cursor="hand2",command=self.help,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b4_1.place(x=1100,y=300,width=220,height=40)

        #Train Data butten
        img8=Image.open(r"college_image\traindata.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b5=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b5.place(x=200,y=380,width=220,height=220)

        b5_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b5_1.place(x=200,y=580,width=220,height=40)


        #photos  butten
        img9=Image.open(r"college_image\photos.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b6=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b6.place(x=500,y=380,width=220,height=220)

        b6_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b6_1.place(x=500,y=580,width=220,height=40)
        

        #Devoloper butten
        img10=Image.open(r"college_image\dev.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b7=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.devoloper)
        b7.place(x=800,y=380,width=220,height=220)

        b7_1=Button(bg_img,text="Devoloper",cursor="hand2",command=self.devoloper,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b7_1.place(x=800,y=580,width=220,height=40)
        

        #Exit butten
        img11=Image.open(r"college_image\exit.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b8=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.IExit)
        b8.place(x=1100,y=380,width=220,height=220)

        b8_1=Button(bg_img,text="Exit",cursor="hand2",command=self.IExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b8_1.place(x=1100,y=580,width=220,height=40)


    #function button photos
    def open_img(self):
        os.startfile("data")

    #.......Function buttons student.......
    def student_details(self):
        self.new_window=Toplevel(self.root) 
        self.app=Student(self.new_window)  


    def train_data(self):
        self.new_window=Toplevel(self.root) 
        self.app=Train(self.new_window)  

    def face_recognition(self):
        self.new_window=Toplevel(self.root) 
        self.app=Face_Recognition(self.new_window)  

    def attendance(self):
        self.new_window=Toplevel(self.root) 
        self.app=Attendance(self.new_window)

    def devoloper(self):
        self.new_window=Toplevel(self.root) 
        self.app=Devoloper(self.new_window)  

    def help(self):
        self.new_window=Toplevel(self.root) 
        self.app=Help(self.new_window)

    #ecit
    def IExit(self):
        self.IExit=tkinter.messagebox.askyesno("exit","Are you sure Exit this Project",parent=self.root)
        if self.IExit >0:
            self.root.destroy()
        else:
            return
 

    
       



if __name__== "__main__":
    root=Tk()
    obj=Face_recognition(root)
    root.mainloop()


