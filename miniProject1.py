from tkinter import *
import tkinterinfo as ti
import databaseVer1 as dbv1
import sys
import sqlite3

# root = Tk()
# app = ap.App(master=root)
root = None
app = None

def main():
    global root, app
    args = sys.argv
    print(args)
    # sql = ".read {}".format(args[0])
    print(args)
    root = Tk()
    dbv1.main(args)
    ti.main(root)



if __name__ == "__main__":
    main()