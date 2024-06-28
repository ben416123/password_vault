import sqlite3, hashlib
from tkinter import *

window = Tk()

window.title("Password Vault")

def loginScreen():
    window.geometry("350x150")

    label = Label(window, text="Enter master password:")
    label.config(CENTER)
    label.pack()

window.mainloop()