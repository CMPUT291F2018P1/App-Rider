from tkinter import *
# import rideapp as ap
import tkinterinfo as ti
import datainfo as di

# root = Tk()
# app = ap.App(master=root)
root = None
app = None

def main():
    global root, app
    root = Tk()
    di.main()
    ti.main(root)



if __name__ == "__main__":
    main()