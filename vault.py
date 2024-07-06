import sqlite3, hashlib
from tkinter import *
from tkinter import simpledialog
from functools import partial

# Connect to the database
with sqlite3.connect("password_vault.db") as db:
    cursor = db.cursor()

# Create tables if they do not exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS masterpassword(
id INTEGER PRIMARY KEY,
password TEXT NOT NULL);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS vault(
id INTEGER PRIMARY KEY,
website TEXT NOT NULL,
username TEXT NOT NULL,
password TEXT NOT NULL);
""")

# Function to prompt the user for input
def popUP(text):
    answer = simpledialog.askstring("Input String", text)
    return answer

# Create the main application window
window = Tk()
window.title("Password Vault")

# Hashing function for passwords
def hashPassword(input):
    hash = hashlib.md5(input)
    hash = hash.hexdigest()
    return hash

# Function to display the first screen for setting the master password
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
    txt1.focus()

    label2 = Label(window)
    label2.pack()

    def savePassword():
        if txt.get() == txt1.get():
            hashedPassword = hashPassword(txt.get().encode("utf-8"))

            insert_password = """INSERT INTO masterpassword(password) VALUES(?)"""
            cursor.execute(insert_password, [(hashedPassword)])
            db.commit()

            passwordVault()
        else:
            label2.config(text="Passwords do not match")

    button = Button(window, text="Save", command=savePassword)
    button.pack(pady=10)

# Function to display the login screen for entering the master password
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

# Function to display the password vault
def passwordVault():
    for widget in window.winfo_children():
        widget.destroy()

    window.geometry("800x350")

    label = Label(window, text="Password Vault")
    label.grid(column=1, row=0)

    button = Button(window, text="+", command=addEntry)
    button.grid(column=1, row=1, pady=10)

    label = Label(window, text="Website")
    label.grid(row=2, column=0, padx=88)
    label = Label(window, text="Username")
    label.grid(row=2, column=1, padx=88)
    label = Label(window, text="Password")
    label.grid(row=2, column=2, padx=88)

    cursor.execute("SELECT * FROM vault")
    entries = cursor.fetchall()

    for i, entry in enumerate(entries):
        label1 = Label(window, text=entry[1], font=("Helvetica", 12))
        label1.grid(column=0, row=i + 3)
        label2 = Label(window, text=entry[2], font=("Helvetica", 12))
        label2.grid(column=1, row=i + 3)
        label3 = Label(window, text=entry[3], font=("Helvetica", 12))
        label3.grid(column=2, row=i + 3)

        button = Button(window, text="Delete", command=partial(removeEntry, entry[0]))
        button.grid(column=3, row=i + 3, pady=3)

def addEntry():
    text1 = "Website"
    text2 = "Username"
    text3 = "Password"

    website = popUP(text1)
    username = popUP(text2)
    password = popUP(text3)

    insertFields = """INSERT INTO vault(website, username, password) VALUES(?, ?, ?)"""
    cursor.execute(insertFields, (website, username, password))
    db.commit()

    passwordVault()

def removeEntry(id):
    cursor.execute("DELETE FROM vault WHERE id = ?", (id,))
    db.commit()
    passwordVault()

check = cursor.execute("SELECT * FROM masterpassword")
if cursor.fetchall():
    loginScreen()
else:
    firstScreen()

window.mainloop()
