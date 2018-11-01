from tkinter import *
# from tkinter import tkk
# tkinter._test()


# root = Tk()
# content = Frame(root)
# button = Button(content)

# import tkinter as tk

class App(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.create_quit()
        self.create_unField()
        self.create_pwdField()
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
        # and here we get a callback when the user hits return.
        # we will have the program print out the value of the
        # application variable when the user hits return
        self.unEntry.bind('<Key-Return>', self.print_unContents)
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
        # and here we get a callback when the user hits return.
        # we will have the program print out the value of the
        # application variable when the user hits return
        self.pwdEntry.bind('<Key-Return>', self.print_pwdContents)

    def create_quit(self):
        self.quit = Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack()
        return



    def print_unContents(self, event):
        print("hi. contents of entry is now ---->",
              self.unContent.get())
        return

    def print_pwdContents(self, event):
        print("hi. contents of entry is now ---->",
              self.pwdContent.get())
        return


root = Tk()
app = App(master=root)
app.master.title("My Do-Nothing Application")
app.master.maxsize(1000, 400)
app.mainloop()
