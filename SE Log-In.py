import tkinter


window = tkinter.Tk()
window.title("Login")
window.geometry("300x300")

UNLabel = tkinter.Label(window, text="User Name")
UNEntry = tkinter.Entry(window)
PassLabel = tkinter.Label(window, text="Password")
PassEntry = tkinter.Entry(window)

UNLabel.pack()
UNEntry.pack()
PassLabel.pack()
PassEntry.pack()

window.mainloop()
