import sqlite3, hashlib
from tkinter import *

window = Tk()

window.title("Password Vault")

def loginScreen():
    window.geometry("250x100")

    label = Label(window, text="Enter master password:")
    label.config(anchor=CENTER)
    label.pack()

    txt = Entry(window, width=10)
    txt.pack()
    button = Button(window, text="Submit")
    button.pack(pady=5)


loginScreen()
window.mainloop()