import sqlite3, hashlib
from tkinter import *

with sqlite3.connect("password_vault.db") as db:
    cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS masterpassword(
id INTEGER PRIMARY KEY,
password TEXT NOT NULL);
""")

window = Tk()

window.title("Password Vault")

def hashPassword(input):
    hash = hashlib.md5(input)
    hash = hash.hexdigest()

    return hash


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
            hashedPassword = hashPassword(txt.get().encode("utf-8"))

            insert_password = """INSERT INTO masterpassword(password)
            VALUES(?) """
            cursor.execute(insert_password, [(hashedPassword)])
            db.commit()

            passwordVault()
        else:
            label2.config(text="Passwords do not match")

    button = Button(window, text="Save", command=savePassword)
    button.pack(pady=10)


def loginScreen():
    window.geometry("250x100")

    label = Label(window, text="Enter master password:")
    label.config(anchor=CENTER)
    label.pack()

    def getMasterPassword():
        checkHashedPassword = hashPassword(txt.get().encode("utf-8"))
        cursor.execute("SELECT * FROM masterpassword WHERE id = 1 AND password = ?", [(checkHashedPassword)])
        return cursor.fetchall()

    def checkPassword():
        match = getMasterPassword()

        if match:
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


check = cursor.execute("SELECT * FROM masterpassword")
if cursor.fetchall():
    loginScreen()
else:
    firstScreen()

window.mainloop()
