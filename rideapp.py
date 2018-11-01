from tkinter import *

class App(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_initWidgets()

    def create_initWidgets(self):
        self.create_quit()
        self.create_unField()
        self.create_pwdField()
        self.create_confirm()
        self.create_register()
        return

    def create_unField(self):
        self.unEntry = Entry()
        self.unEntry.config(width=50)
        self.unEntry.pack(side=LEFT)
        # here is the application variable
        self.unContent = StringVar()
        # set it to some value
        self.unContent.set("Username")
        # tell the entry widget to watch this variable
        self.unEntry["textvariable"] = self.unContent
        return

    def create_pwdField(self):
        self.pwdEntry = Entry(show='*')
        self.pwdEntry.config(width=50)
        self.pwdEntry.pack(side=LEFT)
        # here is the application variable
        self.pwdContent = StringVar()
        # set it to some value
        self.pwdContent.set("Password")
        # tell the entry widget to watch this variable
        self.pwdEntry["textvariable"] = self.pwdContent
        return

    def create_quit(self):
        self.quit = Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side=RIGHT)
        return

    def create_confirm(self):
        self.cButton = Button(self, text="Login", command=checkInfo)
        self.cButton.pack(side=RIGHT)
        return

    def create_register(self):
        self.rButton = Button(self, text="Click to Register",
            command=self.registerScreen)
        self.rButton.pack(side=RIGHT)
        return

    def print_unContents(self, event):
        print(self.unContent.get())
        return

    def print_pwdContents(self, event):
        print(self.pwdContent.get())
        return

    def registerScreen(self):
        print("Register button works")
        self.unEntry.destroy()
        self.pwdEntry.destroy()
        self.cButton.destroy()
        self.rButton.destroy()
        self.create_rScreen()
        return

    def create_rScreen(self):
        print("Function call works, te be implemented")
        return

def checkInfo():
    print("Print statement demonstrates how to grab un and pwd")
    print(app.unContent.get(), app.pwdContent.get())
    return

root = Tk()
app = App(master=root)
app.master.title("My Do-Nothing Application")
app.master.maxsize(1000, 400)
app.master.minsize(1000, 400)
app.mainloop()
