from tkinter import *
import datainfo as di

widgetDict = dict()

def main(parent):
    global widgetDict
    parent.title("Rider App")
    parent.maxsize(1000, 400)
    parent.minsize(1000, 400)
    initialCreate(parent)
    return parent

def initialCreate(parent):
    global widgetDict
    create_eField(parent)
    create_pwdField(parent)
    create_bQuit(parent)
    create_bAlpha(parent, "Login")
    create_bBeta(parent, "Click here to Register")
    create_tGamma(parent, "Please enter your email and password")

    return    
    
def create_eField(parent):
    global widgetDict
    eEntry = Entry(parent, width=25)
    eEntry.pack(side=LEFT)
    content = "email"        
    eEntry.insert(0, content)
    widgetDict["eField"] = eEntry 
    return
    
def create_pwdField(parent):
    global widgetDict
    pwdEntry = Entry(parent, width=25, show="*")
    pwdEntry.pack(side=LEFT)
    content = "password"        
    pwdEntry.insert(0, content)
    widgetDict["pwdField"] = pwdEntry
    return
    
def create_nField(parent):
    global widgetDict
    nEntry = Entry(parent, width=25)
    nEntry.pack(side=LEFT)
    content = "Full name"        
    nEntry.insert(0, content)
    widgetDict["nField"] = nEntry
    return
    
def create_pField(parent):
    global widgetDict
    pEntry = Entry(parent, width=25)
    pEntry.pack(side=LEFT)
    content = "Phone# - ###-###-####"        
    pEntry.insert(0, content)
    widgetDict["pField"] = pEntry
    return
    
def create_tGamma(parent, tb):
    global widgetDict
    tCanvas = Canvas(parent, width=300, height=100)
    tCanvas.pack(side=RIGHT)
    textboxID = tCanvas.create_text(1,1, text=tb, width=300,anchor=NW)
    widgetDict["tCanvas"] = tCanvas
    widgetDict["tGamma"] = (textboxID, tb)
    # print("textbox is {} and has type {}".format(textbox, type(textbox)))
    return
    
    
#  Credit to Voo for the command lambda function idea
# https://stackoverflow.com/questions/6920302/how-to-pass-arguments-to-a-button-command-in-tkinter
def create_bAlpha(parent, tb):
    global widgetDict
    aButton = Button(parent, text=tb, command=lambda: buttonClick(parent, tb))
    aButton.pack(side=TOP)
    widgetDict["bAlpha"] = (aButton, tb)
    return

def create_bBeta(parent, tb):
    global widgetDict
    bButton = Button(parent, text=tb, command=lambda: buttonClick(parent,tb))
    bButton.pack(side=TOP)
    widgetDict["bBeta"] = (bButton, tb)
    return  
            
def create_bQuit(parent):
    global widgetDict
    bQuit = Button(parent, text="QUIT", fg="red",
                          command=parent.destroy)
    bQuit.pack(side=TOP)
    widgetDict["bQuit"] = bQuit    
    return

def buttonClick(parent, tb):
    global widgetDict
    # print(widgetDict)
    if tb == "Login":
        loginCommand()
    elif tb == "Register":
        registerCommand()
    elif tb == "Click here to Register":
        create_rScreen(parent)
    elif tb == "Click here to Login":
        create_lScreen(parent)
    return    

def loginCommand():
    global widgetDict
    eField = widgetDict["eField"]
    pwdField = widgetDict["pwdField"]
    loginT = di.searchLogin(eField.get(), pwdField.get())
    if loginT:
        pass
        # TODO: Create main menu screen
        nText = "Successful login!  Please wait while we develop this app"
        textboxID = widgetDict["tGamma"][0]
        widgetDict["tCanvas"].itemconfig(textboxID, text=nText)   
    else:
        nText = "Incorrect email or password, please try again"
        textboxID = widgetDict["tGamma"][0]
        widgetDict["tCanvas"].itemconfig(textboxID, text=nText)    
    return          
    
def registerCommand():
    global widgetDict
    eField = widgetDict["eField"]
    pwdField = widgetDict["pwdField"]
    pField = widgetDict["pField"]
    nField = widgetDict["nField"]
    regT = di.registerUser(eField.get(), pwdField.get(),pField.get(),nField.get())
    if regT[0] == 1:
        nText = "Successful registration!  Return to Login page to login"
        textboxID = widgetDict["tGamma"][0]
        widgetDict["tCanvas"].itemconfig(textboxID, text=nText)
    elif regT[0] == 0 and regT[1] == 0:
        nText = "email address is already registered, please login to your account"
        textboxID = widgetDict["tGamma"][0]
        widgetDict["tCanvas"].itemconfig(textboxID, text=nText) 
    elif regT[0] == 0 and regT[1] == 1:
        nText = "email address syntax is incorrect, please enter a proper email"
        textboxID = widgetDict["tGamma"][0]
        widgetDict["tCanvas"].itemconfig(textboxID, text=nText)     
    elif regT[0] == 0 and regT[1] == 2:
        nText = "phone number syntax is incorrect, please enter a proper phone number"
        textboxID = widgetDict["tGamma"][0]
        widgetDict["tCanvas"].itemconfig(textboxID, text=nText)      
    print(regT)
    return       
                                    
def create_rScreen(parent):
    global widgetDict
    widgetDict["bBeta"][0].destroy()
    widgetDict["bAlpha"][0].destroy()
    del widgetDict["bBeta"]  
    del widgetDict["bAlpha"]
    create_bAlpha(parent, "Register")
    create_bBeta(parent, "Click here to Login")  
    create_nField(parent)
    create_pField(parent)
    nText = "Please enter an email, password, phone number and your full name"
    textboxID = widgetDict["tGamma"][0]
    widgetDict["tCanvas"].itemconfig(textboxID, text=nText)
    return  
    
def create_lScreen(parent):
    global widgetDict
    widgetDict["bBeta"][0].destroy()
    widgetDict["bAlpha"][0].destroy()
    del widgetDict["bBeta"]  
    del widgetDict["bAlpha"]
    widgetDict["nField"].destroy()
    widgetDict["pField"].destroy()
    del widgetDict["nField"]
    del widgetDict["pField"]
    create_bAlpha(parent, "Login")
    create_bBeta(parent, "Click here to Register")
    nText = "Please enter your email and password"
    textboxID = widgetDict["tGamma"][0]
    widgetDict["tCanvas"].itemconfig(textboxID, text=nText)
    return
    
            
if __name__ == "__main__":
    root = Tk()
    main(root)    