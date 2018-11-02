from tkinter import *
import rideapp as ap

# root = Tk()
# app = ap.App(master=root)
root = None
app = None

def main():
    global root, app
    root = Tk()
    app = ap.App(master=root)
    app.master.title("Ride Application")
    app.master.maxsize(1000, 400)
    app.master.minsize(1000, 400)
    app.mainloop()

if __name__ == "__main__":
    main()

def checkInfo(app):
    print("In check Info")
    if app.screen == "Login":
        print(app.eContent.get(), app.pwdContent.get())
        return
    elif app.screen == "Register":
        print(app.eContent.get(), app.pwdContent.get(),
                app.nContent.get(), app.pContent.get())
        return
    return  
