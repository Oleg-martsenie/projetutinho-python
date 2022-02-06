from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

class Login: 
    def __init__ (self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False, False)

        #Background-Image
        self.bg=ImageTk.PhotoImage(file="images/pybg2.jpg")
        self.bg_image=Label(self.root, image=self.bg).place(x=0,y=0, relwidth=1, relheight=1)

        #Login-Frame
        Frame_login = Frame(self.root, bg="#FFFFFF")
        Frame_login.place(x=330, y=150, width=500, height=350)
        
        #Title&Subtitle
        title = Label(Frame_login, text="Welcome, enter your datas", font=("Impact", 20), fg="#454545", bg="#FFFFFF").place(x=90, y=30)
        subTitle = Label(Frame_login, text="User area", font=("Goudy old style", 12), fg="#2c2c2c", bg="#FFFFFF").place(x=90, y=100)

        #Registry
        registryUser = Label(Frame_login, text="Enter your registry", font=("Goudy old style", 12), fg="#222222", bg="#FFFFFF").place(x=90, y=140)
        self.registry = Entry(Frame_login, font=("Goudy old style", 12), bg="#EEEEEE")
        self.registry.place(x=90, y=170, width=320, height=30)

        #Password
        passwordUser = Label(Frame_login, text="Enter your password", font=("Goudy old style", 12), fg="#222222", bg="#FFFFFF").place(x=90, y=210)
        self.password = Entry(Frame_login, font=("Goudy old style", 12), bg="#EEEEEE")
        self.password.place(x=90, y=240, width=320, height=30)

        #Button
        forget = Button(Frame_login,text="FORGOT PASSWORD?", bd=0,cursor="hand2" ,font=("Goudy old style", 8), fg="#555555", bg="#FFFFFF").place(x=90, y=280)

        #Submit-Button
        submit = Button(Frame_login, 
        # command=self.check_function,
        cursor="hand2",
        text="ACCESS", bd=2,
        font=("Goudy old style", 8, "bold"), 
        fg="#000", bg="#eee").place(x=90, y=310, width=320, height=30)

        def access_function(self) :
            if self.registry.get()=="" or self.password.get()=="":
                messagebox.showerror("Error","Please, Fill the Fields", parent=self.root)
            
            elif self.registry.get()!="T800258" or self.password.get()!="tech2022&guest":
                messagebox.showerror("Error","Registry or Password invalid, Try again", parent=self.root)

            else:
                messagebox.showinfo("Welcome", f"Welcome { self.registry.get() }")


root = Tk()
obj = Login(root)
root.mainloop()