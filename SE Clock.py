from tkinter import *

root = Tk()
root.title("Clock In/Out")

'''Framezz'''
LeftFrame = Frame(root)
LeftFrame.pack(side=LEFT)
RightFrame = Frame(root)
RightFrame.pack(side=RIGHT)


'''ListBox'''
CurrentTimecard = Label(LeftFrame, text="Current Timecard Info")
CurrentTimecard.pack()

Scroll = Scrollbar(LeftFrame, orient=VERTICAL)
PreviousHours = Listbox(LeftFrame, yscrollcommand=Scroll.set)

Scroll.pack(side=RIGHT, fill=Y)
PreviousHours.pack(side=RIGHT, fill=Y)

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


