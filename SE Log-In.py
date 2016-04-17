from tkinter import *
import os
import ctypes

def checkValidity(entry1, entry2):
    strEntry1 = entry1.get()
    strEntry2 = entry2.get()
    if strEntry1 == "worker":
        os.system("SE Register.py")
    elif strEntry1 == "admin":
        os.system("SE Admin Console.py")
    else:
        ctypes.windll.user32.MessageBoxW(None, "Incorrect Username or Password", "Error", 0)
    print(strEntry1)
    print(strEntry2)
window = Tk()
window.title("Login")
window.geometry("300x300")

UNLabel = Label(window, text="User Name")
UNEntry = Entry(window)
PassLabel = Label(window, text="Password")
PassEntry = Entry(window)

LogIn = Button(window, text="Log In", command=lambda: checkValidity(UNEntry,PassEntry))

UNLabel.pack()
UNEntry.pack()
PassLabel.pack()
PassEntry.pack()
LogIn.pack()

window.mainloop()
