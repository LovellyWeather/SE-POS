from tkinter import *

def addToTimecard(Lbox, entry1, entry2, entry3, entry4):
    e1 = entry1.get()
    e2 = entry2.get()
    e3 = entry3.get()
    e4 = entry4.get()
    fullLine = ""
    fullLine+=str(e1)
    fullLine+="   "
    fullLine+=str(e2)
    fullLine+="   "
    fullLine+=str(e3)
    fullLine+="   "
    fullLine+=str(e4)
    Lbox.insert(END, str(fullLine))
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
    entry4.delete(0,END)

root = Tk()
root.title("Clock In/Out")
root.geometry("500x200")

'''Framezz'''
LeftFrame = Frame(root)
LeftFrame.pack(side=LEFT, fill=BOTH, expand=True)
RightFrame = Frame(root)
RightFrame.pack(side=RIGHT)


'''ListBox'''
CurrentTimecard = Label(LeftFrame, text="Current Timecard Info")
CurrentTimecard.pack()

Scroll = Scrollbar(LeftFrame, orient=VERTICAL)
PreviousHours = Listbox(LeftFrame, yscrollcommand=Scroll.set)

Scroll.pack(side=RIGHT, fill=Y)
PreviousHours.pack(side=LEFT, fill=BOTH, expand=True)

'''Labels/Entries'''
lEnterName = Label(RightFrame, text="Enter Name")
eEnterName = Entry(RightFrame)
lEnterDate = Label(RightFrame, text="Enter Date")
eEnterDate = Entry(RightFrame)
lClockIn = Label(RightFrame, text="Clock In Time")
eClockIn = Entry(RightFrame)
lClockOut = Label(RightFrame, text="Clock Out Time")
eClockOut = Entry(RightFrame)

lEnterName.grid(row=0,column=0)
eEnterName.grid(row=0,column=1)
lEnterDate.grid(row=1,column=0)
eEnterDate.grid(row=1,column=1)
lClockIn.grid(row=2,column=0)
eClockIn.grid(row=2,column=1)
lClockOut.grid(row=3,column=0)
eClockOut.grid(row=3,column=1)

Submit = Button(RightFrame, text="Submit", command=lambda: addToTimecard(PreviousHours, eEnterName, eEnterDate, eClockIn, eClockOut))
Submit.grid(row=4,column=1)


