from tkinter import *
import datainfo as di

widgetDict = dict()
currentUser = str()

def main(parent):
    global widgetDict
    parent.title("Rider App")
    parent.maxsize(1000, 400)
    parent.minsize(1000, 400)
    create_lScreen(parent)
    return parent

def create_aField(parent, content):
    global widgetDict
    aEntry = Entry(parent, width=25)
    # aEntry.pack(side=LEFT)
    aEntry.grid(row=1,column=0)
    aEntry.insert(0, content)
    widgetDict["aField"] = aEntry
    return

def create_bField(parent, content, show=None):
    global widgetDict
    bEntry = Entry(parent, width=25, show=show)
    # bEntry.pack(side=LEFT)
    bEntry.grid(row=1, column=1)
    bEntry.insert(0, content)
    widgetDict["bField"] = bEntry
    return

def create_cField(parent, content):
    global widgetDict
    cEntry = Entry(parent, width=25)
    # cEntry.pack(side=LEFT)
    cEntry.grid(row=1, column=2)
    cEntry.insert(0, content)
    widgetDict["cField"] = cEntry
    return

def create_dField(parent, content):
    global widgetDict
    dEntry = Entry(parent, width=25)
    # dEntry.pack(side=LEFT)
    dEntry.grid(row=1, column=3)
    dEntry.insert(0, content)
    widgetDict["dField"] = dEntry
    return
    
def create_eField(parent, content):
    global widgetDict
    eEntry = Entry(parent, width=25)
    # eEntry.pack(side=LEFT)
    eEntry.grid(row=2, column=0)
    eEntry.insert(0, content)
    widgetDict["eField"] = eEntry
    return
    
def create_fField(parent, content):
    global widgetDict
    fEntry = Entry(parent, width=25)
    # fEntry.pack(side=LEFT)
    fEntry.grid(row=2, column=1)
    fEntry.insert(0, content)
    widgetDict["fField"] = fEntry
    return
    
def create_gField(parent, content):
    global widgetDict
    gEntry = Entry(parent, width=25)
    # gEntry.pack(side=LEFT)
    gEntry.grid(row=2, column=2)
    gEntry.insert(0, content)
    widgetDict["gField"] = gEntry
    return
    
def create_hField(parent, content):
    global widgetDict
    hEntry = Entry(parent, width=25)
    # hEntry.pack(side=LEFT)
    hEntry.grid(row=2, column=3)
    hEntry.insert(0, content)
    widgetDict["hField"] = hEntry
    return

def create_bQuit(parent):
    global widgetDict
    bQuit = Button(parent, text="QUIT", fg="red",
                          command=parent.destroy)
    bQuit.grid(row=0, column=0)
    # bQuit.pack(side=TOP)
    widgetDict["bQuit"] = bQuit
    return

#  Credit to Voo for the command lambda function idea
# https://stackoverflow.com/questions/6920302/how-to-pass-arguments-to-a-button-command-in-tkinter
def create_bAlpha(parent, tb):
    global widgetDict
    aButton = Button(parent, text=tb, command=lambda: buttonClick(parent, tb))
    # aButton.pack(side=TOP)
    aButton.grid(row=0, column=1)
    widgetDict["bAlpha"] = (aButton, tb)
    return

def create_bBeta(parent, tb):
    global widgetDict
    bButton = Button(parent, text=tb, command=lambda: buttonClick(parent,tb))
    # bButton.pack(side=TOP)
    bButton.grid(row=0, column=2)
    widgetDict["bBeta"] = (bButton, tb)
    return

def create_tGamma(parent, tb):
    global widgetDict
    tCanvas = Canvas(parent, width=300, height=100)
    # tCanvas.pack(side=RIGHT)
    tCanvas.grid(row=7, column=10)
    textboxID = tCanvas.create_text(1,1, text=tb, width=300,anchor=NW)
    widgetDict["tCanvas"] = tCanvas
    widgetDict["tGamma"] = (textboxID, tb)
    # print("textbox is {} and has type {}".format(textbox, type(textbox)))
    return

