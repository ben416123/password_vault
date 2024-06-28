import sqlite3, hashlib
from tkinter import *

window = Tk()

window.title("Password Vault")


def loginScreen():
    window.geometry("250x100")

    label = Label(window, text="Enter master password:")
    label.config(anchor=CENTER)
    label.pack()

    def checkPassword():
        password = "Test"

        if password == txt.get():
            print("Correct")
        else:
            label1.config(text="Wrong")

    txt = Entry(window, width=20, show="*")
    txt.pack()
    txt.focus()

    label1 = Label(window)
    label1.pack()

    button = Button(window, text="Submit", command=checkPassword)
    button.pack(pady=10)


loginScreen()
window.mainloop()
