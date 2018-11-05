from tkinter import *
import tkinterinfo as ti
import databaseVer1 as dbv1
import sys

# root = Tk()
# app = ap.App(master=root)
root = None
app = None

def main():
    global root, app
    root = Tk()
    dbv1.main()
    ti.main(root)



if __name__ == "__main__":
    main()