import sqlite3, hashlib
from tkinter import *

window = Tk()

window.title("Password Vault")


def firstScreen():
    window.geometry("250x150")

    label = Label(window, text="Enter master password:")
    label.config(anchor=CENTER)
    label.pack()

    txt = Entry(window, width=20, show="*")
    txt.pack()
    txt.focus()

    label1 = Label(window, text="Re-enter password")
    label1.pack()

    txt1 = Entry(window, width=20, show="*")
    txt1.pack()
    txt.focus()

    label2 = Label(window)
    label2.pack()

    def savePassword():
        if txt.get() == txt1.get():
            pass
        else:
            label2.config(text="Passwords do not match")

    button = Button(window, text="Save", command=savePassword)
    button.pack(pady=10)


def loginScreen():
    window.geometry("250x100")

    label = Label(window, text="Enter master password:")
    label.config(anchor=CENTER)
    label.pack()

    def checkPassword():
        password = "Test"

        if password == txt.get():
            passwordVault()
        else:
            txt.delete(0, 'end')
            label1.config(text="Wrong")

    txt = Entry(window, width=20, show="*")
    txt.pack()
    txt.focus()

    label1 = Label(window)
    label1.pack()

    button = Button(window, text="Submit", command=checkPassword)
    button.pack(pady=10)


def passwordVault():
    for widget in window.winfo_children():
        widget.destroy()

    window.geometry("700x350")

    label = Label(window, text="Password Vault")
    label.config(anchor=CENTER)
    label.pack()


firstScreen()
window.mainloop()