def create_lDelta(parent, ls):
    global widgetDict
    lDelta = Listbox(parent, height=20, width=100)
    # lDelta.pack(side=LEFT)
    lDelta.grid(row=8, column=0, columnspan=5)
    for item in ls:
        lDelta.insert(END, item)
    widgetDict["lDelta"] = lDelta
    return

def create_bEpsilon(parent, tb):
    global widgetDict
    bButton = Button(parent, text=tb, command=lambda: buttonClick(parent,tb))
    # bButton.pack(side=TOP)
    bButton.grid(row=0, column=3)
    widgetDict["bEpsilon"] = (bButton, tb)
    return

def create_bZeta(parent, tb):
    global widgetDict
    bButton = Button(parent, text=tb, command=lambda: buttonClick(parent,tb))
    # bButton.pack(side=TOP)
    bButton.grid(row=0, column=4)
    widgetDict["bZeta"] = (bButton, tb)
    return

def create_bEta(parent, tb):
    global widgetDict
    bButton = Button(parent, text=tb, command=lambda: buttonClick(parent,tb))
    # bButton.pack(side=TOP)
    bButton.grid(row=0, column=5)
    widgetDict["bEta"] = (bButton, tb)
    return

def create_bTheta(parent, tb):
    global widgetDict
    bButton = Button(parent, text=tb, command=lambda: buttonClick(parent,tb))
    # bButton.pack(side=TOP)
    bButton.grid(row=0, column=6)
    widgetDict["bTheta"] = (bButton, tb)
    return

def create_bIota(parent, tb):
    global widgetDict
    bButton = Button(parent, text=tb, command=lambda: buttonClick(parent,tb))
    # bButton.pack(side=TOP)
    bButton.grid(row=0, column=7)
    widgetDict["bIota"] = (bButton, tb)
    return

def buttonClick(parent, tb):
    if tb == "Login":
        loginCommand(parent)
    elif tb == "Register":
        registerCommand()
    elif tb == "Click here to Register":
        delete_all()
        create_rScreen(parent)
    elif tb == "Click here to Login":
        delete_all()
        create_lScreen(parent)
    elif tb == "Logout":
        delete_all()
        create_lScreen(parent)
    elif tb == "Main Menu":
        delete_all()
        create_mmScreen(parent)
    elif tb == "Offer a Ride":
        delete_all()
        create_oarScreen(parent)
    elif tb == "Search for Rides":
        delete_all()
        create_sfrScreen(parent)
    elif tb == "Book Members/Cancel Bookings":
        delete_all()
        create_bmcbScreen(parent)
    elif tb == "Post Ride Requests":
        delete_all()
        create_prrScreen(parent)
    elif tb == "Search & Delete Ride Requests":
        delete_all()
        create_sadrrScreen(parent)
    return

def delete_all():
    global widgetDict
    for widget in widgetDict.values():
        if type(widget) == tuple:
            if type(widget[0]) == int:
                pass
            else:
                widget[0].destroy()
        else:
            widget.destroy()
    widgetDict.clear()
    return

def loginCommand(parent):
    global widgetDict, currentUser
    aField = widgetDict["aField"]
    bField = widgetDict["bField"]
    loginT = di.searchLogin(aField.get(), bField.get())
    if loginT:
        currentUser = aField.get()
        delete_all()
        create_mmScreen(parent)
    else:
        nText = "Incorrect email or password, please try again"
        textboxID = widgetDict["tGamma"][0]
        widgetDict["tCanvas"].itemconfig(textboxID, text=nText)
    return

