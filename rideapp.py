from tkinter import *
import miniProject1 as mp

class App(Frame):
    
    screen = "Login"
    
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_initWidgets()

    def create_initWidgets(self):
        self.create_quit()
        self.create_eField()
        self.create_pwdField()
        self.create_confirm("Login")
        self.create_register()
        self.create_text()
        self.screen = "Login"
        return

    def create_text(self):
        self.canvas = Canvas(width=200, height=100)
        self.canvas.pack(side=LEFT)
        tbtext = "Please Enter your email and password"
        self.textbox = self.canvas.create_text(1,1, text=tbtext,
            width=400,anchor=NW)
        return

    def create_quit(self):
        self.bQuit = Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.bQuit.pack(side=LEFT)
        return

    def create_confirm(self, tb):
        self.cButton = Button(self, text=tb, command=self.buttonClick)
        self.cButton.pack(side=LEFT)
        return

    def create_register(self):
        self.rButton = Button(self, text="Click to Register",
            command=self.registerScreen)
        self.rButton.pack(side=LEFT)
        return

    def registerScreen(self):
        self.eEntry.destroy()
        self.pwdEntry.destroy()
        self.cButton.destroy()
        self.rButton.destroy()
        self.create_rScreen()
        return

    def create_rScreen(self):
        tbtext = "Please enter your email, full name,\nphone number and password"
        self.screen = "Register"
        self.canvas.itemconfig(self.textbox, text=tbtext)
        self.create_eField()
        self.create_nField()
        self.create_pField()
        self.create_pwdField()
        self.create_confirm("Submit")
        return

    def create_eField(self):
        
        self.e = Entry(width=50)
        self.e.pack()

        self.e.focus_set()
        # self.eEntry = Entry(state=NORMAL)
        # self.eEntry.focus_set()
        # self.eEntry.config(width=25)
        # self.eEntry.pack(side=LEFT)        
        # # here is the application variable
        # self.eContent = StringVar()
        # # set it to some value
        # self.eContent.set("email")
        # # tell the entry widget to watch this variable
        # self.eEntry["textvariable"] = self.eContent
        return

    def create_nField(self):
        self.nEntry = Entry()
        self.nEntry.config(width=25)
        self.nEntry.pack(side=LEFT)
        # here is the application variable
        self.nContent = StringVar()
        # set it to some value
        self.nContent.set("Full Name")
        # tell the entry widget to watch this variable
        self.nEntry["textvariable"] = self.nContent
        return

    def create_pField(self):
        self.pEntry = Entry()
        self.pEntry.config(width=25)
        self.pEntry.pack(side=LEFT)
        # here is the application variable
        self.pContent = StringVar()
        # set it to some value
        self.pContent.set("Phone Number")
        # tell the entry widget to watch this variable
        self.pEntry["textvariable"] = self.pContent
        return

    def create_pwdField(self):
        self.pwdEntry = Entry(show='*')
        self.pwdEntry.config(width=25)
        self.pwdEntry.pack(side=LEFT)
        # here is the application variable
        self.pwdContent = StringVar()
        # set it to some value
        self.pwdContent.set("Password")
        # tell the entry widget to watch this variable
        self.pwdEntry["textvariable"] = self.pwdContent
        return
        
    def buttonClick(self):
        mp.checkInfo(self)
        return

# def checkInfo(app):
#     print("app.screen is ", app.screen)
#     if app.screen == "Login":
#         print(app.eContent.get(), app.pwdContent.get())
#         mp.functionHi()
#         return
#     elif app.screen == "Register":
#         print(app.eContent.get(), app.pwdContent.get(),
#                 app.nContent.get(), app.pContent.get())
#         return

# root = Tk()
# app = App(master=root)
# app.master.title("My Do-Nothing Application")
# app.master.maxsize(1000, 400)
# app.master.minsize(1000, 400)
# app.mainloop()