def registerCommand():
    global widgetDict
    aField = widgetDict["aField"]
    bField = widgetDict["bField"]
    dField = widgetDict["dField"]
    cField = widgetDict["cField"]
    regT = di.registerUser(aField.get(), bField.get(),dField.get(),cField.get())
    if regT[0] == 1:
        nText = "Successful registration!  Return to Login page to login"

    elif regT[0] == 0 and regT[1] == 0:
        nText = "email address is already registered, please login to your account"

    elif regT[0] == 0 and regT[1] == 1:
        nText = "email address syntax is incorrect, please enter a proper email"

    elif regT[0] == 0 and regT[1] == 2:
        nText = "phone number syntax is incorrect, please enter a proper phone number"
    textboxID = widgetDict["tGamma"][0]
    widgetDict["tCanvas"].itemconfig(textboxID, text=nText)
    return

def create_rScreen(parent):
    create_bQuit(parent)
    create_bAlpha(parent, "Register")
    create_bBeta(parent, "Click here to Login")
    create_aField(parent, "email")
    create_bField(parent, "password", show="*")
    create_cField(parent, "Full name")
    create_dField(parent, "Phone# - ###-###-####")
    nText = "Please enter an email, password, phone number and your full name"
    create_tGamma(parent, nText)
    return

def create_lScreen(parent):
    create_bQuit(parent)
    create_bAlpha(parent, "Login")
    create_bBeta(parent, "Click here to Register")
    create_aField(parent, "email")
    create_bField(parent, "password", show="*")
    nText = "Please enter your email and password"
    create_tGamma(parent, nText)
    return

def create_mmScreen(parent):
    global currentUser
    create_bQuit(parent)
    create_bAlpha(parent, "Logout")
    create_bBeta(parent, "Offer a Ride")
    create_bEpsilon(parent, "Search for Rides")
    create_bZeta(parent, "Book Members/Cancel Bookings")
    create_bEta(parent, "Post Ride Requests")
    create_bTheta(parent, "Search & Delete Ride Requests")

    messages = di.loadMessages(currentUser, 0)
    create_lDelta(parent, messages)
    return

# Offer a Ride
def create_oarScreen(parent):
    create_bQuit(parent)
    create_bAlpha(parent, "Logout")
    create_bBeta(parent, "Main Menu")
    create_bEpsilon(parent, "Confirm")
    create_aField(parent, "Date")
    create_bField(parent, "# of Seats Avaliable")
    create_cField(parent, "Price per seat")
    create_dField(parent, "Luggage Description")
    create_eField(parent, "Source Location")
    create_fField(parent, "Destination Location")
    create_gField(parent, "OPTIONAL: Car #")
    create_hField(parent, "OPTIONAL: Enroute Locations")   
    return 
    
# Search for Rides
def create_sfrScreen(parent):
    create_bQuit(parent)
    create_bAlpha(parent, "Logout")
    create_bBeta(parent, "Main Menu")
    create_bEpsilon(parent, "Search")
    create_aField(parent, "Key One")
    create_bField(parent, "OPTIONAL: Key Two")
    create_cField(parent, "OPTIONAL: Key Three")
    return
    
#  Book Members/Cancel Bookings
def create_bmcbScreen(parent):
    create_bQuit(parent)
    create_bAlpha(parent, "Logout")
    create_bBeta(parent, "Main Menu")   
    
    return
    
#  Post Ride Requests
def create_prrScreen(parent):
    create_bQuit(parent)
    create_bAlpha(parent, "Logout")
    create_bBeta(parent, "Main Menu")
    create_bEpsilon(parent, "Post")  
    create_aField(parent, "Date")
    create_bField(parent, "Pick up Location Code") 
    create_cField(parent, "Drop off Location Code")
    create_dField(parent, "Price")
    return
    
#  Search and delete ride requests
def create_sadrrScreen(parent):
    create_bQuit(parent)
    create_bAlpha(parent, "Logout")
    create_bBeta(parent, "Main Menu")

    return

if __name__ == "__main__":
    root = Tk()
    main(root)
